import streamlit as st

choice = st.radio('Background Type', ['Image', 'Gradient'])

if choice == 'Image':
    st.title('Image Background')
    st.markdown('Boop! :ghost:')

    image = './app/static/house-panther-nose.png'

    css = f'''
    <style>
        .stApp {{
            background-image: url({image});
            background-size: cover;

        }}
        .stApp > header {{
            background-color: transparent;
        }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

else:
    st.title('Gradient Background')
    st.write('Look at the pretty shifting background')

    with open('./files/wave.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)