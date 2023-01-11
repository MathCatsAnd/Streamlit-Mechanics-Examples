import streamlit as st
from io import StringIO
import pandas as pd

st.header('Replace the informational text inside `st.file_uploader`')

code_block = st.expander('Code')

file = st.file_uploader("Choose a file", type=['csv'])

if file != None:
    bytes_data = file.getvalue()
    string_data = StringIO(bytes_data.decode("utf-8"))
    with string_data as f:
        data = pd.read_csv(string_data)

    data

st.subheader('Options to customize file uploader')

drop_text = st.text_input('Enter text to replace "Drag and drop file here"', value = 'Drag and Drop file here')
limit_text = st.text_input('Enter text to replace "Limit 200MB per file"', value='Limit 200MB per file')

drop_color = ''
limit_color = ''
if st.checkbox('Change text color'):
    drop_color = st.color_picker('Drag and Drop color', value='#FF0000')
    limit_color = st.color_picker('Limit color', value='#FF0000')
    drop_color = f'color:{drop_color}; '
    limit_color = f'color:{limit_color}; '

drop_css=f'''
<style>
[data-testid="stFileUploadDropzone"] div div::before {{{drop_color}content:"{drop_text}"}}
[data-testid="stFileUploadDropzone"] div div span{{display:none;}}

[data-testid="stFileUploadDropzone"] div div::after {{{limit_color}font-size: .8em; content:"{limit_text}"}}
[data-testid="stFileUploadDropzone"] div div small{{display:none;}}
</style>
'''
st.markdown(drop_css, unsafe_allow_html=True)


code = """
import streamlit as st
from io import StringIO
import pandas as pd

file = st.file_uploader("Choose a file", type=['csv'])

if file != None:
    bytes_data = file.getvalue()
    string_data = StringIO(bytes_data.decode("utf-8"))
    with string_data as f:
        data = pd.read_csv(string_data)

    data

st.header('Options to customize file uploader')

drop_text = st.text_input('Enter text to replace "Drag and drop file here"', value = 'Drag and Drop file color')
limit_text = st.text_input('Enter text to replace "Limit 200MB per file"', value='Limit 200MB per file')

drop_color = ''
limit_color = ''
if st.checkbox('Change text color'):
    drop_color = st.color_picker('Drag and Drop color', value='#FF0000')
    limit_color = st.color_picker('Limit color', value='#FF0000')
    drop_color = f'color:{drop_color}; '
    limit_color = f'color:{limit_color}; '

drop_css=f'''
<style>
[data-testid="stFileUploadDropzone"] div div::before {{{drop_color}content:"{drop_text}"}}
[data-testid="stFileUploadDropzone"] div div span{{display:none;}}

[data-testid="stFileUploadDropzone"] div div::after {{{limit_color}font-size: .8em; content:"{limit_text}"}}
[data-testid="stFileUploadDropzone"] div div small{{display:none;}}
</style>
'''
st.markdown(drop_css, unsafe_allow_html=True)
"""

with code_block:
    st.code(code)