import streamlit as st
import time

NUM_CONTAINERS = 4

if 'side_state' not in st.session_state or 'state' not in st.session_state:
    st.session_state.side_state = [False]*NUM_CONTAINERS
    st.session_state.state = [False]*NUM_CONTAINERS

# collapse ith (indexed by 0) container; expand (i+1)th container if not already expanded
def next (i, where):
    if where =='body':
        script = f'''
        <script>
            let container = parent.document.querySelector("section.main > div > div > div > div:nth-of-type({i+1}) > div [data-testid='stExpander'] ul li div");
            container.click()   
            let next = parent.document.querySelector("section.main > div > div > div > div:nth-of-type({i+2}) > div [data-testid='stExpander'] ul li [aria-expanded='false']");
            if (!(next === null)) {{
                next.click()
            }}
        </script>
        '''
    else:
        script = f'''
        <script>
            let container = parent.document.querySelector("[data-testid='stSidebarNav'] + div > div > div > div > div:nth-of-type({i+1}) > div [data-testid='stExpander'] ul li div");
            container.click()   
            let next = parent.document.querySelector("[data-testid='stSidebarNav'] + div > div > div > div > div:nth-of-type({i+2}) > div [data-testid='stExpander'] ul li [aria-expanded='false']");
            if (!(next === null)) {{
                next.click()
            }}
        </script>
        '''
    with footer:
        temp = st.empty()
        with temp:
            st.components.v1.html(script)
        # remove script after executing so button will not be effectively disabled if clicked twice in a row
        time.sleep(.2)
        temp.write('')
        time.sleep(.2)

def close (i):
    st.session_state.state[i] = False

side_container_0 = st.sidebar.container()
side_container_1 = st.sidebar.container()
side_container_2 = st.sidebar.container()
side_container_3 = st.sidebar.container()

container_0 = st.container()
container_1 = st.container()
container_2 = st.container()
container_3 = st.container()

st.markdown('#### Be sure nothing is mixed in with the containers up until the nth one '\
            'you are trying to format. The introduction of some other div will '\
            'mess up the index to the nth container.')      
side = st.sidebar.radio('Highlight Sidebar Container',[1,2,3,4])
body = st.radio('Highlight Body Container',[1,2,3,4])

footer = st.container()

with side_container_0:
    st.write('This is container 1.')
    with st.expander('Expander 1'):
        st.button('Next', on_click=next, args=[0,'side'], key='side_next_0')
with side_container_1:
    st.write('This is container 2.')
    with st.expander('Expander 2'):
        st.button('Next', on_click=next, args=[1,'side'], key='side_next_1')
with side_container_2:
    st.write('This is container 3.')
    with st.expander('Expander 3'):
        st.button('Next', on_click=next, args=[2,'side'], key='side_next_2')
with side_container_3:
    st.write('This is container 4.')
    with st.expander('Expander 4'):
        st.button('Next', on_click=next, args=[3,'side'], key='side_next_3')

with container_0:
    st.write('This is container 1.')
    with st.expander('Expander 1'):
        st.button('Next', on_click=next, args=[0,'body'], key='next_0')
with container_1:
    st.write('This is container 2.')
    with st.expander('Expander 2'):
        st.button('Next', on_click=next, args=[1,'body'], key='next_1')
with container_2:
    st.write('This is container 3.')
    with st.expander('Expander 3'):
        st.button('Next', on_click=next, args=[2,'body'], key='next_2')
with container_3:
    st.write('This is container 4.')
    with st.expander('Expander 4'):
        st.button('Next', on_click=next, args=[3,'body'], key='next_3')


css_sidebar_container = f'''
<style>
    [data-testid="stSidebarNav"] + div  > div > div > div > div:nth-of-type({side}) 
    [data-testid="stVerticalBlock"] {{background-color:rgba(175,238,238,.2);}}
</style>
'''
css_body_container = f'''
<style>
    section.main > div > div > div > div:nth-of-type({body}) >
    [data-testid="stVerticalBlock"] {{background-color:rgba(175,238,238,.2)}}
</style>
'''
css_radio = '''
<style>
    [role="radiogroup"] {flex-direction: row;}
</style>
'''

footer.markdown(css_sidebar_container,unsafe_allow_html=True)
footer.markdown(css_body_container,unsafe_allow_html=True)
footer.markdown(css_radio,unsafe_allow_html=True)