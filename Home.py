# Streamlit template to accept persona, purpose, and text inputs and display the results of the NER model.

import streamlit as st
from src import queries
import json

with open("assets/examples.json") as f:
    EXAMPLES = json.load(f)

st.title("Named Entity Recognition")
st.header("Persona")
persona = st.text_input("Persona", EXAMPLES["merchandiser"]["persona"])
st.header("Purpose")
purpose = st.text_input("Purpose", EXAMPLES["merchandiser"]["purpose"])
st.header("Text")
text = st.text_area("Text", EXAMPLES["merchandiser"]["text"], height=500)

# pass in the persona and purpose to queries.entity_type_suggestions on a button

if st.button("Generate Entity Types"):
    entity_types = queries.entity_type_suggestions(persona, purpose)
    st.write(entity_types)
