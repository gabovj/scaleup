import streamlit as st
import components.session_forms as session_forms
import components.dashboard as dashboard

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

email = st.session_state['email_user']

with st.expander("##### 5- STRATEGY: Winning Moves"):
     session_forms.session_five(email)
with st.expander("##### 6- CASH: Cash Conversion Cycle"):
     session_forms.session_six(email)
with st.expander("##### 7- CASH: The Power of Iniciatives"):
     session_forms.session_seven_cash(email)
with st.expander("##### 8- EXECUTION: Alignment (WWW)"):
     session_forms.session_eight(email)
with st.expander("##### 8- EXECUTION: Winning Moves"):
     session_forms.session_eight_winning_moves(email)
with st.expander('##### 8- EXECUTION+: Anual Company Priorities'):
     session_forms.session_eight_anual_company_priorities(email)
with st.expander('##### 8- EXECUTION+: Quarterly Company Priorities'):
     session_forms.session_eight_quarterly_company_priorities(email)
with st.expander('##### 8- EXECUTION+: Individual Priorities'):
     session_forms.session_eight_priorities_individual(email)
with st.expander('##### 8- EXECUTION+: KPI'):
     session_forms.session_eight_kpi(email)


# with st.sidebar:
#         dashboard.check_s5(email)
#         st.divider()
#         dashboard.check_s6(email)
#         st.divider()
#         dashboard.check_s8(email)
#         dashboard.check_s8_priority(email)
#         dashboard.check_s8_priority_individual(email)
#         st.divider()
#         dashboard.check_s4_swot(email)