import streamlit as st
import pandas as pd
from datetime import datetime

try:
    log = pd.read_csv('files/run_by_script_log.csv')
except:
    log = pd.DataFrame({'Run Time':[]})

now = pd.DataFrame({'Run Time':[str(datetime.now())]})

log = pd.concat([log,now], axis=0, ignore_index=True)

log

log.tail().to_csv('files/run_by_script_log.csv', index=False) 
