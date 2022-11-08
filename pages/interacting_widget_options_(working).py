import streamlit as st
import pandas as pd

# page prefix
pre = 'interacting_widget_options__'

# column selection
col1 = 'fur'
col2 = 'color'

if pre+'widgets' not in st.session_state:
    st.session_state[pre+'widgets'] = 1
w = st.session_state[pre+'widgets']

@st.experimental_memo
def get_data():
    data = pd.DataFrame({'fur':['DSH','DSH','DSH','DSH','DSH','DMH',
                                'DMH','DMH','DLH','DLH','DLH','DLH'],
                        'sex':['M','F','M','M','F','M',
                               'M','F','F','F','F','M'],
                        'color':['White','Black','Orange','Orange','Calico','Orange',
                                 'Black','Brown','Calico','Black','White','Brown']})
    return data

df = get_data()

def initialize(reset):
    if reset or \
       (pre+col1+'_possible') not in st.session_state or \
       (pre+col2+'_possible') not in st.session_state:
       st.session_state[pre+col1+'_possible'] = df[col1].unique()
       st.session_state[pre+col2+'_possible'] = df[col2].unique()

initialize(False)

def reset():
    initialize(True)
    st.session_state[pre+col1+f'_selected_{w}'] = st.session_state[pre+col1+'_possible']
    st.session_state[pre+col2+f'_selected_{w}'] = st.session_state[pre+col2+'_possible']
    st.session_state[pre+'widgets'] = (w+1)%2
    return

st.button('Reset',on_click=reset)

def get_row_values(data, col1, filter1, options1, col2, filter2, options2):
    filter1_list = st.session_state[filter1]
    filter2_list = st.session_state[filter2]

    filtered_data = data[data[col1].isin(filter1_list)]
    available_col2_values = filtered_data[col2].unique()
    st.session_state[filter2] = [selected for selected in filter2_list \
                                 if selected in available_col2_values]
    st.session_state[options2] = available_col2_values

    filter2_list = st.session_state[filter2]

    filtered_data = data[data[col2].isin(filter2_list)]
    available_col1_values = filtered_data[col1].unique()
    st.session_state[options1] = available_col1_values
    st.session_state[filter1] = filter1_list
    return

filter = {}
filter[col1] = st.multiselect(f'Select {col1}',st.session_state[pre+col1+'_possible'], 
                            key=(pre+col1+f'_selected_{w}'), 
                            default = st.session_state[pre+col1+'_possible'],
                            on_change = get_row_values, 
                            args=(df,col1,(pre+col1+f'_selected_{w}'),(pre+col1+'_possible'),
                                  col2,(pre+col2+f'_selected_{w}'),(pre+col2+'_possible')))
filter[col2] = st.multiselect(f'Select {col2}',st.session_state[pre+col2+'_possible'], 
                            key=(pre+col2+f'_selected_{w}'),
                            default = st.session_state[pre+col2+'_possible'],
                            on_change = get_row_values, 
                            args=(df,col2,pre+col2+f'_selected_{w}',pre+col2+'_possible',
                                  col1,pre+col1+f'_selected_{w}',pre+col1+'_possible'))

df[df[col1].isin(filter[col1])][df[col2].isin(filter[col2])]

with st.expander('Session State'):
    state = pd.DataFrame({'Attributes':st.session_state.keys(),
                        'Values':st.session_state.values()})
    state[state['Attributes'].apply(lambda x: x.startswith(pre))]