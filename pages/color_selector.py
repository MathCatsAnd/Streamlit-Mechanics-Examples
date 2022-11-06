import streamlit as st
import time

def initialize():
    if 'color1' not in st.session_state:
        st.session_state.color1 = '#3A5683'

    if 'color2' not in st.session_state:
        st.session_state.color2 = '#73956F'
    return

initialize()

color1 = st.session_state.color1
color2 = st.session_state.color2

st.button(f'time={time.time()%10}, c1={color1}, ss.c1={st.session_state.color1}, '\
          f'c2={color2}, ss.c2={st.session_state.color2}', key=str(time.time()))

def set_color(color, player):
    if player == 1:
        st.session_state.color1 = color
    else:
        st.session_state.color2 = color
    return

def reset():
    set_color('#3A5683',1)
    set_color('#73956F',2)
    return

st.button('reset', key='reset', on_click = reset)

columns = st.columns(2)

# def show_it_slow():
#     st.write(f'time={time.time()%10}, c1={color1}, ss.c1={st.session_state.color1}, '\
#              f'c2={color2}, ss.c2={st.session_state.color2}')
#     time.sleep(1)
#     return

with columns[0]:
    color1 = st.color_picker('picker1', key='color1')
    st.write(f'color1 is {color1}')
    st.write(f'st.session_state.color1 is {st.session_state.color1}')
    st.button('red1', key='r1', on_click = set_color, args=('#FF0000',1))
    st.button('blue1', key='b1', on_click = set_color, args=('#0000FF',1))
    st.button('green1', key='g1', on_click = set_color, args=('#00FF00',1))


with columns[1]:
    color2 = st.color_picker('picker2', key='color2')
    st.write(f'color2 is {color2}')
    st.write(f'st.session_state.color2 is {st.session_state.color2}')
    st.button('red2', key='r2', on_click = set_color, args=('#FF0000',2))
    st.button('blue2', key='b2', on_click = set_color, args=('#0000FF',2))
    st.button('green2', key='g2', on_click = set_color, args=('#00FF00',2))