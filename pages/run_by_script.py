import streamlit as st
import pandas as pd
from datetime import datetime

try:
    log = pd.read_csv('files/run_by_script_log.csv')
except:
    log = pd.DataFrame({'Run Time':[]})

if 'logged' not in st.session_state:
    st.session_state.logged = False

if st.session_state.logged == False:
    st.session_state.logged = True
    now = pd.DataFrame({'Run Time':[str(datetime.now())]})
    log = pd.concat([log,now], axis=0, ignore_index=True)
    log.tail().to_csv('files/run_by_script_log.csv', index=False) 

log

def again():
    st.session_state.logged = False

st.button('Log Another Time', on_click=again)
st.button('Refresh Logs')