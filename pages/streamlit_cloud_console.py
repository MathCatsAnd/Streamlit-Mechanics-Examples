import streamlit as st
import subprocess
import os

st.write('Local directory')
ls = os.popen('ls').read()
# ls = os.popen('dir').read()
st.markdown(ls.replace('\n','  \n'))


from base64 import b64encode
def show_pdf():
    """
    displays pdf gnerated and downloads it when prompted
    """
    # to display the pdf
    with open('Streamlit_Student_Ambassadors.pdf', 'rb') as f:
        base64_pdf = b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    # to dowload the pdf
    with open('sample.pdf', 'rb') as file:
        st.download_button(label='Download Invoice', data=file, file_name='receipt.pdf') # defaults to mime='application/octet-stream'

show_pdf()