import streamlit as st
from pathlib import Path

p = Path.cwd() / 'files/cat_background.jpg'

st.write(p)

css = f'''
.stApp {{
    background-image: url('{p}');
}}
.stApp > header {{
    background-color: transparent;
}}

'''
st.image('./files/cat_background.jpg')
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

'<a href="https://www.vecteezy.com/free-vector/cat-pattern">Cat Pattern Vectors by Vecteezy</a>'

