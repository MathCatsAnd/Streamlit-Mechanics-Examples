import streamlit as st
from math import ceil
import pandas as pd 

def initialize():    
    df = pd.read_csv('file_list.csv', index_col='file')
    df['incorrect']=[False]*df.shape[0]
    df['label']=['']*df.shape[0]
    return df

if 'relabeling_images__df' not in st.session_state:
    df = initialize()
    st.session_state.relabeling_images__df = df
else:
    df = st.session_state.relabeling_images__df 

controls = st.columns(3)
with controls[0]:
    batch_size = st.select_slider("Batch size:",range(5,26), value=8)
with controls[1]:
    row_size = st.select_slider("Row size:", range(1,6), value = 4)
num_batches = ceil(df.shape[0]/batch_size)
with controls[2]:
    page = st.selectbox("Page", range(1,num_batches+1), key='relabeling_images__page')
batch = df.index[(page-1)*batch_size : page*batch_size]

def update (image, col): 
    df.at[image,col] = st.session_state[f'relabeling_images__{col}_{image}']
    if st.session_state[f'relabeling_images__incorrect_{image}'] == False:
       st.session_state[f'relabeling_images__label_{image}'] = ''
       df.at[image,'label'] = ''


grid = st.columns(row_size)
col = 0
for image in batch:
    with grid[col]:
        st.image(image, caption=df.loc[image]['original'])
        st.checkbox("Incorrect", key=f'relabeling_images__incorrect_{image}', 
                    value = df.at[image,'incorrect'], 
                    on_change=update, args=(image,'incorrect'))
        if df.at[image,'incorrect']:
            st.text_input('New label:', key=f'relabeling_images__label_{image}', 
                          value = df.at[image,'label'],
                          on_change=update, args=(image,'label'))
        else:
            st.write('##')
            st.write('##')
            st.write('###')
    col = (col + 1) % row_size

st.write('## Corrections')
df[df['incorrect']==True]


with st.expander('Session State'):
    state = pd.DataFrame({'Attributes':st.session_state.keys(),
                        'Values':st.session_state.values()})
    state[state['Attributes'].apply(lambda x: x.startswith('relabeling_images__')) ]