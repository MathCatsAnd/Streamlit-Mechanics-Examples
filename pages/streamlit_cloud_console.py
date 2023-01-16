import streamlit as st
import subprocess
import os

ls = os.popen('ls').read()
ls.replace(' ','  \n')
st.markdown(ls)
