import streamlit as st
from pymongo import MongoClient
import time

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]
# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)
# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def get_db_company_info(email):
    company_data = collection.find_one({"email": email})
    # st.markdown(company_data)
    return company_data

def check_s1(email):
    """
    Check if exists s1_rockefeller_habitsin database
    """
    data = get_db_company_info(email)
    progress = calculate_progress_s1(data)
    display_progress_s1(progress)  

def calculate_progress_s1(data):
    rockefeller_data = data.get('s1_rockefeller_habits', {})
    total_fields = 0
    filled_fields = 0
    
    for category, fields in rockefeller_data.items():
        for field, value in fields.items():
            total_fields += 1
            if value:  # If the value is not None or False
                filled_fields += 1
                
    progress = (filled_fields / total_fields) * 100 if total_fields > 0 else 0
    return progress

def display_progress_s1(progress):
    # progress = calculate_progress_s1(data)
    st.write("##### Session 1")
    my_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(int(progress) + 1):
        my_bar.progress(i)
        progress_text.text(f"{i}% complete")
        time.sleep(0.01)  # To create a visible loading animation
    time.sleep(1)  # To pause after completing the progress bar

def check_s2(email):
    """
    Check if s2 exists in database
    """
    data = get_db_company_info(email)
    progress = calculate_progress_s2(data)
    display_overall_progress_s2(progress)
    # st.markdown(progress)

def calculate_progress_s2(data):
    progress = {}
    for main_category, sub_categories in data.items():
        if main_category.startswith('s2_oppp_'):
            total_fields = 0
            filled_fields = 0
            for sub_category, periods in sub_categories.items():
                for period, fields in periods.items():
                    total_fields += 1
                    if fields and fields != "":  # Checks if the value is not null or empty
                        filled_fields += 1
            progress[main_category] = (filled_fields / total_fields) * 100 if total_fields > 0 else 0
    return progress

def display_overall_progress_s2(progress):
    overall_progress = sum(progress.values()) / len(progress)
    st.write("##### Session 2")
    my_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(101):
        my_bar.progress(i)
        progress_text.text(f"{i}% complete")
        time.sleep(0.01)  # To make the progress visible
        if i >= overall_progress:
            break
    time.sleep(1)  # To pause after completing the progress bar

def check_s3(email):
    company_data = get_db_company_info(email)
    count = len(company_data['s3_face'])
    st.write("##### Session 3")
    progress_text = st.empty()
    for i in range (count+1):
        progress_text.write(f"##### {i} FACEs")
        time.sleep(0.2)  # To make the progress visible

def check_s4_swot(email):
    """
    Check if exists s4_swot
    """
    data = get_db_company_info(email)
    progress = calculate_progress_s4_swot(data)
    display_progress_s4_swot(progress)  

def calculate_progress_s4_swot(data):
    swot_data = data.get('s4_swot', {})
    total_fields = 4  # There are four fields in SWOT: strengths, weaknesses, opportunities, threats
    filled_fields = sum(1 for field, value in swot_data.items() if value)  # Count non-empty fields
    
    progress = (filled_fields / total_fields) * 100
    print("SWOT Progress calculated:", progress)  # Debugging line
    return progress

def display_progress_s4_swot(progress):
    st.write("##### Session 4")
    my_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(int(progress) + 1):
        my_bar.progress(i)
        progress_text.text(f"{i}% complete")
        time.sleep(0.01)  # To create a visible loading animation
    time.sleep(1)  # To pause after completing the progress bar

def check_s5(email):
    """
    Check if exists s5
    """
    data = get_db_company_info(email)
    progress = calculate_progress_s5(data)
    display_progress_s5(progress)  

def calculate_progress_s5(data):
    seven_strata_data = data.get('s5_7_strata', {})
    total_fields = 11  # There are four fields in SWOT: strengths, weaknesses, opportunities, threats
    filled_fields = sum(1 for field, value in seven_strata_data.items() if value)  # Count non-empty fields
    
    progress = (filled_fields / total_fields) * 100
    print("7 Strata Progress calculated:", progress)  # Debugging line
    return progress

def display_progress_s5(progress):
    st.write("##### Session 5")
    my_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(int(progress) + 1):
        my_bar.progress(i)
        progress_text.text(f"{i}% complete")
        time.sleep(0.01)  # To create a visible loading animation
    time.sleep(1)  # To pause after completing the progress bar

def check_s6(email):
    company_data = get_db_company_info(email)
    count = len(company_data['s6_cash_0']) + len(company_data['s6_cash_1']) + len(company_data['s6_cash_2']) + len(company_data['s6_cash_3'])
    st.write("##### Session 6")
    progress_text = st.empty()
    for i in range (count+1):
        progress_text.write(f"##### {i} CASh")
        time.sleep(0.2)  # To make the progress visible

def check_s8(email):
    company_data = get_db_company_info(email)
    count = len(company_data['s8_www'])
    st.write("##### Session 8")
    progress_text = st.empty()
    for i in range (count+1):
        progress_text.write(f"##### {i} WWW")
        time.sleep(0.2)  # To make the progress visible

def check_s8_priority(email):
    company_data = get_db_company_info(email)
    count = len(company_data['s8_anual_company_priorities']) + len(company_data['s8_anual_company_priority_smart'])
    st.write("##### Session 8 Company Priorities")
    progress_text = st.empty()
    for i in range (count+1):
        progress_text.write(f"##### {i} Priorities")
        time.sleep(0.2)  # To make the progress visible

def check_s8_priority_individual(email):
    company_data = get_db_company_info(email)
    count = len(company_data['s8_individual_priorities'])
    st.write("##### Session 8 Individual Priorities")
    progress_text = st.empty()
    for i in range (count+1):
        progress_text.write(f"##### {i} Priorities")
        time.sleep(0.2)  # To make the progress visible

def display_dashboard(email):
    company_data= get_db_company_info(email)
    company_name = company_data['company_name']
    st.title(f'Dashboard for {company_name}')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        check_s1(email)
    with col2:
        check_s2(email)
    with col3:
        check_s3(email)
    with col4:
        check_s4_swot(email)
    col1, col2, col3, col4 = st.columns(4)
    with col1:    
        check_s5(email)
    with col2:
        check_s6(email)
    
    with col4:
        check_s8(email)


