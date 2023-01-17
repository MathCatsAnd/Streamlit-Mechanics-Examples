import streamlit as st
import subprocess
import os

st.write('Local directory')
ls = os.popen('ls').read()
# ls = os.popen('dir').read()
st.markdown(ls.replace('\n','  \n'))
