import streamlit as st
import pandas as pd

st.write('In this scenario, we have a text input (col1), two numeric inputs ' \
         '(col2 and col3), and a computed column (col4 = col2-col3). ' \
         '(Information validation not included.)')

tab_df, tab_string, tab_widget = solutions = st.tabs(['DataFrame','Strings','Widgets'])

################################################################################
## Solution using a dataframe
################################################################################
with tab_df:
    st.write('# Solution using a dataframe')

    # Create an empty dataframe on first page load, will skip on page reloads
    if 'data' not in st.session_state:
        data = pd.DataFrame({'col1':[],'col2':[],'col3':[],'col4':[]})
        st.session_state.data = data

    # Show current data
    st.dataframe(st.session_state.data)

    st.write('#### Using form submission')

    # Function to append inputs from form into dataframe
    def add_dfForm():
        row = pd.DataFrame({'col1':[st.session_state.input_df_form_col1],
                'col2':[st.session_state.input_df_form_col2],
                'col3':[st.session_state.input_df_form_col3],
                'col4':[st.session_state.input_df_form_col2-st.session_state.input_df_form_col3]})
        st.session_state.data = pd.concat([st.session_state.data, row])

    # Inputs listed within a form
    dfForm = st.form(key='dfForm', clear_on_submit=True)
    with dfForm:
        dfFormColumns = st.columns(4)
        with dfFormColumns[0]:
            st.text_input('col1', key='input_df_form_col1')
        with dfFormColumns[1]:
            st.number_input('col2', step=1, key='input_df_form_col2')
        with dfFormColumns[2]:
            st.number_input('col3', step=1, key='input_df_form_col3')
        with dfFormColumns[3]:
            pass
        st.form_submit_button(on_click=add_dfForm)

    st.write('#### Not using form submission')

    # Function to append non-form inputs into dataframe
    def add_df():
        row = pd.DataFrame({'col1':[st.session_state.input_df_col1],
                'col2':[st.session_state.input_df_col2],
                'col3':[st.session_state.input_df_col3],
                'col4':[st.session_state.input_df_col2-st.session_state.input_df_col3]})
        st.session_state.data = pd.concat([st.session_state.data, row])

    # Inputs created outside of a form (allows computing col4 for preview)
    dfColumns = st.columns(4)
    with dfColumns[0]:
        st.text_input('col1', key='input_df_col1')
    with dfColumns[1]:
        st.number_input('col2', step=1, key='input_df_col2')
    with dfColumns[2]:
        st.number_input('col3', step=1, key='input_df_col3')
    with dfColumns[3]:
        st.number_input('col4', step=1, key='input_df_col4', 
                        value = st.session_state.input_df_col2-st.session_state.input_df_col3, 
                        disabled=True)
    st.button('Submit', on_click=add_df)


################################################################################
## Solution without using a dataframe
################################################################################
with tab_string:
    st.write('# Solution without using a dataframe')

    # Create an empty string for each column (alternatively could use lists)
    if 'txt_col1' not in st.session_state:
        st.session_state.txt_col1 = ''
    if 'txt_col2' not in st.session_state:
        st.session_state.txt_col2 = ''
    if 'txt_col3' not in st.session_state:
        st.session_state.txt_col3 = ''
    if 'txt_col4' not in st.session_state:
        st.session_state.txt_col4 = ''

    # Show current data by displaying column strings
    dataColumns = st.columns(4)
    with dataColumns[0]:
        st.write('#### col1')
        st.session_state.txt_col1
    with dataColumns[1]:
        st.write('#### col2')
        st.session_state.txt_col2
    with dataColumns[2]:
        st.write('#### col3')
        st.session_state.txt_col3
    with dataColumns[3]:
        st.write('#### col4')
        st.session_state.txt_col4

    # Function to append data to column strings
    def add_txtForm():
        st.session_state.txt_col1 += (st.session_state.input_txt_col1 + '  \n')
        st.session_state.txt_col2 += (str(st.session_state.input_txt_col2) + '  \n')
        st.session_state.txt_col3 += (str(st.session_state.input_txt_col3) + '  \n')
        st.session_state.txt_col4 += (str(st.session_state.input_txt_col2 \
                                      -st.session_state.input_txt_col3) + '  \n')

    # Inputs listed within a form
    txtForm = st.form(key='txtForm')
    with txtForm:
        txtColumns = st.columns(4)
        with txtColumns[0]:
            st.text_input('col1', key='input_txt_col1')
        with txtColumns[1]:
            st.number_input('col2', step=1, key='input_txt_col2')
        with txtColumns[2]:
            st.number_input('col3', step=1, key='input_txt_col3')
        with txtColumns[3]:
            pass
        st.form_submit_button(on_click=add_txtForm)    


################################################################################
## Solution using input widgets
################################################################################
with tab_widget:
    st.write('# Solution using input widgets')

    # a selection for the user to specify the number of rows
    num_rows = st.slider('Number of rows', min_value=1, max_value=10)

    # columns to lay out the inputs
    grid = st.columns(4)

    # Function to create a row of widgets (with row number input to assure unique keys)
    def add_row(row):
        with grid[0]:
            st.text_input('col1', key=f'input_col1{row}')
        with grid[1]:
            st.number_input('col2', step=1, key=f'input_col2{row}')
        with grid[2]:
            st.number_input('col3', step=1, key=f'input_col3{row}')
        with grid[3]:
            st.number_input('col4', step=1, key=f'input_col4{row}',
                            value = st.session_state[f'input_col2{row}'] \
                                -st.session_state[f'input_col3{row}'],
                            disabled=True)

    # Loop to create rows of input widgets
    for r in range(num_rows):
        add_row(r)