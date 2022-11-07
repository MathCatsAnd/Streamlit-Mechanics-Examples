import streamlit as st

st.write('# Streamlit Code Snippets and Examples')

with st.expander('color selector'):
    st.write('## Using Buttons to Override or Reset Color Pickers')
    st.write('Re: post from Streamlit Forums user mathcatsand (me!)')
    st.write('[Color-Picker Unexpected Behavior]'\
             '(https://discuss.streamlit.io/t/color-picker-unexpected-behavior'\
             '/32380)')
    st.write('This is an example of using session-state to override values '\
             'stored in an input widget (colorpicker in this case).')

with st.expander('column selector'):
    st.write('## Selecting Columns for Display')
    st.write('Re: post from Streamlit Forums user fruitzebra')
    st.write('[Column selection in the dashboard]'\
             '(https://discuss.streamlit.io/t/column-selection-in-the-'\
             'dashboard/32910)')
    st.write('This is an example of how to select columns for display for a '\
             'data frame with many columns. This first solution uses the '\
             'multiselect widget to specify columns for display, with a choice '\
             'to specify by inclusion or exclusion.')

with st.expander('column selector v2'):
    st.write('## Selecting Columns for Display V2')
    st.write('Re: post from Streamlit Forums user fruitzebra')
    st.write('[Column selection in the dashboard]'\
             '(https://discuss.streamlit.io/t/column-selection-in-the-'\
             'dashboard/32910)')
    st.write('This is an alternate solution to the situation described above. '\
             'Instead of using the multiselect widget to specify columns for '\
             'display, checkboxes are used in a two-column display.')

with st.expander('interacting widget options'):
    st.write('## Restricting Widget Options Depending on Another Widget (Bidirectional)')
    st.write('Re: post from Streamlit Forums user PatrickBalada')
    st.write('[Filter dataframe regardless of the order of selection]'\
             '(https://discuss.streamlit.io/t/filter-dataframe-regardless-of-'\
             'the-order-of-selection/32948)')
    st.write('This shows how widget states and options can be affected by '\
             'other widgets. This example shows two widgets applying a filter '\
             'to a data frame, where each widget gets impossible options '\
             'removed depending on the other widget. Warning: this can result '\
             'in a "dead end" and a reset button is provided for that case.')

with st.expander('relabeling images'):
    st.write('## Relabeling Images')
    st.write('Re: post from Streamlit Forums user Truong_Dang_Manh')
    st.write('[How to display a list of images in groups of 10/50/100?]'\
             '(https://discuss.streamlit.io/t/how-to-display-a-list-of-images'\
             '-in-groups-of-10-50-100/32935)')
    st.write('This is a short example to display images in different batch '\
             'sizes, with the ability to record a note for each as needed. '\
             'Specifically, this example allows a user to mark a label as '\
             'incorrect and provide a new label. Images for this example '\
             'were grabbed from a set on Kaggle marked public domain.')
    st.write('[Images Dataset]'\
             '(https://www.kaggle.com/datasets/pavansanagapati/images-dataset)')