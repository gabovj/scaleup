import streamlit as st
from pymongo import MongoClient
import time
from datetime import datetime

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]
# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)
# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def session_one(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    # If existing data is found, use it to pre-fill the form; otherwise, use default values
    prefill_data = existing_data.get("s1_rockefeller_habits", {})
    with st.form(key='s1'):
        st.markdown('##### :orange[Execution: Rockefeller Habits Checklist]')
        st.markdown('**:orange[1.- The executive team is healthy and aligned.]**')
        members_understand_differences = st.checkbox('Team members understand each other‘s differences, priorities, and styles.',
                                                     value=prefill_data.get("ExecutiveTeam", {}).get("members_understand_differences", False))
        meets_frequently = st.checkbox('The team meets frequently (weekly is best) for strategic thinking.',
                                       value=prefill_data.get("ExecutiveTeam", {}).get("meets_frequently", False))
        ongoing_education = st.checkbox('The team participates in ongoing executive education (monthly recommended).',
                                        value=prefill_data.get("ExecutiveTeam", {}).get("ongoing_education", False))
        constructive_debates = st.checkbox('The team is able to engage in constructive debates and all members feel comfortable participating.',
                                           value=prefill_data.get("ExecutiveTeam", {}).get("constructive_debates", False))
        st.markdown('**:orange[2.- Everyone is aligned with the #1 thing that needs to be accomplished this quarter to move the company forward.]**')
        critical_number_identified = st.checkbox('The Critical Number is identified to move the company ahead this quarter.',
                                                 value=prefill_data.get("Alignment", {}).get("critical_number_identified", False))
        priorities_identified = st.checkbox('3-5 Priorities (Rocks) that support the Critical Number are identified and ranked for the quarter.',
                                            value=prefill_data.get("Alignment", {}).get("priorities_identified", False))
        quarterly_theme_announced = st.checkbox('A Quarterly Theme and Celebration/Reward are announced to all employees that bring the Critical Number to life.',
                                                value=prefill_data.get("Alignment", {}).get("quarterly_theme_announced", False))
        theme_posted_everywhere = st.checkbox('Quarterly Theme/Critical Number posted throughout the company and employees are aware of the progress each week.',
                                              value=prefill_data.get("Alignment", {}).get("theme_posted_everywhere", False))
        st.markdown('**:orange[3.- Communication rhythm is established and information moves through organization accurately and quickly.]**')
        daily_huddle = st.checkbox('All employees are in a daily huddle that lasts less than 15 minutes.',
                                   value=prefill_data.get("CommunicationRhythm", {}).get("daily_huddle", False))
        weekly_team_meeting = st.checkbox('All teams have a weekly meeting.',
                                          value=prefill_data.get("CommunicationRhythm", {}).get("weekly_team_meeting", False))
        monthly_exec_meeting = st.checkbox('The executive and middle managers meet for a day of learning, resolving big issues, and DNA transfer each month.',
                                           value=prefill_data.get("CommunicationRhythm", {}).get("monthly_exec_meeting", False))
        quarterly_annual_offsite = st.checkbox('Quarterly and annually, the executive and middle managers meet offsite to work on the 4 Decisions.',
                                               value=prefill_data.get("CommunicationRhythm", {}).get("quarterly_annual_offsite", False))
        st.markdown('**:orange[4.- Every facet of the organization has a person assigned with accountability for ensuring goals are met.]**')
        face_completed = st.checkbox('The Function Accountability Chart (FACe) is completed (right people, doing the right things, right).',
                                     value=prefill_data.get("Accountability", {}).get("face_completed", False))
        financial_statements_person_assigned = st.checkbox('Financial statements have a person assigned to each line item.',
                                                           value=prefill_data.get("Accountability", {}).get("financial_statements_person_assigned", False))
        pace_assigned = st.checkbox('Each of the 4-9 processes on the Process Accountability Chart (PACe) has someone that is accountable for them.',
                                    value=prefill_data.get("Accountability", {}).get("pace_assigned", False))
        key_thrust_capability_assigned = st.checkbox('Each 3-5 year Key Thrust/Capability has a corresponding expert on the Advisory Board if internal expertise doesn’t exist.',
                                                     value=prefill_data.get("Accountability", {}).get("key_thrust_capability_assigned", False))
        st.markdown('**:orange[5.- Ongoing employee input is collected to identify obstacles and opportunities.]**')
        start_stop_keep_conversation = st.checkbox('All executives (and middle managers) have a Start/Stop/Keep conversation with at least one employee weekly.',
                                                   value=prefill_data.get("EmployeeInput", {}).get("start_stop_keep_conversation", False))
        insights_shared_weekly = st.checkbox('The insights from employee conversations are shared at the weekly executive team meeting.',
                                             value=prefill_data.get("EmployeeInput", {}).get("insights_shared_weekly", False))
        employee_input_collected = st.checkbox('Employee input about obstacles and opportunities is being collected weekly.',
                                               value=prefill_data.get("EmployeeInput", {}).get("employee_input_collected", False))
        mid_management_responsible = st.checkbox('A mid-management team is responsible for the process of closing the loop on all obstacles and opportunities.',
                                                 value=prefill_data.get("EmployeeInput", {}).get("mid_management_responsible", False))
        st.markdown('**:orange[6.- Reporting and analysis of customer feedback data is as frequent and accurate as financial data.]**')
        conversation_with_end_user = st.checkbox('All executives (and middle managers) have a 4Q conversation with at least one end user weekly.',
                                                 value=prefill_data.get("CustomerFeedback", {}).get("conversation_with_end_user", False))
        customer_insights_shared = st.checkbox('The insights from customer conversations are shared at the weekly executive team meeting.',
                                               value=prefill_data.get("CustomerFeedback", {}).get("customer_insights_shared", False))
        all_employees_involved = st.checkbox('All employees are involved in collecting customer data.',
                                             value=prefill_data.get("CustomerFeedback", {}).get("all_employees_involved", False))
        mid_management_feedback_responsible = st.checkbox('A mid-management team is responsible for the process of closing the loop on all customer feedback.',
                                                          value=prefill_data.get("CustomerFeedback", {}).get("mid_management_feedback_responsible", False))
        st.markdown('**:orange[7.- Core Values and Purpose are “alive” in the organization.]**')
        known_by_all = st.checkbox('Core Values are discovered, Purpose is articulated, and both are known by all employees.',
                                   value=prefill_data.get("CoreValuesPurpose", {}).get("known_by_all", False))
        refer_back_when_giving_feedback = st.checkbox('All executives and middle managers refer back to the Core Values and Purpose when giving praise or reprimands.',
                                                      value=prefill_data.get("CoreValuesPurpose", {}).get("refer_back_when_giving_feedback", False))
        hr_processes_align = st.checkbox('HR processes and activities align with the Core Values and Purpose (hiring, orientation, appraisal, recognition, etc.).',
                                         value=prefill_data.get("CoreValuesPurpose", {}).get("hr_processes_align", False))
        actions_identified_quarterly = st.checkbox('Actions are identified and implemented each quarter to strengthen the Core Values and Purpose in the organization.',
                                                   value=prefill_data.get("CoreValuesPurpose", {}).get("actions_identified_quarterly", False))
        st.markdown('**:orange[8.- Employees can articulate the following key components of the company’s strategy accurately.]**')
        bhag_progress_visible = st.checkbox('Big Hairy Audacious Goal (BHAG) – Progress is tracked and visible.',
                                            value=prefill_data.get("CompanyStrategy", {}).get("bhag_progress_visible", False))
        core_customer_profile = st.checkbox('Core Customer(s) – Their profile in 25 words or less.',
                                            value=prefill_data.get("CompanyStrategy", {}).get("core_customer_profile", False))
        brand_promises = st.checkbox('3 Brand Promises – And the corresponding Brand Promise KPIs reported on weekly.',
                                     value=prefill_data.get("CompanyStrategy", {}).get("brand_promises", False))
        elevator_pitch = st.checkbox('Elevator Pitch – A compelling response to the question “What does your company do?”',
                                     value=prefill_data.get("CompanyStrategy", {}).get("elevator_pitch", False))
        st.markdown('**:orange[9.- All employees can answer quantitatively whether they had a good day or week (Column 7 of the One-Page Strategic Plan).]**')
        kpis_reported_weekly = st.checkbox('1 or 2 Key Performance Indicators (KPIs) are reported on weekly for each role/person.',
                                           value=prefill_data.get("EmployeePerformance", {}).get("kpis_reported_weekly", False))
        critical_number_aligned = st.checkbox('Each employee has 1 Critical Number that aligns with the company’s Critical Number for the quarter (clear line of sight).',
                                              value=prefill_data.get("EmployeePerformance", {}).get("critical_number_aligned", False))
        quarterly_priorities_aligned = st.checkbox('Each individual/team has 3-5 Quarterly Priorities/Rocks that align with those of the company.',
                                                   value=prefill_data.get("EmployeePerformance", {}).get("quarterly_priorities_aligned", False))
        managers_have_coaches = st.checkbox('All executives and middle managers have a coach (or peer coach) holding them accountable to behavior changes.',
                                            value=prefill_data.get("EmployeePerformance", {}).get("managers_have_coaches", False))
        st.markdown('**:orange[10.- The company’s plans and performance are visible to everyone.]**')
        situation_room_established = st.checkbox('A “situation room” is established for weekly meetings (physical or virtual).',
                                                 value=prefill_data.get("CompanyVisibility", {}).get("situation_room_established", False))
        values_posted_everywhere = st.checkbox('Core Values, Purpose and Priorities are posted throughout the company.',
                                               value=prefill_data.get("CompanyVisibility", {}).get("values_posted_everywhere", False))
        scoreboards_displayed = st.checkbox('Scoreboards are up everywhere displaying current progress on KPIs and Critical Numbers.',
                                            value=prefill_data.get("CompanyVisibility", {}).get("scoreboards_displayed", False))
        system_for_tracking_priorities = st.checkbox('There is a system in place for tracking and managing the cascading Priorities and KPIs.',
                                                     value=prefill_data.get("CompanyVisibility", {}).get("system_for_tracking_priorities", False))
        submitted_s1 = st.form_submit_button(":orange[Save Habits]")
        if submitted_s1:
            try:
                s1_rockefeller_habits = {
                    "s1_rockefeller_habits": {
                        "ExecutiveTeam": {
                            "members_understand_differences": members_understand_differences,
                            "meets_frequently": meets_frequently,
                            "ongoing_education": ongoing_education,
                            "constructive_debates": constructive_debates,
                        },
                        "Alignment": {
                            "critical_number_identified": critical_number_identified,
                            "priorities_identified": priorities_identified,
                            "quarterly_theme_announced": quarterly_theme_announced,
                            "theme_posted_everywhere": theme_posted_everywhere,
                        },
                        "CommunicationRhythm": {
                            "daily_huddle": daily_huddle,
                            "weekly_team_meeting": weekly_team_meeting,
                            "monthly_exec_meeting": monthly_exec_meeting,
                            "quarterly_annual_offsite": quarterly_annual_offsite,
                        },
                        "Accountability": {
                            "face_completed": face_completed,
                            "financial_statements_person_assigned": financial_statements_person_assigned,
                            "pace_assigned": pace_assigned,
                            "key_thrust_capability_assigned": key_thrust_capability_assigned,
                        },
                        "EmployeeInput": {
                            "start_stop_keep_conversation": start_stop_keep_conversation,
                            "insights_shared_weekly": insights_shared_weekly,
                            "employee_input_collected": employee_input_collected,
                            "mid_management_responsible": mid_management_responsible,
                        },
                        "CustomerFeedback": {
                            "conversation_with_end_user": conversation_with_end_user,
                            "customer_insights_shared": customer_insights_shared,
                            "all_employees_involved": all_employees_involved,
                            "mid_management_feedback_responsible": mid_management_feedback_responsible,
                        },
                        "CoreValuesPurpose": {
                            "known_by_all": known_by_all,
                            "refer_back_when_giving_feedback": refer_back_when_giving_feedback,
                            "hr_processes_align": hr_processes_align,
                            "actions_identified_quarterly": actions_identified_quarterly,
                        },
                        "CompanyStrategy": {
                            "bhag_progress_visible": bhag_progress_visible,
                            "core_customer_profile": core_customer_profile,
                            "brand_promises": brand_promises,
                            "elevator_pitch": elevator_pitch,
                        },
                        "EmployeePerformance":{
                            "kpis_reported_weekly": kpis_reported_weekly,
                            "critical_number_aligned" : critical_number_aligned,
                            "quarterly_priorities_aligned": quarterly_priorities_aligned,
                            "managers_have_coaches": managers_have_coaches,
                        },
                        "CompanyVisibility": {
                            "situation_room_established": situation_room_established,
                            "values_posted_everywhere": values_posted_everywhere,
                            "scoreboards_displayed": scoreboards_displayed,
                            "system_for_tracking_priorities": system_for_tracking_priorities,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s1_rockefeller_habits}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Habits saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_faith(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_faith", {}) if existing_data else {}
    with st.form(key='s2_faith'):
        st.markdown('##### :orange[Spirituality 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            faith_relationships_10_25_years = st.text_area("Relationships", key="faith_relationship_10_25",
                                                         placeholder='SPIRITUALITY - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("faith_10_25_years", {}).get("faith_relationships_10_25_years", ""))
        with col2:
            faith_achievements_10_25_years = st.text_area("Achievements", key="faith_achievements_10_25",
                                                        placeholder='SPIRITUALITY - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("faith_10_25_years", {}).get("faith_achievements_10_25_years", ""))
        with col3:
            faith_rituals_10_25_years = st.text_area("Rituals", key="faith_rituals_10_25",
                                                   placeholder='SPIRITUALITY - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("faith_10_25_years", {}).get("faith_rituals_10_25_years", ""))
        with col4:
            faith_wealth_10_25_years = st.text_area("Wealth ($)", key="faith_wealth_10_25",
                                                  placeholder='SPIRITUALITY - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("faith_10_25_years", {}).get("faith_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            faith_relationships_1_year = st.text_area("Relationships", key="faith_relationship_1",
                                                    placeholder='SPIRITUALITY - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("faith_1_year", {}).get("faith_relationships_1_year", ""))
        with col2:
            faith_achievements_1_year = st.text_area("Achievements", key="faith_achievements_1",
                                                   placeholder='SPIRITUALITY - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("faith_1_year", {}).get("faith_achievements_1_year", ""))
        with col3:
            faith_rituals_1_year = st.text_area("Rituals", key="faith_rituals_1",
                                              placeholder='SPIRITUALITY - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("faith_1_year", {}).get("faith_rituals_1_year", ""))
        with col4:
            faith_wealth_1_year = st.text_area("Wealth ($)", key="faith_wealth_1",
                                             placeholder='SPIRITUALITY - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("faith_1_year", {}).get("faith_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            faith_relationships_start_90_days = st.text_area("Relationships", key="faith_relationships_90_start",
                                                           placeholder='SPIRITUALITY - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("faith_90_days", {}).get("faith_relationships_start_90_days", ""))
        with col2:
            faith_achievements_start_90_days = st.text_area("Achievements", key="faith_achievements_90_start",
                                                          placeholder='SPIRITUALITY - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("faith_90_days", {}).get("faith_achievements_start_90_days", ""))
        with col3:
            faith_rituals_start_90_days = st.text_area("Rituals", key="faith_rituals_90_start",
                                                     placeholder='SPIRITUALITY - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("faith_90_days", {}).get("faith_rituals_start_90_days", ""))
        with col4:
            faith_wealth_start_90_days = st.text_area("Wealth ($)", key="faith_wealth_90_start",
                                                    placeholder='SPIRITUALITY - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("faith_90_days", {}).get("faith_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            faith_relationships_stop_90_days = st.text_area("Relationships", key="faith_relationships_90_stop",
                                                          placeholder='SPIRITUALITY - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("faith_90_days", {}).get("faith_relationships_stop_90_days", ""))
        with col2:
            faith_achievements_stop_90_days = st.text_area("Achievements", key="faith_achievements_90_stop",
                                                         placeholder='SPIRITUALITY - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("faith_90_days", {}).get("faith_achievements_stop_90_days", ""))
        with col3:
            faith_rituals_stop_90_days = st.text_area("Rituals", key="faith_rituals_90_stop",
                                                    placeholder='SPIRITUALITY - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("faith_90_days", {}).get("faith_rituals_stop_90_days", ""))
        with col4:
            faith_wealth_stop_90_days = st.text_area("Wealth ($)", key="faith_wealth_90_stop",
                                                   placeholder='SPIRITUALITY - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("faith_90_days", {}).get("faith_wealth_stop_90_days", ""))
        
        submitted_s2_faith = st.form_submit_button(":orange[Save FAITH Info]")
        if submitted_s2_faith:
            try:
                s2_faith = {
                    "s2_oppp_faith": {
                        "faith_90_days": {
                            "faith_relationships_start_90_days": faith_relationships_start_90_days,
                            "faith_relationships_stop_90_days": faith_relationships_stop_90_days,
                            "faith_achievements_start_90_days": faith_achievements_start_90_days,
                            "faith_achievements_stop_90_days": faith_achievements_stop_90_days,
                            "faith_rituals_start_90_days": faith_rituals_start_90_days,
                            "faith_rituals_stop_90_days": faith_rituals_stop_90_days,
                            "faith_wealth_start_90_days": faith_wealth_start_90_days,
                            "faith_wealth_stop_90_days": faith_wealth_stop_90_days,
                        },
                        "faith_1_year": {
                            "faith_relationships_1_year": faith_relationships_1_year,
                            "faith_achievements_1_year": faith_achievements_1_year,
                            "faith_rituals_1_year": faith_rituals_1_year,
                            "faith_wealth_1_year": faith_wealth_1_year,
                        },
                        "faith_10_25_years": {
                            "faith_relationships_10_25_years": faith_relationships_10_25_years,
                            "faith_achievements_10_25_years": faith_achievements_10_25_years,
                            "faith_rituals_10_25_years": faith_rituals_10_25_years,
                            "faith_wealth_10_25_years": faith_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_faith}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FAITH info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_family(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_family", {}) if existing_data else {}
    with st.form(key='s2_family'):
        st.markdown('##### :orange[Family 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            family_relationships_10_25_years = st.text_area("Relationships", key="family_relationship_10_25",
                                                         placeholder='FAMILY - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("family_10_25_years", {}).get("family_relationships_10_25_years", ""))
        with col2:
            family_achievements_10_25_years = st.text_area("Achievements", key="family_achievements_10_25",
                                                        placeholder='FAMILY - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("family_10_25_years", {}).get("family_achievements_10_25_years", ""))
        with col3:
            family_rituals_10_25_years = st.text_area("Rituals", key="family_rituals_10_25",
                                                   placeholder='FAMILY - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("family_10_25_years", {}).get("family_rituals_10_25_years", ""))
        with col4:
            family_wealth_10_25_years = st.text_area("Wealth ($)", key="family_wealth_10_25",
                                                  placeholder='FAMILY - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("family_10_25_years", {}).get("family_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Family 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            family_relationships_1_year = st.text_area("Relationships", key="family_relationship_1",
                                                    placeholder='FAMILY - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("family_1_year", {}).get("family_relationships_1_year", ""))
        with col2:
            family_achievements_1_year = st.text_area("Achievements", key="family_achievements_1",
                                                   placeholder='FAMILY - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("family_1_year", {}).get("family_achievements_1_year", ""))
        with col3:
            family_rituals_1_year = st.text_area("Rituals", key="family_rituals_1",
                                              placeholder='FAMILY - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("family_1_year", {}).get("family_rituals_1_year", ""))
        with col4:
            family_wealth_1_year = st.text_area("Wealth ($)", key="family_wealth_1",
                                             placeholder='FAMILY - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("family_1_year", {}).get("family_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Family 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            family_relationships_start_90_days = st.text_area("Relationships", key="family_relationships_90_start",
                                                           placeholder='FAMILY - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("family_90_days", {}).get("family_relationships_start_90_days", ""))
        with col2:
            family_achievements_start_90_days = st.text_area("Achievements", key="family_achievements_90_start",
                                                          placeholder='FAMILY - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("family_90_days", {}).get("family_achievements_start_90_days", ""))
        with col3:
            family_rituals_start_90_days = st.text_area("Rituals", key="family_rituals_90_start",
                                                     placeholder='FAMILY - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("family_90_days", {}).get("family_rituals_start_90_days", ""))
        with col4:
            family_wealth_start_90_days = st.text_area("Wealth ($)", key="family_wealth_90_start",
                                                    placeholder='FAMILY - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("family_90_days", {}).get("family_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Family 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            family_relationships_stop_90_days = st.text_area("Relationships", key="family_relationships_90_stop",
                                                          placeholder='FAMILY - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("family_90_days", {}).get("family_relationships_stop_90_days", ""))
        with col2:
            family_achievements_stop_90_days = st.text_area("Achievements", key="family_achievements_90_stop",
                                                         placeholder='FAMILY - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("family_90_days", {}).get("family_achievements_stop_90_days", ""))
        with col3:
            family_rituals_stop_90_days = st.text_area("Rituals", key="family_rituals_90_stop",
                                                    placeholder='FAMILY - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("family_90_days", {}).get("family_rituals_stop_90_days", ""))
        with col4:
            family_wealth_stop_90_days = st.text_area("Wealth ($)", key="family_wealth_90_stop",
                                                   placeholder='FAMILY - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("family_90_days", {}).get("family_wealth_stop_90_days", ""))
        submitted_s2_family = st.form_submit_button(":orange[Save FAMILY Info]")
        if submitted_s2_family:
            try:
                s2_family = {
                    "s2_oppp_family": {
                        "family_90_days": {
                            "family_relationships_start_90_days": family_relationships_start_90_days,
                            "family_relationships_stop_90_days": family_relationships_stop_90_days,
                            "family_achievements_start_90_days": family_achievements_start_90_days,
                            "family_achievements_stop_90_days": family_achievements_stop_90_days,
                            "family_rituals_start_90_days": family_rituals_start_90_days,
                            "family_rituals_stop_90_days": family_rituals_stop_90_days,
                            "family_wealth_start_90_days": family_wealth_start_90_days,
                            "family_wealth_stop_90_days": family_wealth_stop_90_days,
                        },
                        "family_1_year": {
                            "family_relationships_1_year": family_relationships_1_year,
                            "family_achievements_1_year": family_achievements_1_year,
                            "family_rituals_1_year": family_rituals_1_year,
                            "family_wealth_1_year": family_wealth_1_year,
                        },
                        "family_10_25_years": {
                            "family_relationships_10_25_years": family_relationships_10_25_years,
                            "family_achievements_10_25_years": family_achievements_10_25_years,
                            "family_rituals_10_25_years": family_rituals_10_25_years,
                            "family_wealth_10_25_years": family_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_family}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FAMILY info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_friends(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_friends", {}) if existing_data else {}
    with st.form(key='s2_friends'):
        st.markdown('##### :orange[Friends 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            friends_relationships_10_25_years = st.text_area("Relationships", key="friends_relationship_10_25",
                                                         placeholder='FRIENDS - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("friends_10_25_years", {}).get("friends_relationships_10_25_years", ""))
        with col2:
            friends_achievements_10_25_years = st.text_area("Achievements", key="friends_achievements_10_25",
                                                        placeholder='FRIENDS - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("friends_10_25_years", {}).get("friends_achievements_10_25_years", ""))
        with col3:
            friends_rituals_10_25_years = st.text_area("Rituals", key="friends_rituals_10_25",
                                                   placeholder='FRIENDS - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("friends_10_25_years", {}).get("friends_rituals_10_25_years", ""))
        with col4:
            friends_wealth_10_25_years = st.text_area("Wealth ($)", key="friends_wealth_10_25",
                                                  placeholder='FRIENDS - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("friends_10_25_years", {}).get("friends_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Friends 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            friends_relationships_1_year = st.text_area("Relationships", key="friends_relationship_1",
                                                    placeholder='FRIENDS - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("friends_1_year", {}).get("friends_relationships_1_year", ""))
        with col2:
            friends_achievements_1_year = st.text_area("Achievements", key="friends_achievements_1",
                                                   placeholder='FRIENDS - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("friends_1_year", {}).get("friends_achievements_1_year", ""))
        with col3:
            friends_rituals_1_year = st.text_area("Rituals", key="friends_rituals_1",
                                              placeholder='FRIENDS - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("friends_1_year", {}).get("friends_rituals_1_year", ""))
        with col4:
            friends_wealth_1_year = st.text_area("Wealth ($)", key="friends_wealth_1",
                                             placeholder='FRIENDS - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("friends_1_year", {}).get("friends_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Friends 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            friends_relationships_start_90_days = st.text_area("Relationships", key="friends_relationships_90_start",
                                                           placeholder='FRIENDS - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("friends_90_days", {}).get("friends_relationships_start_90_days", ""))
        with col2:
            friends_achievements_start_90_days = st.text_area("Achievements", key="friends_achievements_90_start",
                                                          placeholder='FRIENDS - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("friends_90_days", {}).get("friends_achievements_start_90_days", ""))
        with col3:
            friends_rituals_start_90_days = st.text_area("Rituals", key="friends_rituals_90_start",
                                                     placeholder='FRIENDS - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("friends_90_days", {}).get("friends_rituals_start_90_days", ""))
        with col4:
            friends_wealth_start_90_days = st.text_area("Wealth ($)", key="friends_wealth_90_start",
                                                    placeholder='FRIENDS - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("friends_90_days", {}).get("friends_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Friends 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            friends_relationships_stop_90_days = st.text_area("Relationships", key="friends_relationships_90_stop",
                                                          placeholder='FRIENDS - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("friends_90_days", {}).get("friends_relationships_stop_90_days", ""))
        with col2:
            friends_achievements_stop_90_days = st.text_area("Achievements", key="friends_achievements_90_stop",
                                                         placeholder='FRIENDS - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("friends_90_days", {}).get("friends_achievements_stop_90_days", ""))
        with col3:
            friends_rituals_stop_90_days = st.text_area("Rituals", key="friends_rituals_90_stop",
                                                    placeholder='FRIENDS - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("friends_90_days", {}).get("friends_rituals_stop_90_days", ""))
        with col4:
            friends_wealth_stop_90_days = st.text_area("Wealth ($)", key="friends_wealth_90_stop",
                                                   placeholder='FRIENDS - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("friends_90_days", {}).get("friends_wealth_stop_90_days", ""))
        submitted_s2_friends = st.form_submit_button(":orange[Save FRIENDS Info]")
        if submitted_s2_friends:
            try:
                s2_friends = {
                    "s2_oppp_friends": {
                        "friends_90_days": {
                            "friends_relationships_start_90_days": friends_relationships_start_90_days,
                            "friends_relationships_stop_90_days": friends_relationships_stop_90_days,
                            "friends_achievements_start_90_days": friends_achievements_start_90_days,
                            "friends_achievements_stop_90_days": friends_achievements_stop_90_days,
                            "friends_rituals_start_90_days": friends_rituals_start_90_days,
                            "friends_rituals_stop_90_days": friends_rituals_stop_90_days,
                            "friends_wealth_start_90_days": friends_wealth_start_90_days,
                            "friends_wealth_stop_90_days": friends_wealth_stop_90_days,
                        },
                        "friends_1_year": {
                            "friends_relationships_1_year": friends_relationships_1_year,
                            "friends_achievements_1_year": friends_achievements_1_year,
                            "friends_rituals_1_year": friends_rituals_1_year,
                            "friends_wealth_1_year": friends_wealth_1_year,
                        },
                        "friends_10_25_years": {
                            "friends_relationships_10_25_years": friends_relationships_10_25_years,
                            "friends_achievements_10_25_years": friends_achievements_10_25_years,
                            "friends_rituals_10_25_years": friends_rituals_10_25_years,
                            "friends_wealth_10_25_years": friends_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_friends}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FRIENDS info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_fitness(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_fitness", {}) if existing_data else {}
    with st.form(key='s2_fitness'):
        st.markdown('##### :orange[Fitness 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            fitness_relationships_10_25_years = st.text_area("Relationships", key="fitness_relationship_10_25",
                                                         placeholder='FITNESS - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("fitness_10_25_years", {}).get("fitness_relationships_10_25_years", ""))
        with col2:
            fitness_achievements_10_25_years = st.text_area("Achievements", key="fitness_achievements_10_25",
                                                        placeholder='FITNESS - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("fitness_10_25_years", {}).get("fitness_achievements_10_25_years", ""))
        with col3:
            fitness_rituals_10_25_years = st.text_area("Rituals", key="fitness_rituals_10_25",
                                                   placeholder='FITNESS - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("fitness_10_25_years", {}).get("fitness_rituals_10_25_years", ""))
        with col4:
            fitness_wealth_10_25_years = st.text_area("Wealth ($)", key="fitness_wealth_10_25",
                                                  placeholder='FITNESS - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("fitness_10_25_years", {}).get("fitness_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Fitness 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fitness_relationships_1_year = st.text_area("Relationships", key="fitness_relationship_1",
                                                    placeholder='FITNESS - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("fitness_1_year", {}).get("fitness_relationships_1_year", ""))
        with col2:
            fitness_achievements_1_year = st.text_area("Achievements", key="fitness_achievements_1",
                                                   placeholder='FITNESS - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("fitness_1_year", {}).get("fitness_achievements_1_year", ""))
        with col3:
            fitness_rituals_1_year = st.text_area("Rituals", key="fitness_rituals_1",
                                              placeholder='FITNESS - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("fitness_1_year", {}).get("fitness_rituals_1_year", ""))
        with col4:
            fitness_wealth_1_year = st.text_area("Wealth ($)", key="fitness_wealth_1",
                                             placeholder='FITNESS - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("fitness_1_year", {}).get("fitness_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Fitness 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fitness_relationships_start_90_days = st.text_area("Relationships", key="fitness_relationships_90_start",
                                                           placeholder='FITNESS - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("fitness_90_days", {}).get("fitness_relationships_start_90_days", ""))
        with col2:
            fitness_achievements_start_90_days = st.text_area("Achievements", key="fitness_achievements_90_start",
                                                          placeholder='FITNESS - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("fitness_90_days", {}).get("fitness_achievements_start_90_days", ""))
        with col3:
            fitness_rituals_start_90_days = st.text_area("Rituals", key="fitness_rituals_90_start",
                                                     placeholder='FITNESS - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("fitness_90_days", {}).get("fitness_rituals_start_90_days", ""))
        with col4:
            fitness_wealth_start_90_days = st.text_area("Wealth ($)", key="fitness_wealth_90_start",
                                                    placeholder='FITNESS - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("fitness_90_days", {}).get("fitness_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Fitness 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fitness_relationships_stop_90_days = st.text_area("Relationships", key="fitness_relationships_90_stop",
                                                          placeholder='FITNESS - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("fitness_90_days", {}).get("fitness_relationships_stop_90_days", ""))
        with col2:
            fitness_achievements_stop_90_days = st.text_area("Achievements", key="fitness_achievements_90_stop",
                                                         placeholder='FITNESS - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("fitness_90_days", {}).get("fitness_achievements_stop_90_days", ""))
        with col3:
            fitness_rituals_stop_90_days = st.text_area("Rituals", key="fitness_rituals_90_stop",
                                                    placeholder='FITNESS - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("fitness_90_days", {}).get("fitness_rituals_stop_90_days", ""))
        with col4:
            fitness_wealth_stop_90_days = st.text_area("Wealth ($)", key="fitness_wealth_90_stop",
                                                   placeholder='FITNESS - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("fitness_90_days", {}).get("fitness_wealth_stop_90_days", ""))
        submitted_s2_fitness = st.form_submit_button(":orange[Save FITNESS Info]")
        if submitted_s2_fitness:
            try:
                s2_fitness = {
                    "s2_oppp_fitness": {
                        "fitness_90_days": {
                            "fitness_relationships_start_90_days": fitness_relationships_start_90_days,
                            "fitness_relationships_stop_90_days": fitness_relationships_stop_90_days,
                            "fitness_achievements_start_90_days": fitness_achievements_start_90_days,
                            "fitness_achievements_stop_90_days": fitness_achievements_stop_90_days,
                            "fitness_rituals_start_90_days": fitness_rituals_start_90_days,
                            "fitness_rituals_stop_90_days": fitness_rituals_stop_90_days,
                            "fitness_wealth_start_90_days": fitness_wealth_start_90_days,
                            "fitness_wealth_stop_90_days": fitness_wealth_stop_90_days,
                        },
                        "fitness_1_year": {
                            "fitness_relationships_1_year": fitness_relationships_1_year,
                            "fitness_achievements_1_year": fitness_achievements_1_year,
                            "fitness_rituals_1_year": fitness_rituals_1_year,
                            "fitness_wealth_1_year": fitness_wealth_1_year,
                        },
                        "fitness_10_25_years": {
                            "fitness_relationships_10_25_years": fitness_relationships_10_25_years,
                            "fitness_achievements_10_25_years": fitness_achievements_10_25_years,
                            "fitness_rituals_10_25_years": fitness_rituals_10_25_years,
                            "fitness_wealth_10_25_years": fitness_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_fitness}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FITNESS info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_finance(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_finance", {}) if existing_data else {}
    with st.form(key='s2_finance'):
        st.markdown('##### :orange[Finance 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            finance_relationships_10_25_years = st.text_area("Relationships", key="finance_relationship_10_25",
                                                         placeholder='FINANCE - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("finance_10_25_years", {}).get("finance_relationships_10_25_years", ""))
        with col2:
            finance_achievements_10_25_years = st.text_area("Achievements", key="finance_achievements_10_25",
                                                        placeholder='FINANCE - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("finance_10_25_years", {}).get("finance_achievements_10_25_years", ""))
        with col3:
            finance_rituals_10_25_years = st.text_area("Rituals", key="finance_rituals_10_25",
                                                   placeholder='FINANCE - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("finance_10_25_years", {}).get("finance_rituals_10_25_years", ""))
        with col4:
            finance_wealth_10_25_years = st.text_area("Wealth ($)", key="finance_wealth_10_25",
                                                  placeholder='FINANCE - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("finance_10_25_years", {}).get("finance_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Finance 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            finance_relationships_1_year = st.text_area("Relationships", key="finance_relationship_1",
                                                    placeholder='FINANCE - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("finance_1_year", {}).get("finance_relationships_1_year", ""))
        with col2:
            finance_achievements_1_year = st.text_area("Achievements", key="finance_achievements_1",
                                                   placeholder='FINANCE - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("finance_1_year", {}).get("finance_achievements_1_year", ""))
        with col3:
            finance_rituals_1_year = st.text_area("Rituals", key="finance_rituals_1",
                                              placeholder='FINANCE - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("finance_1_year", {}).get("finance_rituals_1_year", ""))
        with col4:
            finance_wealth_1_year = st.text_area("Wealth ($)", key="finance_wealth_1",
                                             placeholder='FINANCE - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("finance_1_year", {}).get("finance_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Finance 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            finance_relationships_start_90_days = st.text_area("Relationships", key="finance_relationships_90_start",
                                                           placeholder='FINANCE - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("finance_90_days", {}).get("finance_relationships_start_90_days", ""))
        with col2:
            finance_achievements_start_90_days = st.text_area("Achievements", key="finance_achievements_90_start",
                                                          placeholder='FINANCE - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("finance_90_days", {}).get("finance_achievements_start_90_days", ""))
        with col3:
            finance_rituals_start_90_days = st.text_area("Rituals", key="finance_rituals_90_start",
                                                     placeholder='FINANCE - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("finance_90_days", {}).get("finance_rituals_start_90_days", ""))
        with col4:
            finance_wealth_start_90_days = st.text_area("Wealth ($)", key="finance_wealth_90_start",
                                                    placeholder='FINANCE - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("finance_90_days", {}).get("finance_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Finance 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            finance_relationships_stop_90_days = st.text_area("Relationships", key="finance_relationships_90_stop",
                                                          placeholder='FINANCE - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("finance_90_days", {}).get("finance_relationships_stop_90_days", ""))
        with col2:
            finance_achievements_stop_90_days = st.text_area("Achievements", key="finance_achievements_90_stop",
                                                         placeholder='FINANCE - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("finance_90_days", {}).get("finance_achievements_stop_90_days", ""))
        with col3:
            finance_rituals_stop_90_days = st.text_area("Rituals", key="finance_rituals_90_stop",
                                                    placeholder='FINANCE - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("finance_90_days", {}).get("finance_rituals_stop_90_days", ""))
        with col4:
            finance_wealth_stop_90_days = st.text_area("Wealth ($)", key="finance_wealth_90_stop",
                                                   placeholder='FINANCE - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("finance_90_days", {}).get("finance_wealth_stop_90_days", ""))
        submitted_s2_finance = st.form_submit_button(":orange[Save FINANCE Info]")
        if submitted_s2_finance:
            try:
                s2_finance = {
                    "s2_oppp_finance": {
                        "finance_90_days": {
                            "finance_relationships_start_90_days": finance_relationships_start_90_days,
                            "finance_relationships_stop_90_days": finance_relationships_stop_90_days,
                            "finance_achievements_start_90_days": finance_achievements_start_90_days,
                            "finance_achievements_stop_90_days": finance_achievements_stop_90_days,
                            "finance_rituals_start_90_days": finance_rituals_start_90_days,
                            "finance_rituals_stop_90_days": finance_rituals_stop_90_days,
                            "finance_wealth_start_90_days": finance_wealth_start_90_days,
                            "finance_wealth_stop_90_days": finance_wealth_stop_90_days,
                        },
                        "finance_1_year": {
                            "finance_relationships_1_year": finance_relationships_1_year,
                            "finance_achievements_1_year": finance_achievements_1_year,
                            "finance_rituals_1_year": finance_rituals_1_year,
                            "finance_wealth_1_year": finance_wealth_1_year,
                        },
                        "finance_10_25_years": {
                            "finance_relationships_10_25_years": finance_relationships_10_25_years,
                            "finance_achievements_10_25_years": finance_achievements_10_25_years,
                            "finance_rituals_10_25_years": finance_rituals_10_25_years,
                            "finance_wealth_10_25_years": finance_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_finance}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FINANCE info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_three(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    show_face(email)
    
    with st.form(key='s3'):
        st.markdown('##### :orange[People: Function Accountability Chart (FACe)]')
        col1, col2 = st.columns(2)
        with col1:
            function_name = st.text_input('Function')
        with col2:
            person_accountable = st.text_input('Person Accountable')
        leading_indicators = st.text_area('Leading Indicators')
        results_outcomes = st.text_area('Results / Outcomes')
        
        submitted_s3 = st.form_submit_button(":orange[Save People Functions]")
        if submitted_s3:
            try:
                face_item ={
                    "s3_face": {
                        "function_name": function_name,
                        "person_accountable": person_accountable,
                        "leading_indicators": leading_indicators,
                        "results_outcomes": results_outcomes,
                    } 
                }
            # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $push operator to add
                update_doc = {"$push": face_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("FACe saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_face(email):
    
    company_data = collection.find_one({"email": email})
    if company_data:
        face_data = company_data.get("s3_face", [])
        name_db = company_data.get("company_name", "Unknown Company")
        for index, face in enumerate(face_data, start=1):
            # Use columns to layout face details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the face details
                st.markdown(f"**:orange[FACE {index}:]** {face.get('function_name', 'N/A')} :orange[/] Person Accountable: {face.get('person_accountable', 'N/A')}")
                # st.divider()
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{face['function_name']}_{face['person_accountable']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_face(email, face)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_face(email, face_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {"s3_face": face_item}}
        )
        st.success("FACe deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_opsp(email):
    st.markdown('##### One-Page Strategic Plan (OPSP)')
    st.text('Falta')

def session_four_swt_strenght(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Strenghts]')
    show_strengths(email)
    with st.form(key='s4_SWT_strenghts'):    
        col1, col2 = st.columns(2)
        with col1:
            st.write("1.- What are your Business Strengths?")
            strenght = st.text_input('Wtrite strength')
        with col2:
            st.write('')  
        submitted_s4_swt_strenght = st.form_submit_button(":orange[Add Strenght]")
        if submitted_s4_swt_strenght:
            try:
                strenght_item ={
                    "s4_strenghts": {
                        "strenght": strenght,
                    } 
                }
            # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $push operator to add
                update_doc = {"$push": strenght_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Strenght saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_strengths(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        strenght_data = company_data.get("s4_strenghts", [])
        name_db = company_data.get("company_name", "Unknown Company")
        for index, strenght in enumerate(strenght_data, start=1):
            # Use columns to layout strenght details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the strenght details
                st.markdown(f"**:orange[{index}-]** {strenght.get('strenght', 'N/A')}")
                # st.divider()
                
            with col2:
                # Construct a unique key for the button based on the strenght details
                button_key = f"delete_{strenght['strenght']}_{index}"
                # Display the delete button next to the strenght details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_strenght(email, strenght)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_strenght(email, strenght_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {"s4_strenghts": strenght_item}}
        )
        st.success("Strenght deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_swt_weaknesses(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Weaknesses]')
    show_weaknesses(email)
    with st.form(key='s4_SWT_Weaknesses'):    
        col1, col2 = st.columns(2)
        with col1:
            st.write("1.- What are your Business Weaknesses?")
            weakness = st.text_input('Wtrite weakness')
        with col2:
            st.write('')  
        submitted_s4_swt_weakness = st.form_submit_button(":orange[Add Weakness]")
        if submitted_s4_swt_weakness:
            try:
                weakness_item ={
                    "s4_weaknesses": {
                        "weakness": weakness,
                    } 
                }
            # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $push operator to add
                update_doc = {"$push": weakness_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Weakness saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_weaknesses(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        weakness_data = company_data.get("s4_weaknesses", [])
        name_db = company_data.get("company_name", "Unknown Company")
        for index, weakness in enumerate(weakness_data, start=1):
            # Use columns to layout strenght details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the strenght details
                st.markdown(f"**:orange[{index}-]** {weakness.get('weakness', 'N/A')}")
                # st.divider()
                
            with col2:
                # Construct a unique key for the button based on the strenght details
                button_key = f"delete_{weakness['weakness']}_{index}"
                # Display the delete button next to the strenght details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_weakness(email, weakness)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No weaknesses data saved for {email}.")

def delete_weakness(email, weakness_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {"s4_weaknesses": weakness_item}}
        )
        st.success("Weakness deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_swt_trends(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Trends]')
    show_trends(email)
    with st.form(key='s4_SWT_Trends'):
        st.write("3.- What are your Business Trends?")    
        col1, col2, col3 = st.columns([1.6,.7,.7])
        with col1:
            trend = st.text_input('Wtrite trend')
        with col2:
            trend_type = st.selectbox('Select trend type', ('Opportunity', 'Threat'), index=None)  
        with col3:
            action_trend = st.selectbox('Select action', ('Mitigate', 'Take Advantage'), index=None)
        submitted_s4_swt_trend = st.form_submit_button(":orange[Add Trend]")
        if submitted_s4_swt_trend:
            try:
                trend_item ={
                    "s4_trends": {
                        "trend": trend,
                        "trend_type": trend_type,
                        "action_trend": action_trend,
                    } 
                }
            # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $push operator to add
                update_doc = {"$push": trend_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Trend saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_trends(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        trend_data = company_data.get("s4_trends", [])
        name_db = company_data.get("company_name", "Unknown Company")
        for index, trend in enumerate(trend_data, start=1):
            # Use columns to layout strenght details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the strenght details
                st.markdown(f"**:orange[{index}-]** {trend.get('trend', 'N/A')} :orange[/] {trend.get('trend_type', 'N/A')} ")
                # st.divider()
                
            with col2:
                # Construct a unique key for the button based on the strenght details
                button_key = f"delete_{trend['trend']}_{index}"
                # Display the delete button next to the strenght details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_trend(email, trend)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No weaknesses data saved for {email}.")

def delete_trend(email, trend_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {"s4_trends": trend_item}}
        )
        st.success("Trend deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_five(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    # If existing data is found, use it to pre-fill the form; otherwise, use default values
    prefill_data = existing_data.get("s5_7_strata", {})
    with st.form(key='s5'):
        st.markdown('##### :orange[7 Strata]')
        mindshare = st.text_area('Words You Own (Midshare):',
                                 value=prefill_data.get("mindshare", ""))
        st.markdown('**:orange[Sandbox and Brand Promises]**')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            core_customers = st.text_area('Who / Where', help='Core Customers',
                                 value=prefill_data.get("core_customers", ""))
        with col2:
            products_and_services = st.text_area('What', help='Products and Services',
                                 value=prefill_data.get("products_and_services", ""))
        with col3:
            brand_promises_7_strata = st.text_area('Brand Promises', help='brand_promises',
                                 value=prefill_data.get("brand_promises_7_strata", ""))
        with col4:
            kpis = st.text_area('KPIs', help='KPIs',
                                 value=prefill_data.get("kpis", ""))
        catalytic_mechanism = st.text_area('Brand Promise Guarantee (Catalytic Mechanism):',
                                 value=prefill_data.get("catalytic_mechanism", ""))
        key_to_making_money = st.text_area('One-PHRASE Strategy (Key to Making Money):',
                                 value=prefill_data.get("key_to_making_money", ""))
        differentiating_activities = st.text_area('Differentiating Activities (3-5 Hows):',
                                 value=prefill_data.get("differentiating_activities", ""))
        x_factor = st.text_area('X-Factor (10x - 100x Underlying Advantage):',
                                 value=prefill_data.get("x_factor", ""))
        col1, col2 = st.columns(2)
        with col1:
            profit_per_x = st.text_area('Profit per X (Economic Engine):',
                                 value=prefill_data.get("profit_per_x", ""))
        with col2:
            bhag = st.text_area('BHAG* (10 - 25 Year Goal):',
                                 value=prefill_data.get("bhag", ""))
        submitted_s5 = st.form_submit_button(":orange[Save 7 Strata]")
        if submitted_s5:
            try:
                s5_7_strata = {
                    "s5_7_strata": {
                        "mindshare": mindshare,
                        "core_customers": core_customers,
                        "products_and_services": products_and_services,
                        "brand_promises_7_strata": brand_promises_7_strata,
                        "kpis": kpis,
                        "catalytic_mechanism": catalytic_mechanism,
                        "key_to_making_money": key_to_making_money,
                        "differentiating_activities": differentiating_activities,
                        "x_factor":x_factor,
                        "profit_per_x": profit_per_x,
                        "bhag": bhag,
                    }
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s5_7_strata}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("7 Strata saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_six(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    # If existing data is found, use it to pre-fill the form; otherwise, use default values
    prefill_data = existing_data.get("s6_cash", {})
    st.markdown('##### :orange[Cash Acceleration Strategies (CASh)]')
    st.divider()
    titles = ['A) Ways to improve your Sales Cycle', 
              'B) Ways to improve your Make/Production & Inventory Cycle',
              'C) Ways to improve your Delivery Cycle',
              'D) Ways to improve your Billing & Payment Cycle',
              ]
    cash_ = [None] * len(titles)
    select_cash_ = [None] * len(titles)

    for index, t in enumerate(titles):
        show_cash(email, array_name= f's6_cash_{index}', input_1=f'cash_{index}', input_2=f'select_cash_{index}')
        with st.form(key=f's6_cash_{index}'):
            
            col1, col2 = st.columns(2)
            with col1:
                cash_[index] = st.text_input(f'{t}')
            with col2:
                select_cash_[index] = st.selectbox("Nivel:", ("Shorten Cycle Times", "Eliminate Mistakes", "Improve Business Model & P/L"), index=None)
            submitted_s6 = st.form_submit_button(":orange[Add]")
            if submitted_s6:
                try:
                    cash_item ={
                        f"s6_cash_{index}": {
                            f"cash_{index}": cash_[index],
                            f"select_cash_{index}": select_cash_[index],
                        } 
                    }
                    # Filter for the document to update
                    filter_doc = {"email": email}
                    # Use the $set operator to update the desired fields
                    update_doc = {"$push": cash_item}
                    # Use upsert=True to insert a new document if no matching document is found
                    collection.update_one(filter_doc, update_doc, upsert=True)
                    # collection.insert_one(perfil)
                    st.success("Data saved!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        st.divider()
    
def show_cash(email, array_name, input_1, input_2):
    
    company_data = collection.find_one({"email": email})
    if company_data:
        cash_data = company_data.get(array_name, [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, cash in enumerate(cash_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the cash details
                st.markdown(f":orange[{index}-] {cash.get(input_1, 'N/A')} :orange[/] {cash.get(input_2, 'N/A')}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{cash[input_1]}_{cash[input_2]}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_cash(email, array_name, cash)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_cash(email, array_name, cash_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {array_name: cash_item}}
        )
        st.success("FACe deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_seven_cash(email):
    st.text('Falta')

def session_eight(email):
    st.markdown('##### :orange[Who • What • When (WWW)]')
    show_www(email)
    with st.form(key=f's8_www'):      
        col1, col2, col3 = st.columns(3)
        with col1:
            who = st.text_input('Who')
        with col2:
            what = st.text_input('What')
        with col3:
            when = st.text_input('When')
        submitted_s8_www = st.form_submit_button(":orange[Add WWW]")
        if submitted_s8_www:
            try:
                www_item ={
                    "s8_www": {
                        "who": who,
                        "what": what,
                        "when": when,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": www_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("WWW saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
def show_www(email):
    
    company_data = collection.find_one({"email": email})
    if company_data:
        www_data = company_data.get('s8_www', [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, www in enumerate(www_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the cash details
                st.markdown(f":orange[{index}-] {www.get('who', 'N/A')} :orange[/] {www.get('what', 'N/A')} :orange[/] {www.get('when', 'N/A')}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{www['who']}_{www['what']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_www(email, www)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No WWW data saved for {email}.")

def delete_www(email, www_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {'s8_www': www_item}}
        )
        st.success("WWW deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_winning_moves(email):
    st.write('Falta')

def session_eight_anual_company_priorities(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    # If existing data is found, use it to pre-fill the form; otherwise, use default values
    prefill_data = existing_data.get("s8_anual_company_priority_smart", {})
    st.markdown('##### :orange[Anual Company Priorities]')
    show_anual_priority(email)
    with st.form(key='s8_anual_priorities'):
        anual_company_priority = st.text_area('Anual Company Priority')
        col1, col2 = st.columns(2)
        with col1:
            owner = st.text_input('Owner')
        with col2:
            success_criteria = st.selectbox('Success Criteria', ('Will happen', 'At risk - need help', 'Will not happen'), index=None)
        submitted_s8_anual_priority = st.form_submit_button(":orange[Add anual priority]")
        if submitted_s8_anual_priority:
            try:
                priority_item ={
                    "s8_anual_company_priorities": {
                        "company_priority": anual_company_priority,
                        "owner": owner,
                        "success_criteria": success_criteria,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Company Priority saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

    with st.form(key='s8_anual_priority_smart'):
        anual_company_priority_smart = st.text_area("What's one specific thing we can do as an organization to improve next period based on last period's Priorities?",
                                              placeholder="Refine and rewrite your idea as a S.M.A.R.T. priority",
                                              value=prefill_data.get("anual_company_priority_smart", ""))
        
        submitted_s8_anual_priority_smart = st.form_submit_button(":orange[Add SMART quarterly priority]")
        if submitted_s8_anual_priority_smart:
            try:
                priority_smart_item ={
                    "s8_anual_company_priority_smart": {
                        "anual_company_priority_smart": anual_company_priority_smart,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$set": priority_smart_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("SMART Company Priority saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_anual_priority(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        priorities_data = company_data.get('s8_anual_company_priorities', [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, priority in enumerate(priorities_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the cash details
                st.markdown(f":orange[{index}-] {priority.get('company_priority', 'N/A')} :orange[/] {priority.get('owner', 'N/A')} :orange[/] {priority.get('success_criteria', 'N/A')}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{priority['company_priority']}_{priority['owner']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_anual_priority(email, priority)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No anual priorities saved for {email}.")

def delete_anual_priority(email, priority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {'s8_anual_company_priorities': priority_item}}
        )
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_quarterly_company_priorities(email):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    existing_data = collection.find_one({"email": email})
    # If existing data is found, use it to pre-fill the form; otherwise, use default values
    prefill_data = existing_data.get("s8_quarterly_company_priority_smart", {})
    prefill_data_2 = existing_data.get("s8_anual_company_priorities", {})
    # Use list comprehension to extract 'company_priority' from each dictionary
    anual_priorities = [item['company_priority'] for item in prefill_data_2]
    st.markdown('##### :orange[Quarterly Company Priorities]')
    show_quarterly_priority(email)
    with st.form(key='s8_quarterly_priorities'):
        quarterly_company_priority = st.text_area('Quarterly Company Priority')
        col1, col2 = st.columns(2)
        with col1:
            owner = st.text_input('Owner')
            quarterly_number = st.selectbox('Quarterly period', (1,2,3,4), index=None)
        with col2:
            success_criteria = st.selectbox('Success Criteria', ('Will happen', 'At risk - need help', 'Will not happen'), index=None)
            anual_priority_parent = st.selectbox('Anual priority', (anual_priorities), index=None)
        submitted_s8_quarterly_priority = st.form_submit_button(":orange[Add quarterly priority]")
        if submitted_s8_quarterly_priority:
            try:
                priority_item ={
                    "s8_quarterly_company_priorities": {
                        "company_priority": quarterly_company_priority,
                        "owner": owner,
                        "success_criteria": success_criteria,
                        "quarterly_number": quarterly_number,
                        "anual_priority_parent": anual_priority_parent
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Quarterly priority saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

    with st.form(key='s8_quarterly_company_priority_smart'):
        quarterly_company_priority_smart = st.text_area("What's one specific thing we can do as an organization to improve next period based on last period's Priorities?",
                                              placeholder="Refine and rewrite your idea as a S.M.A.R.T. priority",
                                              value=prefill_data.get("quarterly_company_priority_smart", ""))
        
        submitted_s8_quarterly_priority_smart = st.form_submit_button(":orange[Add SMART quarterly priority]")
        if submitted_s8_quarterly_priority_smart:
            try:
                priority_smart_item ={
                    "s8_quarterly_company_priority_smart": {
                        "quarterly_company_priority_smart": quarterly_company_priority_smart,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$set": priority_smart_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("SMART Company Priority saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_quarterly_priority(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        priorities_data = company_data.get('s8_quarterly_company_priorities', [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, priority in enumerate(priorities_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the cash details
                st.markdown(f":orange[{index}-] {priority.get('company_priority', 'N/A')} :orange[/] {priority.get('owner', 'N/A')} :orange[/] {priority.get('success_criteria', 'N/A')} :orange[/] {priority.get('anual_priority_parent', 'N/A')}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{priority['company_priority']}_{priority['owner']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_quarterly_priority(email, priority)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No anual priorities saved for {email}.")

def delete_quarterly_priority(email, priority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {'s8_quarterly_company_priorities': priority_item}}
        )
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_priorities_individual(email):
    st.markdown('##### :orange[Individual Priorities]')
    show_priority_individual(email)
    with st.form(key='s8_priorities_individual'):
        individual_priority = st.text_area('Individual Priority')
        col1, col2, col3 = st.columns(3)
        with col1:
            owner_individual = st.text_input('Owner')
        with col2:
            status_individual = st.selectbox('Status', ('Will happen', 'At risk - need help', 'Will not happen'), index=None)
        next_steps_individual_priority = st.text_area('If applicable, what are your next steps to complete Individual Priority',
                                                      placeholder="Enter the action Item on your WWW Worksheet")
        with col3:
            deadline_individual = st.date_input('Deadline', value=None, format='DD/MM/YYYY')
        submitted_s8_priority_individual = st.form_submit_button("Add")
        if submitted_s8_priority_individual:
            deadline_individual =deadline_individual.strftime("%d/%m/%Y")
            try:
                individual_priority_item ={
                    "s8_individual_priorities": {
                        "individual_priority": individual_priority,
                        "owner_individual": owner_individual,
                        "status_individual": status_individual,
                        "deadline_individual": deadline_individual,
                        "next_steps_individual_priority": next_steps_individual_priority,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email": email}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": individual_priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # collection.insert_one(perfil)
                st.success("Individual Priority saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_priority_individual(email):
    company_data = collection.find_one({"email": email})
    if company_data:
        ipriorities_data = company_data.get('s8_individual_priorities', [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, ipriority in enumerate(ipriorities_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Display the cash details
                st.markdown(f":orange[{index}-] {ipriority.get('individual_priority', 'N/A')} :orange[/] {ipriority.get('owner_individual', 'N/A')} :orange[/] {ipriority.get('status_individual', 'N/A')} :orange[/] {ipriority.get('deadline_individual', 'N/A')}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{ipriority['individual_priority']}_{ipriority['owner_individual']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_priority_individual(email, ipriority)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No Individual priority saved for {email}.")

def delete_priority_individual(email, ipriority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email": email},
            {"$pull": {'s8_individual_priorities': ipriority_item}}
        )
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")




def session_nine_individual_13_week(email):
    with st.form(key='session_9_individual_13_week'):
        st.markdown("##### :orange[Individual 13-Week Race]")
        individual_name = st.text_input("Your Name")
        col1, col2, col3, col4, col5 = st.columns([1.3,.7,1,1.5,.5])
        with col1:
            # st.write("Your KPIs")
            kp1_1 = st.text_area('Your KPI 1', key="kpi_1")
            kp1_2 = st.text_area('Your KPI 2', key="kpi_2")
            kp1_3 = st.text_area('Your KPI 3', key="kpi_3")
        with col2:
            # st.write("Goal")
            goal_1 = st.text_area('Goal 1',key="Goal_1")
            goal_2 = st.text_area('Goal 2',key="Goal_2")
            goal_3 = st.text_area('Goal 3',key="Goal_3")
        with col3:
            critical_1 = st.radio("Critical #1",
                                  [":green[■]",":green[■]", 
                                   ":orange[■]", ":red[■]"],
                                   )



        submit_session_nine_individual_13_week = st.form_submit_button("ADD KPI")




