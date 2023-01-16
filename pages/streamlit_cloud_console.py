import streamlit as st
import subprocess
import os

st.write(os.popen('ls').read())
