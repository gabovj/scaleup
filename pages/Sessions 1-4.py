import streamlit as st
from pymongo import MongoClient
import components.session_forms as session_forms
import components.dashboard as dashboard

st.set_page_config(
    page_title="Forms", 
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

email = st.session_state['email_user']

if 'company_id' not in st.session_state:
    st.session_state['company_id'] = None
if 'company_name' not in st.session_state:
    st.session_state['company_name'] = None

def set_company_and_id(email):
    filter_query = {
        'email_coach': email,
        # 'coach_name': coach_name,
    }
    documents = list(collection.find(filter_query))
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

# Page start here
if st.session_state["authenticated"]:
    with st.sidebar:
        st.write(f'Ahoj, {st.session_state["user_name"]}!')
        selected_company, company_id = set_company_and_id(email)

        # Update the session state only if non-None values are returned
        if selected_company is not None:
            st.session_state['company_name'] = selected_company
        if company_id is not None:
            st.session_state['company_id'] = company_id

        # Your existing code for displaying the session state information
        if st.session_state['company_name'] is not None:
            st.write(f"Selected Company: :orange[{st.session_state['company_name']}]")
        else:
            st.warning("No Company Selected")
        if st.session_state['company_id'] is not None:
            st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
        else:
            st.warning("No Company ID")
    
    st.text(st.session_state['company_name'])
    st.text(st.session_state['company_id'])
    st.text(st.session_state['email_user'])
    
    company_id_selected = st.session_state['company_id']
    print(company_id_selected)
    with st.expander("##### 1- Scaling Up - 4 Decisions"):
        session_forms.session_one(email, company_id_selected)

    with st.expander("##### 2- People: Life by design"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Company: :orange[{st.session_state['company_name']}]")
        with col2:
            st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
        st.divider()
        st.markdown('##### :orange[One-Page Personal Plan (OPPP)]')
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Spirituality", "Family", "Friends", "Fitness", "Finance"])
        with tab1:
            session_forms.session_two_spirituality(email, company_id_selected)
        with tab2:
            session_forms.session_two_family(email, company_id_selected)
        with tab3:
            session_forms.session_two_friends(email, company_id_selected)
        with tab4:
            session_forms.session_two_fitness(email, company_id_selected)
        with tab5:
            session_forms.session_two_finance(email, company_id_selected)

    with st.expander("##### 3- People: Right people in the right place"):
        session_forms.session_three(email, company_id_selected)

    with st.expander("##### 4- Strategy: Core Ideology (OPSP)"):
        session_forms.session_four_opsp(email)

    with st.expander("##### 4- Strategy: Core Ideology (SWT)"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Company: :orange[{st.session_state['company_name']}]")
        with col2:
            st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
        st.divider()
        session_forms.session_four_swt_strenght(email, company_id_selected)
        session_forms.session_four_swt_weaknesses(email, company_id_selected)
        session_forms.session_four_swt_trends(email, company_id_selected)


# with st.sidebar:
#         dashboard.check_s1(email)
#         st.divider()
#         dashboard.check_s2(email)
#         st.divider()
#         dashboard.check_s3(email)
#         st.divider()
#         dashboard.check_s4_swot(email)