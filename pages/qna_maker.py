import pandas as pd
import numpy as np
from math import ceil
import streamlit as st

st.set_page_config(layout='wide')

# Initiate Session State Values
if 'instantiated' not in st.session_state:
    # Answers-to-Questions is a one-to-many relationship
    st.session_state.answers = pd.DataFrame({'Answer':[]})
    # Question are associated to an answer via 'AID' (Answer ID)
    # 'QAID' (Question-Answer ID) is used for distinct placeholder text for a clearer demo
    st.session_state.questions = pd.DataFrame({'AID':[],'QAID':[],'Question':[]})
    st.session_state.aid = 1
    st.session_state.qid = 1
    st.session_state.instantiated = True

# Add a new answer block to the dataframe
def add_answer():
    df_a = st.session_state.answers
    df_q = st.session_state.questions
    # Create answer
    df_a.loc[st.session_state.aid] = [f'Placeholder Answer {st.session_state.aid}']
    # Create question associated to answer
    df_q.loc[st.session_state.qid] = [st.session_state.aid,1,f'Placeholder Question {st.session_state.aid}-1']
    st.session_state.aid += 1
    st.session_state.qid += 1

# Add a new question to an existing answer
def add_question(aid):
    df_q = st.session_state.questions
    # Get the current maximum question placeholder number
    last_question = df_q[df_q['AID']==aid]['QAID'].max()
    if np.isnan(last_question):
        last_question = 0
    # Create question
    df_q.loc[st.session_state.qid] = [aid, last_question+1, f'Placeholder Question {aid}-{last_question+1}']
    st.session_state.qid += 1

# Remove all questions associated to an answer
def clear_questions(aid):
    df_q = st.session_state.questions
    st.session_state.questions = df_q[df_q['AID'] != aid]

# Remove all questions associated to an answer and repopulate with a new question
def reset_questions(aid):
    clear_questions(aid)
    add_question(aid)

# Remove a specific question assocated to an answer
def remove_question(aid,qid):
    df_q = st.session_state.questions
    # If no other questions, clear all (and repopulate with a new question)
    if df_q[df_q['AID']==aid].shape[0] <= 1:
        reset_questions(aid)
    # Otherwise remove question
    else:
        st.session_state.questions = df_q.drop(qid)

# Remove an answer and all associated questions
def remove_answer (aid):
    df_a = st.session_state.answers
    st.session_state.answers = df_a.drop(aid)
    clear_questions(aid)

# Update dataframe with submitted answer text
def commit_answer(aid, widget_key):
    df_a = st.session_state.answers
    df_a.loc[aid] = [st.session_state[widget_key]]

# Update dataframe with submitted question text
def commit_question(qid, widget_key):
    df_q = st.session_state.questions
    df_q.loc[qid, 'Question'] = st.session_state[widget_key]

# Dispaly an answer and all associated questions
def display_qna(aid, render_as='stack'):
    df_a = st.session_state.answers
    df_q = st.session_state.questions
    qna_block = st.container()
    if  render_as == 'stack':
        a_block = qna_block.container()
        q_block = qna_block.container()
        mod_block = qna_block.container()
    else:
        left, right = qna_block.columns(2)
        a_block = left.container()
        q_block = right.container()
        mod_block = left.container()
    a_block.button('Remove QnA', key=f'a_remove_{aid}', on_click=remove_answer, args=[aid])
    a_block.write('## Answer')
    a_block.text_area('Answer',df_a.loc[aid,'Answer'], label_visibility='collapsed', 
            key=f'a_{aid}', on_change=commit_answer, args=[aid,f'a_{aid}'])
    q_block.write('### Questions')
    # Provide auto-numbering of questions via index for user-friendly display
    for index, qid in enumerate(df_q[df_q['AID'] == aid].index, start=1):
        q_block.text_input(str(index),df_q.loc[qid,'Question'], 
                key=f'q_{qid}', on_change=commit_question, args=[qid,f'q_{qid}'])
    qid_list = list(df_q[df_q['AID'] == aid].index)
    mod_block.write('---')

    # Options to modify question list
    mod_block.write('### Modify QnA')
    mod_block.button('Add Question', on_click=add_question, args=[aid], key=f'q_add_{aid}')
    mod_block.button('Remove All Questions', on_click=reset_questions, args=[aid], key=f'q_clear_{aid}')
    # Use format_func to convert between user-facing auto-numbering and internal qid (question id)
    qid = mod_block.selectbox('Specific Question', qid_list, 
            format_func=lambda qid:qid_list.index(qid)+1, key=f'q_select_{aid}')
    mod_block.button('Remove Specific Question', key=f'q_remove_{aid}', on_click=remove_question, args=(aid,qid))
    qna_block.write('<hr style="border-top: 5px solid;" />', unsafe_allow_html=True)

# Helper function to change page number via button callback
def change_page(increment):
    st.session_state.page += increment

# Page controls in Sidebar
with st.sidebar:
    page_columns = st.columns(2)
    a_per_page = page_columns[1].slider('Answers per Page',1, 10,5, key='a_per_page')
    last_page = ceil(len(st.session_state.answers.index)/a_per_page)
    page = page_columns[0].selectbox('Page',range(1,last_page+1), key='page')
    # New columns to facilitate vertical alignment
    page_columns = st.columns(2)

    # Compare current page selection to first and last page number
    if page == 1:
        first = True
    else:
        first = False
    if page == last_page:
        last = True
    else:
        last = False
    # Next/Back buttons for page selection
    page_columns[0].button('Previous', on_click=change_page, args=[-1],
        disabled=first)
    page_columns[1].button('Next', on_click=change_page, args=[1],
        disabled=last)
    st.write('---')
    # Button to add new answer block
    st.button('New QnA', on_click=add_answer)
    display_type = st.radio("List by",['columns','rows'])


# Render QnAs saved to the dataframes
df_a = st.session_state.answers
df_q = st.session_state.questions
answer_index = list(df_a.index)

if len(answer_index) > 0:
    first = (page-1)*a_per_page
    next = min(first + a_per_page, len(answer_index))

    if display_type == 'columns':
        render_qna_item_as = 'stack'
        blocks = st.columns(st.session_state.a_per_page)
    else:
        render_qna_item_as = '2columns'
        blocks = []
        for c in range(st.session_state.a_per_page):
            blocks.append(st.container())
    if len(answer_index) > 0:
        first = (page-1)*a_per_page
        next = min(first + a_per_page, len(answer_index))
        for i in range(first,next):
            with blocks[i%a_per_page]:
                display_qna(answer_index[i], render_qna_item_as)


with st.expander('Saved DataFrames'):
    st.session_state.questions
    st.session_state.answers