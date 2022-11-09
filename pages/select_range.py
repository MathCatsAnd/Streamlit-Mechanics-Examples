import streamlit as st

values = range(5)
labels = ['first','second','third','fourth','fifth']

selection = st.select_slider('Choose a range',values,value=(1,3), format_func=(lambda x:labels[x]))

st.write(f'The selection is {selection} with values having type {type(selection[0])}.')