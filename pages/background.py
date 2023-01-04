import streamlit as st

css = '''
.stApp {
    background: url('https://raw.githubusercontent.com/MathCatsAnd/Streamlit-Mechanics-Examples/main/files/cat_background.jpg');
}
.stApp > header {
    background-color: transparent;
}

'''
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.write('<div style="background-color: grey; font-size: 3em">Image attribution:<br />' \
    '<a href="https://www.vecteezy.com/vector-art/5298806-seamless-pattern-of-cute-cartoon-cat-illustration-design-on-purple-background">Artwork by psmxp</a><br/>' \
    '<a href="https://www.vecteezy.com/free-vector/cat-pattern">Cat Pattern Vectors by Vecteezy</a></div>',unsafe_allow_html=True)

