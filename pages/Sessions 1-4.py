import streamlit as st
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

email = st.session_state['email_user']

with st.expander("##### 1- Scaling Up - 4 Decisions"):
    session_forms.session_one(email)

with st.expander("##### 2- People: Life by design"):
    st.markdown('##### :orange[One-Page Personal Plan (OPPP)]')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Spirituality", "Family", "Friends", "Fitness", "Finance"])
    with tab1:
        session_forms.session_two_faith(email)
    with tab2:
        session_forms.session_two_family(email)
    with tab3:
        session_forms.session_two_friends(email)
    with tab4:
        session_forms.session_two_fitness(email)
    with tab5:
        session_forms.session_two_finance(email)

with st.expander("##### 3- People: Right people in the right place"):
     session_forms.session_three(email)

with st.expander("##### 4- Strategy: Core Ideology (OPSP)"):
     session_forms.session_four_opsp(email)

with st.expander("##### 4- Strategy: Core Ideology (SWT)"):
     session_forms.session_four_swt_strenght(email)
     session_forms.session_four_swt_weaknesses(email)
     session_forms.session_four_swt_trends(email)


# with st.sidebar:
#         dashboard.check_s1(email)
#         st.divider()
#         dashboard.check_s2(email)
#         st.divider()
#         dashboard.check_s3(email)
#         st.divider()
#         dashboard.check_s4_swot(email)