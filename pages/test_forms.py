import streamlit as st
from pymongo import MongoClient
import components.session_forms as session_forms
import components.dashboard as dashboard
import components.authenticate as authenticate
import components.search as search

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

email = "hpmbala@gmail.com"
company_id_selected = "81281e34-2a87-4a26-a800-16d8e33dadaf"

with st.expander("##### 3- People: Right people in the right place"):
        session_forms.session_three(email, company_id_selected)
        session_forms.session_three_extra(email, company_id_selected)



