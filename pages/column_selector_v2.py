import streamlit as st
import pandas as pd



def initialize():
    if 'columns_selector_v2__df' not in st.session_state:
        data = {}
        for i in range(20):
            col = f'col{i}'
            data[col]= range(10)
        st.write('initializing')
        df = pd.DataFrame(data)
        st.session_state.columns_selector_v2__df = df
        st.session_state.columns_selector_v2__columns = list(df.columns)

initialize()

df = st.session_state.columns_selector_v2__df
columns = st.session_state.columns_selector_v2__columns

def set_all(setting):
    for col in list(df.columns):
        st.session_state[f'columns_selector_v2__{col}'] = setting
    if setting:
        st.session_state.columns_selector_v2__columns = list(df.columns)
    else:
        st.session_state.columns_selector_v2__columns.clear()

def move_column(col, state):
    if state:
        st.session_state.columns_selector_v2__columns.append(col)
    else:
        st.session_state.columns_selector_v2__columns.remove(col)


configure = st.columns(2)
with configure[0]:
    st.button('Include All', on_click=set_all, args=(True,))
    included = st.expander('Included', expanded=True)
    with included:
        st.write('')
    
with configure[1]:
    st.button('Exclude All', on_click=set_all, args=(False,))
    excluded = st.expander('Excluded', expanded=True)
    with excluded:
        st.write('')


for col in df.columns:
    if col in st.session_state.columns_selector_v2__columns:
        with included:
            st.checkbox(col,key=f'columns_selector_v2__{col}', value=True, 
                        on_change=move_column, args=(col,False))
    else:
        with excluded:
            st.checkbox(col, key=f'columns_selector_v2__{col}', value=False, 
                        on_change=move_column, args=(col,True))     

df[columns]

st.markdown('''<style>[data-testid="stExpander"] ul [data-testid="stVerticalBlock"] 
               {overflow-y:scroll; max-height:400px;} </style>''', 
               unsafe_allow_html=True)