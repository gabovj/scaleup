import streamlit as st
from pymongo import MongoClient
import components.session_forms as session_forms
import components.dashboard as dashboard
import components.authenticate as authenticate

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]
# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)
# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def set_company_and_id(email):
    filter_query = {
        'email_coach': email,
        # 'coach_name': coach_name,
    }
    documents = list(collection.find(filter_query))
    # Filter out documents without 'company_name'
    documents = [doc for doc in documents if 'company_name' in doc]

    # Initialize company_id to None or a default value
    company_id = None
    selected_company = None 

    # Check if documents are found
    if documents:
        # Extract company names and create a mapping to the original documents
        company_names = [doc['company_name'] for doc in documents]
        company_to_doc = {doc['company_name']: doc for doc in documents}

        # Create a form
        with st.form("my_form"):
            # Create a select box within the form
            selected_company = st.selectbox("Select a company:", company_names, index=None)
            # Form submission button
            submitted = st.form_submit_button(":orange[Set Company]")

        if submitted:  # Check if the form has been submitted
            if selected_company:
                selected_doc = company_to_doc[selected_company]
                company_id = selected_doc.get('company_id')

    return selected_company, company_id