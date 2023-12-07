import streamlit as st
import components.session_forms as session_forms
import components.dashboard as dashboard
import components.authenticate as authenticate
import components.search as search

st.set_page_config(
    page_title="Sessions 5-8", 
    page_icon="🆙", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "mailto:hola@neuva.com",
        'About': "# Scale Up!"
    }
    )

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'email_user' not in st.session_state:
    st.session_state['email_user'] = None

email = st.session_state['email_user']

if 'company_id' not in st.session_state:
    st.session_state['company_id'] = None
if 'company_name' not in st.session_state:
    st.session_state['company_name'] = None

# Page start here
if st.session_state["authenticated"]:
    with st.sidebar:
          st.write(f'Ahoj, {st.session_state["user_name"]}!')
          selected_company, company_id = search.set_company_and_id(email)

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
          st.divider()
          authenticate.button_logout()

    company_id_selected = st.session_state['company_id']
    print(company_id_selected)

    with st.expander("##### 9- EXECUTION: Predictable System"):
        session_forms.session_nine_individual_13_week(email)
    # with st.expander("##### 6- CASH: Cash Conversion Cycle"):
    #      session_forms.session_six(email)
    # with st.expander("##### 7- CASH: The Power of Iniciatives"):
    #      session_forms.session_seven_cash(email)
    # with st.expander("##### 8- EXECUTION: Alignment (WWW)"):
    #      session_forms.session_eight(email)
    # with st.expander("##### 8- EXECUTION: Winning Moves"):
    #      session_forms.session_eight_winning_moves(email)
    # with st.expander('##### 8- EXECUTION+: Anual Company Priorities'):
    #      session_forms.session_eight_anual_company_priorities(email)
    # with st.expander('##### 8- EXECUTION+: Quarterly Company Priorities'):
    #      session_forms.session_eight_quarterly_company_priorities(email)
    # with st.expander('##### 8- EXECUTION+: Individual Priorities'):
    #      session_forms.session_eight_priorities_individual(email)
    # with st.expander('##### 8- EXECUTION+: KPI'):
    #      st.text('Falta')
else:
    st.write("# Please Log In")
    # st.write(st.session_state)
    with st.sidebar:
        st.divider()
        authenticate.button_login()