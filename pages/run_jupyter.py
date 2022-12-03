import streamlit as st
import pandas as pd
import subprocess

greeting = st.selectbox('Select a Greeting',['','Hi','Hey','Hello','\'Sup','Greetings','Howdy'])
name = st.text_input('Name')

if st.button('Submit'):
    if greeting == '' or name == '':
        st.write('Please fill in name and greeting')
    else:
        inputs = pd.DataFrame({'greeting':[greeting],'name':[name]})
        inputs.to_csv('files/my_notebook_inputs.csv', index=False)
        subprocess.run(['jupyter','nbconvert', '--execute', 'files/my_notebook.ipynb', '--to', 'html'])
        with open('files/my_notebook.html','r', encoding='utf-8') as f:
            result = f.read()
        result = result.removeprefix('<!DOCTYPE html>')
        st.components.v1.html(result, height=400, scrolling=True)