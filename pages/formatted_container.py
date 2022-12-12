import streamlit as st

with st.sidebar.container():
    st.write('This is container 1.')
with st.sidebar.container():
    st.write('This is container 2.')
with st.sidebar.container():
    st.write('This is container 3.')
with st.sidebar.container():
    st.write('This is container 4.')
side = st.sidebar.radio('Highlight Sidebar Container',[1,2,3,4])

with st.container():
    st.write('This is container 1.')
with st.container():
    st.write('This is container 2.')
with st.container():
    st.write('This is container 3.')
with st.container():
    st.write('This is container 4.')
body = st.radio('Highlight Body Container',[1,2,3,4])

st.markdown('#### Be sure nothing is mixed in with the containers up until the nth one '\
            'you are trying to format. The introduction of some other div will '\
            'mess of the index to the nth container.')

css_sidebar_container = f'''
<style>
    [data-testid="stSidebarNav"] + div [data-testid="stVerticalBlock"] div:nth-of-type({side})
    [data-testid="stVerticalBlock"] {{background-color:rgba(175,238,238,.2);}}
</style>
'''
css_body_container = f'''
<style>
    [data-testid="stSidebar"] + section [data-testid="stVerticalBlock"] div:nth-of-type({body})
    [data-testid="stVerticalBlock"] {{background-color:rgba(175,238,238,.2)}}
</style>
'''
css_radio = '''
<style>
    [role="radiogroup"] {flex-direction: row;}
</style>
'''

st.markdown(css_sidebar_container,unsafe_allow_html=True)
st.markdown(css_body_container,unsafe_allow_html=True)
st.markdown(css_radio,unsafe_allow_html=True)