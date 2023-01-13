import streamlit as st
from io import StringIO
import pandas as pd

file, multi = st.tabs(['file_uploader','multiselect'])

with file:
    st.header('Replace the informational text inside `st.file_uploader`')

    file_code_block = st.expander('Code')

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
        drop_color = f' color:{drop_color};'
        limit_color = f' color:{limit_color};'

    file_css=f'''
    <style>
    [data-testid="stFileUploadDropzone"] div div::before {{content:"{drop_text}";{drop_color}}}
    [data-testid="stFileUploadDropzone"] div div span{{display:none;}}

    [data-testid="stFileUploadDropzone"] div div::after {{font-size: .8em; content:"{limit_text}";{limit_color}}}
    [data-testid="stFileUploadDropzone"] div div small{{display:none;}}
    </style>
    '''
    st.markdown(file_css, unsafe_allow_html=True)


    file_code = """
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

st.subheader('Options to customize file uploader')

drop_text = st.text_input('Enter text to replace "Drag and drop file here"', value = 'Drag and Drop file here')
limit_text = st.text_input('Enter text to replace "Limit 200MB per file"', value='Limit 200MB per file')

drop_color = ''
limit_color = ''
if st.checkbox('Change text color'):
    drop_color = st.color_picker('Drag and Drop color', value='#FF0000')
    limit_color = st.color_picker('Limit color', value='#FF0000')
    drop_color = f' color:{drop_color};'
    limit_color = f' color:{limit_color};'

file_css=f'''
<style>
[data-testid="stFileUploadDropzone"] div div::before {{content:"{drop_text}";{drop_color}}}
[data-testid="stFileUploadDropzone"] div div span{{display:none;}}

[data-testid="stFileUploadDropzone"] div div::after {{font-size: .8em; content:"{limit_text}";{limit_color}}}
[data-testid="stFileUploadDropzone"] div div small{{display:none;}}
</style>
'''
st.markdown(file_css, unsafe_allow_html=True)
    """

    with file_code_block:
        st.code(file_code)

with multi:
    st.header('Replace default text inside `st.multiselect`')

    multi_code_block = st.expander('Code')

    choices = st.multiselect('*Felis catus*', ['cat','kitty','kitten','floof','danger-floof','house panther'])

    if choices == []:
        choices = 'None'
    
    st.write(f'Selections made: {choices}')
    
    st.subheader('Options to customize default text')

    select_text = st.text_input('Enter text to replace "Choose an option"', value = '猫')
    
    select_color = ''
    
    if st.checkbox('Change text color', key='multi-color'):
        select_color = st.color_picker('Choose an option', value='#FF0000')
        select_color = f' color:{select_color};'

    multi_css=f'''
    <style>
    .stMultiSelect div div div div div:nth-of-type(2) {{visibility: hidden;}}
    .stMultiSelect div div div div div:nth-of-type(2)::before {{visibility: visible; content:"{select_text}";{select_color}}}
    </style>
    '''
    st.markdown(multi_css, unsafe_allow_html=True)

    multi_code = """
    import streamlit as st

    choices = st.multiselect('*Felis catus*', ['cat','kitty','kitten','floof','danger-floof','house panther'])

if choices == []:
    choices = 'None'

st.write(f'Selections made: {choices}')

st.subheader('Options to customize default text')

select_text = st.text_input('Enter text to replace "Choose an option"', value = '猫')

select_color = ''

if st.checkbox('Change text color', key='multi-color'):
    select_color = st.color_picker('Choose an option', value='#FF0000')
    select_color = f' color:{select_color};'

multi_css=f'''
<style>
.stMultiSelect div div div div div:nth-of-type(2) {{visibility: hidden;}}
.stMultiSelect div div div div div:nth-of-type(2)::before {{visibility: visible; content:"{select_text}";{select_color}}}
</style>
'''
st.markdown(multi_css, unsafe_allow_html=True)
    """

    with multi_code_block:
        st.code(multi_code)