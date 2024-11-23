from backend import call_function
import streamlit as st
import pandas as pd

# Load the CSV file
tramits_df = pd.read_csv('/Users/alexlatorre/Documents/GitHub/local_ecityclic/data/tramits.csv')

# Create a dictionary to map Titol to Sequence
titol_to_sequence = dict(zip(tramits_df['Titol'], tramits_df['Sequence']))

# Function to handle the selection change
def on_select_change():
    tramit_input_title = st.session_state.tramit_input_title
    if tramit_input_title == "Select an option":
        return
    tramit_row = tramits_df[tramits_df['Titol'] == tramit_input_title]
    if not tramit_row['Vigent'].values[0]:
        st.write("Aquest tramit no esta disponible ara mateix")
    else:
        # Add the selected tramit to the list of previously searched Tramits
        if tramit_input_title not in st.session_state.searched_tramits:
            st.session_state.searched_tramits.append(tramit_input_title)
        
        # Prepare the input for the model
        tramit_input = [titol_to_sequence[title] for title in st.session_state.searched_tramits]
        result = call_function(tramit_input)
        
        # Check if any prediction is the same as the input
        result = ["Repetir tramit: " + tramit_input_title if r == tramit_input_title else r for r in result]
        st.session_state.result = result

# Function to handle button click
def on_button_click(tramit_title):
    if tramit_title.startswith("Repetir tramit: "):
        tramit_title = tramit_title.replace("Repetir tramit: ", "")
    st.session_state.tramit_input_title = tramit_title
    st.session_state.searched_tramits.append(tramit_title)
    on_select_change()

# Initialize the session state for storing previously searched Tramits and results
if 'searched_tramits' not in st.session_state:
    st.session_state.searched_tramits = []
if 'result' not in st.session_state:
    st.session_state.result = []

# Layout
st.set_page_config(layout="wide")
st.title("Tramits Selector")

col1, col2 = st.columns([1, 3])

with col1:
    st.header("History")
    st.write("Previously searched Tramits:")
    for tramit in st.session_state.searched_tramits:
        st.write(tramit)

with col2:
    st.header("Select Tramit")
    options = ['Select an option'] + tramits_df['Titol'].tolist()
    st.selectbox('Select tramit', options, key='tramit_input_title', on_change=on_select_change)
    
    st.header("Predictions")
    if st.session_state.result:
        for r in st.session_state.result:
            st.button(r, on_click=on_button_click, args=(r,))