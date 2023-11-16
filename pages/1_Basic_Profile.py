import streamlit as st
import time
from pymongo import MongoClient
import components.authenticate as authenticate

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

def edita_perfil(email):
    st.subheader(f"Edit profile")
    with st.form(key='profile_info'):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name")
            location = st.text_input("Location")
        with col2:
            industrial_sector = st.text_input("Industrial Sector")
            num_employees = st.number_input("Number of employees", step=1)
        
        submitted = st.form_submit_button("Save Profile")
        
        if submitted:
            try:
                perfil_data = {
                    "email": email,
                    "company_name": company_name,
                    "location": location,
                    "industrial_sector": industrial_sector,
                    "num_employees": num_employees
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": perfil_data}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Profile saved!")
                time.sleep(3)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_perfil(email):
    st.title("Profile")
    perfil = collection.find_one({"email": email})
    if perfil:
        # st.text(perfil)
        company_name = perfil.get("company_name")
        company_email = perfil.get("email")
        industrial_sector = perfil.get("industrial_sector")
        location = perfil.get("location")
        num_employees = perfil.get("num_employees")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'Name: **{company_name}**')
            st.markdown(f'Location: **{location}**')
            st.markdown(f'Email: **{company_email}**')
        with col2:
            st.markdown(f'Industrial Sector: **{industrial_sector}**')
            st.markdown(f'Number of employees: **{num_employees}**')
        
        with st.sidebar:
            st.write(f'Ahoj, {company_name}!')


# Page start here

if st.session_state["authenticated"]:
    email = st.session_state['email_user']
    # Display profile data
    show_perfil(email)
    st.divider()
    edita_perfil(email)
    authenticate.button_logout()
else:
    st.write("# Edit Profile")
    st.markdown(
        """
        Test Website
        """
    )
    st.markdown('Please Log In')
    authenticate.button_login()