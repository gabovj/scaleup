import streamlit as st
import time
from pymongo import MongoClient
import components.authenticate as authenticate
import uuid
from datetime import datetime
import logging

st.set_page_config(
    page_title="Home", 
    page_icon="🆙", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:hola@neuva.com",
        'About': "# Scale Up!"
    }
    )

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]

# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)

# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def new_company(email, coach_name):
    st.subheader(f":orange[Add New Company]")
    with st.form(key='new_company', clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name")
            city = st.text_input("City")
            email_company = st.text_input("Contact Email")
        with col2:
            industrial_sector = st.text_input("Industrial Sector")
            country = st.text_input("Country")
            num_employees = st.number_input("Number of employees", step=1)
        
        submitted = st.form_submit_button(":orange[Create Company Profile]")

        if submitted:
            company_id = str(uuid.uuid4())
            try:
                new_company = {
                    'timestamp': datetime.now(),
                    "email_coach": email,
                    "coach_name": coach_name,
                    "company_id": company_id,
                    "company_name": company_name,
                    "city": city,
                    "country": country,
                    "email_company": email_company,
                    "industrial_sector": industrial_sector,
                    "num_employees": num_employees
                }
                collection.insert_one(new_company)
                st.session_state['company_id'] = company_id
                st.success("Company created Succesfully!")
                st.write(f"company ID: {st.session_state['company_id']}")
                logging.info(f'New company ID generated: {company_id}')
                return st.session_state['company_id']
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                st.error(f"An error occurred: {e}")
                return None

def show_companies_by_coach(email, coach_name):
    st.subheader(f":orange[Companies coached by {coach_name}]")
    filter_query = {
        'email_coach': email,
        'coach_name': coach_name,
    }
    documents = list(collection.find(filter_query))
    # Initialize company_id to None or a default value
    company_id = None

    # Check if documents are found
    if documents:
        # Extract company names and create a mapping to the original documents
        company_names = [doc['company_name'] for doc in documents]
        company_to_doc = {doc['company_name']: doc for doc in documents}

        # Create a select box with company names
        selected_company = st.selectbox("Select a company:", company_names, index=None)

        # Display information about the selected company
        if selected_company:
            selected_doc = company_to_doc[selected_company]
            # st.write(f"Company Name: :orange[{selected_company}]")

            # Use columns for layout
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Company Name:** :orange[{selected_doc.get('company_name', 'N/A')}]")
                location = f"{selected_doc.get('city', 'N/A')}, {selected_doc.get('country', 'N/A')}"
                st.write(f"**Location:** :orange[{location}]")
                st.write(f"**Contact:** {selected_doc.get('email_company', 'N/A')}")

            with col2:
                st.write(f"**Company ID:** :orange[{selected_doc.get('company_id', 'N/A')}]")
                st.write(f"**Sector:** :orange[{selected_doc.get('industrial_sector', 'N/A')}]")
                st.write(f"**Number of Employees:** :orange[{selected_doc.get('num_employees', 'N/A')}]")
            
            company_id = selected_doc.get('company_id')            
            # Delete button
            col1, col2, col3 =st.columns(3)
            with col2:
                if st.button(":red[Delete Company]"):
                    delete_company(email, company_id)

    else:
        st.write("No documents found.")
    return company_id

def edita_perfil(email, company_id):
    existing_data = collection.find_one({"email_coach": email, "company_id": company_id})
    prefill_data = existing_data if existing_data else {}
    st.subheader(f":orange[Edit company profile]")
    with st.form(key='edit_company_profile'):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name", value=prefill_data.get('company_name', ''))
            city = st.text_input("City", value=prefill_data.get('city', ''))
            email_company = st.text_input("Contact Email", value=prefill_data.get('email_company', ''))
        with col2:
            industrial_sector = st.text_input("Industrial Sector", value=prefill_data.get('industrial_sector', ''))
            country =st.text_input("Country", value=prefill_data.get('country', ''))
            # Ensure num_employees is a number, default to 0 if not
            num_employees_default = prefill_data.get('num_employees', 0)
            num_employees = st.number_input("Number of employees", step=1, value=num_employees_default)
        
        submitted = st.form_submit_button(":orange[Edit Company Profile]")
        
        if submitted:
            try:
                data_edited = {
                    "company_name": company_name,
                    "city": city,
                    "country": country,
                    "email_company": email_company,
                    "industrial_sector": industrial_sector,
                    "num_employees": num_employees
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": data_edited}
                 # Update the existing document without upserting
                result = collection.update_one(filter_doc, update_doc)

                if result.matched_count == 0:
                    st.error("No matching document found to update.")
                else:
                    st.success("Profile saved!")
                    time.sleep(1)
                    st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def delete_company(email, company_id):
    """Deletes a company from the database."""
    if company_id:
        try:
            # Perform the deletion
            result = collection.delete_one({'email_coach': email, 'company_id': company_id})

            if result.deleted_count > 0:
                st.success("Company deleted successfully.")
                st.rerun()
            else:
                st.error("No matching company found to delete.")
        except Exception as e:
            st.error(f"An error occurred while deleting the company: {e}")
    else:
        st.error("Invalid company ID.")

# Page start here
if st.session_state["authenticated"]:
    email = st.session_state['email_user']
    coach_name = st.session_state['user_name']
    with st.sidebar:
            st.write(f'Ahoj, {coach_name}!')
    # Add new company
    new_company(email, coach_name)
    # Display profile data
    company_id = show_companies_by_coach(email, coach_name)
    st.divider()
    st.session_state['company_id'] = company_id
    edita_perfil(email, company_id)
    # st.write(st.session_state)
    authenticate.button_logout()
else:
    st.write("# Protected Zone")
    st.markdown(
        """
        
        """
    )
    st.markdown('Please Log In')
    st.markdown('Please Log In')
    st.write(st.session_state)
    authenticate.button_login()