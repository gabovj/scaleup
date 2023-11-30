import streamlit as st
import components.authenticate as authenticate
import components.dashboard as dashboard

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

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

authenticate.set_st_state_vars()


# st.text(st.session_state)

# Add login/logout buttons
if st.session_state["authenticated"]:
    email = st.session_state['email_user']
    # dashboard.get_db_company_info(email)
    dashboard.display_dashboard(email)
    
    authenticate.button_logout()
else:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('test_logo.png', width=250)
    st.write("# Scaling up Forms db")
    st.markdown(
        """
        test site
    """
    )
    authenticate.button_login()