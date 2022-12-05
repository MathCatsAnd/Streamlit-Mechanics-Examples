import streamlit as st
from streamlit import session_state as ss

if 'dates' not in ss:
    ss.dates = 0

st.write(f'Current number of dates omitted: {ss.dates}')

COL_NUM = 6

small_view = st.columns(COL_NUM)

for i in range(ss.dates):
    with small_view[i%COL_NUM]:
        st.date_input('',key=f'date{i}')

def add_date():
    ss.dates += 1

def remove_date():
    ss.dates -= 1

st.button('Add another date', on_click=add_date)
st.button('Remove a date', on_click=remove_date)

date_list = []

for i in range(ss.dates):
    date_list.append(ss[f'date{i}'])

st.write(date_list)