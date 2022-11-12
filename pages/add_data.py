import streamlit as st
import pandas as pd

st.write('# Solution using a dataframe')

if 'data' not in st.session_state:
    data = pd.DataFrame({'colA':[],'colB':[],'colC':[],'colD':[]})
    st.session_state.data = data

data = st.session_state.data

st.dataframe(data)

def add_dfForm():
    row = pd.DataFrame({'colA':[st.session_state.input_colA],
            'colB':[st.session_state.input_colB],
            'colC':[st.session_state.input_colC],
            'colD':[st.session_state.input_colD]})
    st.session_state.data = pd.concat([st.session_state.data, row])


dfForm = st.form(key='dfForm')
with dfForm:
    dfColumns = st.columns(4)
    with dfColumns[0]:
        st.text_input('colA', key='input_colA')
    with dfColumns[1]:
        st.text_input('colB', key='input_colB')
    with dfColumns[2]:
        st.text_input('colC', key='input_colC')
    with dfColumns[3]:
        st.text_input('colD', key='input_colD')
    st.form_submit_button(on_click=add_dfForm)



st.write('# Solution without using a dataframe')

if 'col1' not in st.session_state:
    st.session_state.col1 = ''
if 'col2' not in st.session_state:
    st.session_state.col2 = ''
if 'col3' not in st.session_state:
    st.session_state.col3 = ''
if 'col4' not in st.session_state:
    st.session_state.col4 = ''

dataColumns = st.columns(4)
with dataColumns[0]:
    st.write('#### col1')
    st.session_state.col1
with dataColumns[1]:
    st.write('#### col2')
    st.session_state.col2
with dataColumns[2]:
    st.write('#### col3')
    st.session_state.col3
with dataColumns[3]:
    st.write('#### col4')
    st.session_state.col4

def add_txtForm():
    st.session_state.col1 += (st.session_state.input_col1 + '  \n')
    st.session_state.col2 += (st.session_state.input_col2 + '  \n')
    st.session_state.col3 += (st.session_state.input_col3 + '  \n')
    st.session_state.col4 += (st.session_state.input_col4 + '  \n')

txtForm = st.form(key='txtForm')
with txtForm:
    txtColumns = st.columns(4)
    with txtColumns[0]:
        st.text_input('col1', key='input_col1')
    with txtColumns[1]:
        st.text_input('col2', key='input_col2')
    with txtColumns[2]:
        st.text_input('col3', key='input_col3')
    with txtColumns[3]:
        st.text_input('col4', key='input_col4')
    st.form_submit_button(on_click=add_txtForm)    