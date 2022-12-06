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
    log.tail(10).to_csv('files/run_by_script_log.csv', index=False) 

st.write(log.tail(10))

def again():
    st.session_state.logged = False

st.button('Log Another Time', on_click=again)
st.button('Refresh Logs')

st.markdown('This page can be scheduled to execute remotely by script using '\
    'Selenium with Chromedriver. If an app has an expensive caching operation '\
    'to perform that is shared between sessions, this is one way to prompt the '\
    'app to run.')

st.code('''
from selenium import webdriver
import time

url = 'https://mathcatsand-examples.streamlit.app/run_by_script'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
page = browser.get(url)
time.sleep(10)
browser.quit()
''')