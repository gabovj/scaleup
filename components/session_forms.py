import streamlit as st
from pymongo import MongoClient
import time
from datetime import datetime
import components.metricas_efectiv as mce

# Use your MongoDB Atlas connection string here
mongo_uri = st.secrets["mongo_uri"]
# Create a MongoClient using the provided URI
client = MongoClient(mongo_uri)
# Specify the database and collection
db = client["ScalingUP"]
collection = db["Companies"]

def session_one(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Initialize company_name with a default value
    company_name = "No Company Selected"
    # Update the query to include both email and company_id
    query = {"email_coach": email, "company_id": company_id}
    # Try to retrieve existing data for the specified email and company_id
    existing_data = collection.find_one(query)
    # Check if existing data is found, use it to pre-fill the form; otherwise, use default values
    if existing_data:
        prefill_data = existing_data.get("s1_rockefeller_habits", {})
        # Update company_name if it exists in the document
        company_name = existing_data.get("company_name", company_name)
    else:
        prefill_data = {}  # Use an empty dictionary if no data is found
    with st.form(key='s1'):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Company: :orange[{st.session_state['company_name']}]")
        with col2:
            st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
        st.divider()
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s1_rockefeller_habits}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s1_rockefeller_habits",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s1_rockefeller_habits
                    }
                }
                log_collection.insert_one(log_entry)

                st.success("Habits saved!")

            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_spirituality(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
    # If existing data is found, use it to pre-fill the form; otherwise, use empty strings
    prefill_data = existing_data.get("s2_oppp_spirituality", {}) if existing_data else {}
    with st.form(key='s2_spirituality'):
        st.markdown('##### :orange[Spirituality 10-25 years (Aspirations)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            spirituality_relationships_10_25_years = st.text_area("Relationships", key="spirituality_relationship_10_25",
                                                         placeholder='SPIRITUALITY - Write the relationship aspirations you want to achieve in 10-25 years.',
                                                         value=prefill_data.get("spirituality_10_25_years", {}).get("spirituality_relationships_10_25_years", ""))
        with col2:
            spirituality_achievements_10_25_years = st.text_area("Achievements", key="spirituality_achievements_10_25",
                                                        placeholder='SPIRITUALITY - Write the achievements aspirations you want to achieve in 10-25 years.',
                                                        value=prefill_data.get("spirituality_10_25_years", {}).get("spirituality_achievements_10_25_years", ""))
        with col3:
            spirituality_rituals_10_25_years = st.text_area("Rituals", key="spirituality_rituals_10_25",
                                                   placeholder='SPIRITUALITY - Write the rituals aspirations you want to achieve in 10-25 years.',
                                                   value=prefill_data.get("spirituality_10_25_years", {}).get("spirituality_rituals_10_25_years", ""))
        with col4:
            spirituality_wealth_10_25_years = st.text_area("Wealth ($)", key="spirituality_wealth_10_25",
                                                  placeholder='SPIRITUALITY - Write the wealth aspirations you want to achieve in 10-25 years.',
                                                  value=prefill_data.get("spirituality_10_25_years", {}).get("spirituality_wealth_10_25_years", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 1 year (Activities)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            spirituality_relationships_1_year = st.text_area("Relationships", key="spirituality_relationship_1",
                                                    placeholder='SPIRITUALITY - Write the relationship activities you plan to start in 1 year.',
                                                    value=prefill_data.get("spirituality_1_year", {}).get("spirituality_relationships_1_year", ""))
        with col2:
            spirituality_achievements_1_year = st.text_area("Achievements", key="spirituality_achievements_1",
                                                   placeholder='SPIRITUALITY - Write the achievements activities you plan to start in 1 year.',
                                                   value=prefill_data.get("spirituality_1_year", {}).get("spirituality_achievements_1_year", ""))
        with col3:
            spirituality_rituals_1_year = st.text_area("Rituals", key="spirituality_rituals_1",
                                              placeholder='SPIRITUALITY - Write the rituals activities you plan to start in 1 year.',
                                              value=prefill_data.get("spirituality_1_year", {}).get("spirituality_rituals_1_year", ""))
        with col4:
            spirituality_wealth_1_year = st.text_area("Wealth ($)", key="spirituality_wealth_1",
                                             placeholder='SPIRITUALITY - Write the wealth activities you plan to start in 1 year.',
                                             value=prefill_data.get("spirituality_1_year", {}).get("spirituality_wealth_1_year", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 90 days (Start Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            spirituality_relationships_start_90_days = st.text_area("Relationships", key="spirituality_relationships_90_start",
                                                           placeholder='SPIRITUALITY - Write the relationships actions you want to start in the next 90 days.', 
                                                           value=prefill_data.get("spirituality_90_days", {}).get("spirituality_relationships_start_90_days", ""))
        with col2:
            spirituality_achievements_start_90_days = st.text_area("Achievements", key="spirituality_achievements_90_start",
                                                          placeholder='SPIRITUALITY - Write the achivements actions you want to stop in the next 90 days.',
                                                          value=prefill_data.get("spirituality_90_days", {}).get("spirituality_achievements_start_90_days", ""))
        with col3:
            spirituality_rituals_start_90_days = st.text_area("Rituals", key="spirituality_rituals_90_start",
                                                     placeholder='SPIRITUALITY - Write the ritual actions you want to stop in the next 90 days.',
                                                     value=prefill_data.get("spirituality_90_days", {}).get("spirituality_rituals_start_90_days", ""))
        with col4:
            spirituality_wealth_start_90_days = st.text_area("Wealth ($)", key="spirituality_wealth_90_start",
                                                    placeholder='SPIRITUALITY - Write the wealth actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("spirituality_90_days", {}).get("spirituality_wealth_start_90_days", ""))
        st.divider()
        st.markdown('##### :orange[Spirituality 90 days (Stop Actions)]')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            spirituality_relationships_stop_90_days = st.text_area("Relationships", key="spirituality_relationships_90_stop",
                                                          placeholder='SPIRITUALITY - Write the relationships actions you want to stop in the next 90 days',
                                                          value=prefill_data.get("spirituality_90_days", {}).get("spirituality_relationships_stop_90_days", ""))
        with col2:
            spirituality_achievements_stop_90_days = st.text_area("Achievements", key="spirituality_achievements_90_stop",
                                                         placeholder='SPIRITUALITY - Write the achivements actions you want to stop in the next 90 days.',
                                                         value=prefill_data.get("spirituality_90_days", {}).get("spirituality_achievements_stop_90_days", ""))
        with col3:
            spirituality_rituals_stop_90_days = st.text_area("Rituals", key="spirituality_rituals_90_stop",
                                                    placeholder='SPIRITUALITY - Write the ritual actions you want to stop in the next 90 days.',
                                                    value=prefill_data.get("spirituality_90_days", {}).get("spirituality_rituals_stop_90_days", ""))
        with col4:
            spirituality_wealth_stop_90_days = st.text_area("Wealth ($)", key="spirituality_wealth_90_stop",
                                                   placeholder='SPIRITUALITY - Write the wealth actions you want to stop in the next 90 days.',
                                                   value=prefill_data.get("spirituality_90_days", {}).get("spirituality_wealth_stop_90_days", ""))
        
        submitted_s2_spirituality = st.form_submit_button(":orange[Save SPIRITUALITY Info]")
        if submitted_s2_spirituality:
            try:
                s2_spirituality = {
                    "s2_oppp_spirituality": {
                        "spirituality_90_days": {
                            "spirituality_relationships_start_90_days": spirituality_relationships_start_90_days,
                            "spirituality_relationships_stop_90_days": spirituality_relationships_stop_90_days,
                            "spirituality_achievements_start_90_days": spirituality_achievements_start_90_days,
                            "spirituality_achievements_stop_90_days": spirituality_achievements_stop_90_days,
                            "spirituality_rituals_start_90_days": spirituality_rituals_start_90_days,
                            "spirituality_rituals_stop_90_days": spirituality_rituals_stop_90_days,
                            "spirituality_wealth_start_90_days": spirituality_wealth_start_90_days,
                            "spirituality_wealth_stop_90_days": spirituality_wealth_stop_90_days,
                        },
                        "spirituality_1_year": {
                            "spirituality_relationships_1_year": spirituality_relationships_1_year,
                            "spirituality_achievements_1_year": spirituality_achievements_1_year,
                            "spirituality_rituals_1_year": spirituality_rituals_1_year,
                            "spirituality_wealth_1_year": spirituality_wealth_1_year,
                        },
                        "spirituality_10_25_years": {
                            "spirituality_relationships_10_25_years": spirituality_relationships_10_25_years,
                            "spirituality_achievements_10_25_years": spirituality_achievements_10_25_years,
                            "spirituality_rituals_10_25_years": spirituality_rituals_10_25_years,
                            "spirituality_wealth_10_25_years": spirituality_wealth_10_25_years,
                        },
                    }
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_spirituality}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s2_spirituality",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s2_spirituality
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("SPIRITUALITY info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_family(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_family}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s2_family",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s2_family
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("FAMILY info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_friends(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_friends}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s2_friends",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s2_friends
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("FRIENDS info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_fitness(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_fitness}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s2_fitness",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s2_fitness
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("FITNESS info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_two_finance(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s2_finance}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s2_finance",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s2_finance
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("FINANCE info saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_three(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    show_face(email, company_id)
    
    with st.form(key='s3', clear_on_submit=False):
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $push operator to add
                update_doc = {"$push": face_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: face_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": face_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("FACe saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_face(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
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
                    delete_face(email, company_id, face)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_face(email, company_id, face_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {"s3_face": face_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: face_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": face_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("FACe deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_opsp(email):
    st.markdown('##### One-Page Strategic Plan (OPSP)')
    st.text('Falta')

def session_four_swt_strenght(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Strenghts]')
    show_strengths(email, company_id)
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $push operator to add
                update_doc = {"$push": strenght_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: strenght_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": strenght_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Strenght saved!")
                # time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_strengths(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
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
                    delete_strenght(email, company_id, strenght)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_strenght(email, company_id, strenght_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {"s4_strenghts": strenght_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: strenght_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": strenght_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_swt_weaknesses(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Weaknesses]')
    show_weaknesses(email, company_id)
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $push operator to add
                update_doc = {"$push": weakness_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: weakness_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": weakness_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Weakness saved!")
                # time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_weaknesses(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
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
                    delete_weakness(email, company_id, weakness)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No weaknesses data saved for {email}.")

def delete_weakness(email, company_id, weakness_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {"s4_weaknesses": weakness_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: weakness_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": weakness_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Weakness deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_four_swt_trends(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    st.markdown('##### :orange[Trends]')
    show_trends(email, company_id)
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $push operator to add
                update_doc = {"$push": trend_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: trend_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": trend_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Trend saved!")
                # time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_trends(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
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
                    delete_trend(email, company_id, trend)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No weaknesses data saved for {email}.")

def delete_trend(email, company_id, trend_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {"s4_trends": trend_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: trend_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": trend_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_five(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)

    # Check if existing_data is not None
    if existing_data:
        prefill_data = existing_data.get("s5_7_strata", {})
    else:
        prefill_data = {}
    with st.form(key='s5'):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Company: :orange[{st.session_state['company_name']}]")
        with col2:
            st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
        st.divider()
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
                filter_doc = {"email_coach": email, "company_id": company_id}
                 # Use the $set operator to update the desired fields
                update_doc = {"$set": s5_7_strata}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: s5_7_strata",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": s5_7_strata
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("7 Strata saved!")
                # time.sleep(3)
                # st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def session_six(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
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
        show_cash(email, company_id, array_name= f's6_cash_{index}', input_1=f'cash_{index}', input_2=f'select_cash_{index}')
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
                    filter_doc = {"email_coach": email, "company_id": company_id}
                    # Use the $set operator to update the desired fields
                    update_doc = {"$push": cash_item}
                    # Use upsert=True to insert a new document if no matching document is found
                    collection.update_one(filter_doc, update_doc, upsert=True)
                    # Log the action
                    log_collection = db["ScaleUpActionLogs"]
                    log_entry = {
                        "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                        "action": "Added: cash_item",
                        "details": {
                            "email": email,
                            "company_id": company_id,
                            "changes": cash_item
                        }
                    }
                    log_collection.insert_one(log_entry)
                    st.success("Data saved!")
                    st.rerun()
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        st.divider()
    
def show_cash(email, company_id, array_name, input_1, input_2):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
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
                    delete_cash(email, company_id, array_name, cash)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No FACe data saved for {email}.")

def delete_cash(email, company_id,array_name, cash_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {array_name: cash_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: cash_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": cash_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_seven_cash(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    # Initialize prefill_data with a default value
    prefill_data = {}
    if company_data:
        prefill_data = company_data.get("s7_metricas_efectivo", {})
    # print("Prefill Data:", prefill_data)

    st.write('##### :orange[Metricas Clave de Efectivo]')
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    with st.form(key='metricas_clave_efectivo'):
        col1, col2 = st.columns(2)
        with col1:
            st.write(':orange[Índice de Solvencia]')
            activo_circulante = st.number_input('Activo circulante', 
                                                value=prefill_data.get("activo_circulante", None),
                                                placeholder='Ingresa un valor')
            pasivo_corto_plazo = st.number_input('Pasivo corto plazo', 
                                                 value=prefill_data.get("pasivo_corto_plazo", None),
                                                 placeholder='Ingresa un valor')
            mce.indice_solvencia(email, company_id)
            st.divider()

            st.write(':orange[Días Cartera]')
            promedio_cuentas_por_cobrar_clientes = st.number_input('Promedio cuentas por cobrar a clientes', 
                                                                   value=prefill_data.get("promedio_cuentas_por_cobrar_clientes", None),
                                                                   placeholder='Ingresa un valor')
            ventas_netas = st.number_input('Ventas Netas', 
                                           value=prefill_data.get("ventas_netas", None),
                                           placeholder='Ingresa un valor')
            mce.dias_cartera(email, company_id)
            st.divider()

            st.write(':orange[Días proveedor]')
            promedio_cuentas_por_pagar_proveedores = st.number_input('Promedio de cuentas por pagar a proveedores', 
                                                                     value=prefill_data.get("promedio_cuentas_por_pagar_proveedores", None),
                                                                     placeholder='Ingresa un valor')
            compras_netas = st.number_input('Compras netas (promedio de inventarios)', 
                                            value=prefill_data.get("compras_netas", None), 
                                            placeholder='Ingresa un valor')
            mce.dias_proveedor(email, company_id)
            st.divider()

            st.write(':orange[Utilidad Neta]')
            ventas_netas_display = prefill_data.get("ventas_netas", 0)
            costo_ventas_display = prefill_data.get("costo_ventas", 0)
            st.markdown('Ventas netas')
            st.markdown(str(ventas_netas_display))  # Convert to string for display
            st.markdown('Costo de ventas')
            st.markdown(str(costo_ventas_display))  # Convert to string for display
            gastos_totales = st.number_input('Gastos totales', 
                                            value=prefill_data.get("gastos_totales", None),  # Default to 0 if None
                                            placeholder='Ingresa un valor')
            # if gastos_totales is None:
            #     st.error("Please enter a value for 'Gastos totales' to proceed.")
            # else:
            mce.utilidad_neta(email, company_id)       
        
        with col2:
            st.write(':orange[Rentabilidad de las Ventas]')
            utilidad_neta = st.number_input('Utilidad Neta',
                                            value=prefill_data.get("utilidad_neta", None),
                                            placeholder='Ingresa un valor')
            st.markdown('Ventas netas')
            st.markdown(ventas_netas_display)
            mce.rentabilidad_ventas(email, company_id)
            st.divider()

            st.write(':orange[Días Inventario]')
            promedio_inventarios = st.number_input('Promedio inventarios',
                                                   value=prefill_data.get("promedio_inventarios", None),
                                                   placeholder='Ingresa un valor')
            costo_ventas = st.number_input('Costo de ventas',
                                           value=prefill_data.get("costo_ventas", None),
                                           placeholder='Ingresa un valor')
            mce.dias_inventario(email, company_id)
            st.divider()

            st.write(':orange[Apalancamiento]')
            pasivo_total = st.number_input('Pasivo total', 
                                           value=prefill_data.get("pasivo_total", None),
                                           placeholder='Ingresa un valor')
            activo_total = st.number_input('Activo total', 
                                           value=prefill_data.get("activo_total", None),
                                           placeholder='Ingresa un valor')
            # if pasivo_total is None:
            #     st.error("Please enter a value for 'Pasivo total' to proceed.")
            # else:
            mce.apalancamiento(email, company_id)

        submit_metricas_clave_efectivo = st.form_submit_button(':orange[Calcular metricas]')

        if submit_metricas_clave_efectivo:
            try:
                metricas_efectivo_item = {
                    "s7_metricas_efectivo":{
                        "activo_circulante": activo_circulante,
                        "pasivo_corto_plazo": pasivo_corto_plazo,
                        "promedio_cuentas_por_cobrar_clientes": promedio_cuentas_por_cobrar_clientes,
                        "ventas_netas": ventas_netas,
                        "promedio_cuentas_por_pagar_proveedores": promedio_cuentas_por_pagar_proveedores,
                        "compras_netas": compras_netas,
                        "utilidad_neta": utilidad_neta,
                        "promedio_inventarios": promedio_inventarios,
                        "costo_ventas": costo_ventas,
                        "pasivo_total": pasivo_total,
                        "activo_total": activo_total,
                        "gastos_totales": gastos_totales,
                    }
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$set": metricas_efectivo_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Updated: metricas_efectivo_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": metricas_efectivo_item
                    }
                }
                log_collection.insert_one(log_entry)
                with st.spinner('Generando Metricas!'):
                    time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
def extract_value(data):
    if isinstance(data, dict):
        return float(data.get("$numberDouble", 0))
    return float(data)   

def session_eight(email, company_id):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    st.markdown('##### :orange[Who • What • When (WWW)]')
    show_www(email, company_id)
    with st.form(key=f's8_www'):      
        col1, col2, col3 = st.columns(3)
        with col1:
            who = st.text_input('Who')
        with col2:
            what = st.text_input('What')
        with col3:
            when = st.date_input('When', value=None, format="DD/MM/YYYY")
        submitted_s8_www = st.form_submit_button(":orange[Add WWW]")
        if submitted_s8_www:
            try:
                # Convert the date to a datetime object
                when_datetime = datetime.combine(when, datetime.min.time())
                www_item ={
                    "s8_www": {
                        "who": who,
                        "what": what,
                        "when": when_datetime,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": www_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: www_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": www_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("WWW saved!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
def show_www(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        www_data = company_data.get('s8_www', [])
        # name_db = company_data.get("company_name", "Unknown Company")
        for index, www in enumerate(www_data, start=1):
            # Use columns to layout cash details and delete button
            col1, col2 = st.columns([0.9, 0.1])
            
            with col1:
                # Retrieve and format the date
                when_date = www.get('when', None)
                formatted_date = when_date.strftime('%d-%b-%Y').upper() if when_date else 'N/A'
                
                # Display the WWW data
                st.markdown(f":orange[{index}-] {www.get('who', 'N/A')} :orange[/] {www.get('what', 'N/A')} :orange[/] {formatted_date}")
                
            with col2:
                # Construct a unique key for the button based on the face details
                button_key = f"delete_{www['who']}_{www['what']}"
                # Display the delete button next to the face details with the unique key
                if st.button(":red[Delete]", key=button_key):
                    delete_www(email, company_id, www)
                    # Refresh the page to see the updated list
                    st.rerun()
    else:
        st.info(f"No WWW data saved for {email}.")

def delete_www(email, company_id, www_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_www': www_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: www_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": www_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_winning_moves(email, company_id):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    show_winning_moves(email, company_id)
    with st.form(key=f's8_winning_moves'):
        st.markdown('##### :orange[Winning Moves]')
        col1, col2, col3= st.columns(3)
        with col1:
            winning_move_name = st.text_input('Name')
        with col2:
            winning_move_owner = st.text_input('Owner')
        with col3:
            winning_move_end_date = st.date_input('End date', format="DD/MM/YYYY", value=None)        
        winning_move_supergreen = st.text_input(':green[Super Green]')
        winning_move_green = st.text_input(':green[Green]')
        winning_move_yellow = st.text_input(':orange[Yellow]')
        winning_move_red = st.text_input(':red[Red]')

        submitted_s8_winning_move = st.form_submit_button(":orange[Add Winning Move]")
        if submitted_s8_winning_move:
            try:
                winning_move_end_date = datetime.combine(winning_move_end_date, datetime.min.time())
                winning_move_item ={
                    "s8_winning_moves": {
                        "wm_name": winning_move_name,
                        "wm_owner": winning_move_owner,
                        "wm_end_date": winning_move_end_date,
                        "winning_move_supergreen": winning_move_supergreen,
                        "winning_move_green": winning_move_green,
                        "winning_move_yellow": winning_move_yellow,
                        "winning_move_red": winning_move_red     
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": winning_move_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: winning_move_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": winning_move_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Winning move saved!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_winning_moves(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        wm_data = company_data.get('s8_winning_moves', None)
        if wm_data:
            for index, wm in enumerate(wm_data, start=1):
                # Use columns to layout cash details and delete button
                col1, col2 = st.columns([0.9, 0.1])
                
                with col1:
                    # Display the cash details
                    st.markdown(f":orange[{index}-] {wm.get('wm_name', 'N/A')} :orange[/] {wm.get('wm_owner', 'N/A')}")
                    st.markdown(f":green[SuperGreen]: {wm.get('winning_move_supergreen', 'N/A')}")
                    st.markdown(f":green[Green]: {wm.get('winning_move_green', 'N/A')}")
                    st.markdown(f":orange[Yellow]: {wm.get('winning_move_yellow', 'N/A')}")
                    st.markdown(f":red[Red]: {wm.get('winning_move_red', 'N/A')}")
                with col2:
                    # Construct a unique key for the button based on the face details
                    button_key = f"delete_{wm['wm_name']}_{wm['wm_owner']}"
                    # Display the delete button next to the face details with the unique key
                    if st.button(":red[Delete]", key=button_key):
                        delete_wm(email, company_id, wm)
                        # Refresh the page to see the updated list
                        st.rerun()
        else:
            # Display an info message if 's8_winning_moves' does not exist or is empty
            st.info(f'No winning moves data available for :red[{st.session_state["company_name"]}], add some winning moves!')                        
    else:
        st.info(f"No data saved for {st.session_state['company_name']}.")

def delete_wm(email, company_id, wm_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_winning_moves': wm_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: winning_move_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": wm_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success("Deleted")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_anual_company_priorities(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    st.markdown('##### :orange[Anual Company Priorities]')
    show_anual_priority(email, company_id)
    with st.form(key='s8_anual_priorities'):
        anual_company_priority = st.text_input('Anual Company Priority')
        col1, col2 = st.columns(2)
        with col1:
            acp_owner = st.text_input('Owner')
        with col2:
            acp_end_date = st.date_input('End date', format="DD/MM/YYYY", value=None)
        acp_supergreen = st.text_input(':green[Super Green]', key="acp_SG")
        acp_green = st.text_input(':green[Green]', key="acp_G")
        acp_yellow = st.text_input(':orange[Yellow]', key="acp_Y")
        acp_red = st.text_input(':red[Red]', key="acp_R")
        submitted_s8_anual_priority = st.form_submit_button(":orange[Add anual priority]")
        if submitted_s8_anual_priority:
            try:
                acp_end_date = datetime.combine(acp_end_date, datetime.min.time())
                anual_priority_item ={
                    "s8_anual_company_priorities": {
                        "anual_company_priority": anual_company_priority,
                        "acp_owner": acp_owner,
                        "acp_end_date": acp_end_date,
                        "acp_supergreen": acp_supergreen,
                        "acp_green": acp_green,
                        "acp_yellow": acp_yellow,
                        "acp_red": acp_red,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": anual_priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: anual_priority_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": anual_priority_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Company Priority saved!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_anual_priority(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        priorities_data = company_data.get('s8_anual_company_priorities', None)
        if priorities_data:
            for index, priority in enumerate(priorities_data, start=1):
                # Use columns to layout cash details and delete button
                col1, col2 = st.columns([0.9, 0.1])
                
                with col1:
                    # Display the cash details
                    st.markdown(f":orange[{index}-] {priority.get('anual_company_priority', 'N/A')} :orange[/] {priority.get('acp_owner', 'N/A')}")
                    st.markdown(f":green[SuperGreen]: {priority.get('acp_supergreen', 'N/A')}")
                    st.markdown(f":green[Green]: {priority.get('acp_green', 'N/A')}")
                    st.markdown(f":orange[Yellow]: {priority.get('acp_yellow', 'N/A')}")
                    st.markdown(f":red[Red]: {priority.get('acp_red', 'N/A')}")
                    
                with col2:
                    # Construct a unique key for the button based on the face details
                    button_key = f"delete_{priority['anual_company_priority']}_{priority['acp_owner']}"
                    # Display the delete button next to the face details with the unique key
                    if st.button(":red[Delete]", key=button_key):
                        delete_anual_priority(email, company_id, priority)
                        # Refresh the page to see the updated list
                        st.rerun()
        else:
            st.info(f"No anual priorities saved for :red[{st.session_state['company_name']}], add some anual priorities!:point_down:")
    else:
        st.info(f"No anual priorities saved for {email}.")

def delete_anual_priority(email, company_id, priority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_anual_company_priorities': priority_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: anual_priority_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": priority_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_quarterly_company_priorities(email, company_id):
    # Initialize MongoDB client and select database and collection
    mongo_uri = st.secrets["mongo_uri"]
    client = MongoClient(mongo_uri)
    db = client["ScalingUP"]
    collection = db["Companies"]
    # Try to retrieve existing data for the user
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)    
    if existing_data:
        prefill_data_2 = existing_data.get("s8_anual_company_priorities", {})
    else:
        prefill_data_2 = {}
    # Use list comprehension to extract 'company_priority' from each dictionary
    anual_priorities = [item['anual_company_priority'] for item in prefill_data_2]
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    st.markdown('##### :orange[Quarterly Company Priorities]')
    show_quarterly_priority(email, company_id)
    with st.form(key='s8_quarterly_priorities'):
        quarterly_company_priority = st.text_input('Quarterly Company Priority')
        col1, col2 = st.columns(2)
        with col1:
            qcp_owner = st.text_input('Owner')
            quarterly_number = st.selectbox('Quarterly period', (1,2,3,4), index=None)    
        with col2:
            qcp_end_date = st.date_input('End date', format="DD/MM/YYYY", value=None)      
            anual_priority_parent = st.selectbox('Anual priority', (anual_priorities), index=None)
        qcp_supergreen = st.text_input(':green[Super Green]', key="qcp_SG")
        qcp_green = st.text_input(':green[Green]', key="qcp_G")
        qcp_yellow = st.text_input(':orange[Yellow]', key="qcp_Y")
        qcp_red = st.text_input(':red[Red]', key="qcp_R")
        
        submitted_s8_quarterly_priority = st.form_submit_button(":orange[Add quarterly priority]")
        if submitted_s8_quarterly_priority:
            try:
                qcp_end_date = datetime.combine(qcp_end_date, datetime.min.time())
                quarterly_priority_item ={
                    "s8_quarterly_company_priorities": {
                        "quarterly_company_priority": quarterly_company_priority,
                        "qcp_owner": qcp_owner,
                        "quarterly_number": quarterly_number,
                        "anual_priority_parent": anual_priority_parent,
                        "qcp_end_date": qcp_end_date,
                        "qcp_supergreen": qcp_supergreen,
                        "qcp_green": qcp_green,
                        "qcp_yellow": qcp_yellow,
                        "qcp_red": qcp_red
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": quarterly_priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: quarterly_priority_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": quarterly_priority_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Quarterly priority saved!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_quarterly_priority(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        priorities_data = company_data.get('s8_quarterly_company_priorities', None)
        if priorities_data:
            for index, q_priority in enumerate(priorities_data, start=1):
                # Use columns to layout cash details and delete button
                col1, col2 = st.columns([0.9, 0.1])
                
                with col1:
                    # Display the cash details
                    st.markdown(f":orange[{index}-] {q_priority.get('quarterly_company_priority', 'N/A')} :orange[/] {q_priority.get('qcp_owner', 'N/A')} :orange[/] {q_priority.get('anual_priority_parent', 'N/A')}")
                    st.markdown(f":green[SuperGreen]: {q_priority.get('qcp_supergreen', 'N/A')}")
                    st.markdown(f":green[Green]: {q_priority.get('qcp_green', 'N/A')}")
                    st.markdown(f":orange[Yellow]: {q_priority.get('qcp_yellow', 'N/A')}")
                    st.markdown(f":red[Red]: {q_priority.get('qcp_red', 'N/A')}")
                with col2:
                    # Construct a unique key for the button based on the face details
                    button_key = f"delete_{q_priority['quarterly_company_priority']}_{q_priority['qcp_owner']}"
                    # Display the delete button next to the face details with the unique key
                    if st.button(":red[Delete]", key=button_key):
                        delete_quarterly_priority(email, company_id,q_priority)
                        # Refresh the page to see the updated list
                        st.rerun()
        else:
            st.info(f"No quarterly priorities saved for :red[{st.session_state['company_name']}], add some quarterly priorities!:point_down:")
    else:
        st.info(f"No anual priorities saved for {email}.")

def delete_quarterly_priority(email, company_id, priority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_quarterly_company_priorities': priority_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: quarterly_priority_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": priority_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_priorities_individual(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    existing_data = collection.find_one(query)
    if existing_data:
        qcp_data = existing_data.get("s8_quarterly_company_priorities", {})
    else:
        qcp_data = {} 
    q_priorities = [item['quarterly_company_priority'] for item in qcp_data]
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    st.markdown('##### :orange[Individual Priorities]')
    show_priority_individual(email, company_id)
    with st.form(key='s8_priorities_individual'):
        individual_priority = st.text_input('Individual Priority')
        col1, col2, col3 = st.columns(3)
        with col1:
            ip_owner = st.text_input('Owner', key="ip_owner")
        with col2:
            deadline_individual = st.date_input('Deadline', value=None, format='DD/MM/YYYY')
        with col3:
            quarterly_priority_parent = st.selectbox('Quarterly priority', (q_priorities), index=None)
        ip_supergreen = st.text_input(':green[Super Green]', key="ip_SG")
        ip_green = st.text_input(':green[Green]', key="ip_G")
        ip_yellow = st.text_input(':orange[Yellow]', key="ip_Y")
        ip_red = st.text_input(':red[Red]', key="ip_R")
        submitted_s8_priority_individual = st.form_submit_button(":orange[Add Individual Priority]")
        if submitted_s8_priority_individual:
            deadline_individual =deadline_individual.strftime("%d/%m/%Y")
            try:
                individual_priority_item ={
                    "s8_individual_priorities": {
                        "individual_priority": individual_priority,
                        "ip_owner": ip_owner,
                        "deadline_individual": deadline_individual,
                        "quarterly_priority_parent": quarterly_priority_parent,
                        "ip_supergreen": ip_supergreen,
                        "ip_green": ip_green,
                        "ip_yellow": ip_yellow,
                        "ip_red": ip_red,
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": individual_priority_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: individual_priority_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": individual_priority_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Individual Priority saved!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_priority_individual(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        ipriorities_data = company_data.get('s8_individual_priorities', None)
        if ipriorities_data:
            for index, ipriority in enumerate(ipriorities_data, start=1):
                # Use columns to layout cash details and delete button
                col1, col2 = st.columns([0.9, 0.1])
                
                with col1:
                    # Display the cash details
                    st.markdown(f":orange[{index}-] {ipriority.get('individual_priority', 'N/A')} :orange[/] {ipriority.get('ip_owner', 'N/A')} :orange[/] {ipriority.get('quarterly_priority_parent', 'N/A')}")
                    st.markdown(f":green[SuperGreen]: {ipriority.get('ip_supergreen', 'N/A')}")
                    st.markdown(f":green[Green]: {ipriority.get('ip_green', 'N/A')}")
                    st.markdown(f":orange[Yellow]: {ipriority.get('ip_yellow', 'N/A')}")
                    st.markdown(f":red[Red]: {ipriority.get('ip_red', 'N/A')}")
                with col2:
                    # Construct a unique key for the button based on the face details
                    button_key = f"delete_{ipriority['individual_priority']}_{ipriority['ip_owner']}"
                    # Display the delete button next to the face details with the unique key
                    if st.button(":red[Delete]", key=button_key):
                        delete_priority_individual(email, company_id, ipriority)
                        # Refresh the page to see the updated list
                        st.rerun()
        else:
            st.info(f"No individual priorities saved for :red[{st.session_state['company_name']}], add some individual priorities!:point_down:")
    else:
        st.info(f"No Individual priority saved for {email}.")

def delete_priority_individual(email, company_id, ipriority_item):
    """
    Remove the specified face from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_individual_priorities': ipriority_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: individual_priority_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": ipriority_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success(" deleted!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def session_eight_kpi(email, company_id):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Company: :orange[{st.session_state['company_name']}]")
    with col2:
        st.write(f"Company ID: :orange[{st.session_state['company_id']}]")
    st.divider()
    st.markdown('##### :orange[KPIs]')
    show_kpi(email, company_id)
    with st.form(key='s8_kpis'):
        st.markdown('##### Define your process and KPIs')
        stage_name = st.text_input('Stage name')
        st.divider()
        col1, col2 = st.columns([.7,.3])
        with col1:
           living_kpi = st.text_input('Living KPI')
        with col2:
            living_kpi_owner = st.text_input('Owner', key="living_kpi_owner")
        living_kpi_supergreen = st.text_input(':green[Super Green]', key="living_kpi_SG")
        living_kpi_green = st.text_input(':green[Green]', key="living_kpi_G")
        living_kpi_yellow = st.text_input(':orange[Yellow]', key="living_kpi_Y")
        living_kpi_red = st.text_input(':red[Red]', key="living_kpi_R")

        st.divider()
        col1, col2 = st.columns([.7,.3])
        with col1:
           lagging_kpi = st.text_input('Lagging KPI')
        with col2:
            lagging_kpi_owner = st.text_input('Owner', key="lagging_kpi_owner")
        lagging_kpi_supergreen = st.text_input(':green[Super Green]', key="lagging_kpi_SG")
        lagging_kpi_green = st.text_input(':green[Green]', key="lagging_kpi_G")
        lagging_kpi_yellow = st.text_input(':orange[Yellow]', key="lagging_kpi_Y")
        lagging_kpi_red = st.text_input(':red[Red]', key="lagging_kpi_R")
        
        st.divider()
        col1, col2 = st.columns([.7,.3])
        with col1:
           efficiency_kpi = st.text_input('Efficiency KPI')
        with col2:
            efficiency_kpi_owner = st.text_input('Owner', key="efficiency_kpi_owner")
        efficiency_kpi_supergreen = st.text_input(':green[Super Green]', key="efficiency_kpi_SG")
        efficiency_kpi_green = st.text_input(':green[Green]', key="efficiency_kpi_G")
        efficiency_kpi_yellow = st.text_input(':orange[Yellow]', key="efficiency_kpi_Y")
        efficiency_kpi_red = st.text_input(':red[Red]', key="efficiency_kpi_R")  
        
        submitted_s8_kpi = st.form_submit_button(":orange[Add Stage]")
        if submitted_s8_kpi:
            try:
                stage_item = {
                    "s8_stage_kpis": {
                        stage_name: {
                            "living": {
                                "living_kpi": living_kpi,
                                "living_kpi_owner": living_kpi_owner,
                                "colors":{
                                    "living_kpi_supergreen": living_kpi_supergreen,
                                    "living_kpi_green": living_kpi_green,
                                    "living_kpi_yellow": living_kpi_yellow,
                                    "living_kpi_red": living_kpi_red,
                                    },
                            },
                            "lagging": {
                                "lagging_kpi": lagging_kpi,
                                "lagging_kpi_owner": lagging_kpi_owner,
                                "colors":{
                                    "lagging_kpi_supergreen": lagging_kpi_supergreen,
                                    "lagging_kpi_green": lagging_kpi_green,
                                    "lagging_kpi_yellow": lagging_kpi_yellow,
                                    "lagging_kpi_red": lagging_kpi_red,
                                     },
                            },
                            "efficiency": {
                                "efficiency_kpi": efficiency_kpi,
                                "efficiency_kpi_owner": efficiency_kpi_owner,
                                "colors":{
                                    "efficiency_kpi_supergreen": efficiency_kpi_supergreen,
                                    "efficiency_kpi_green": efficiency_kpi_green,
                                    "efficiency_kpi_yellow": efficiency_kpi_yellow,
                                    "efficiency_kpi_red": efficiency_kpi_red,
                                    }
                            },
                        }
                        
                    } 
                }
                # Filter for the document to update
                filter_doc = {"email_coach": email, "company_id": company_id}
                # Use the $set operator to update the desired fields
                update_doc = {"$push": stage_item}
                # Use upsert=True to insert a new document if no matching document is found
                collection.update_one(filter_doc, update_doc, upsert=True)
                # Log the action
                log_collection = db["ScaleUpActionLogs"]
                log_entry = {
                    "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
                    "action": "Added: kpi_stage_item",
                    "details": {
                        "email": email,
                        "company_id": company_id,
                        "changes": stage_item
                    }
                }
                log_collection.insert_one(log_entry)
                st.success("Stage saved!")
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")

def show_kpi(email, company_id):
    query = {"email_coach": email, "company_id": company_id}
    company_data = collection.find_one(query)
    if company_data:
        kpi_data = company_data.get('s8_stage_kpis', None)
        if kpi_data:
            for index, kpi in enumerate(kpi_data, start=1):
                for stage_name, stage_details in kpi.items():
                    col1, col2 = st.columns([0.9, 0.1])
                    with col1:
                        st.markdown(f":orange[{index}-] {stage_name}")
                        # Access 'living' KPI details
                        living_kpi_details = stage_details.get('living', {})
                        living_kpi = living_kpi_details.get('living_kpi', 'N/A')
                        st.markdown(f":orange[Living KPI:] {living_kpi}")
                        # Access 'lagging' KPI details
                        lagging_kpi_details = stage_details.get('lagging', {})
                        lagging_kpi = lagging_kpi_details.get('lagging_kpi', 'N/A')
                        st.markdown(f":orange[Lagging KPI:] {lagging_kpi}")
                        # Access 'efficiency' KPI details
                        efficiency_kpi_details = stage_details.get('efficiency', {})
                        efficiency_kpi = efficiency_kpi_details.get('efficiency_kpi', 'N/A')
                        st.markdown(f":orange[Efficiency KPI:] {efficiency_kpi}")
                    with col2:
                        # Construct a unique key for the button based on the face details
                        button_key = f"delete_{kpi[stage_name]}"
                        # Display the delete button next to the face details with the unique key
                        if st.button(":red[Delete]", key=button_key):
                            delete_kpi(email, company_id, kpi)
                            # Refresh the page to see the updated list
                            st.rerun()
        else:
            st.info(f"No Kpi's saved for :red[{st.session_state['company_name']}], add some Kpi's!:point_down:")
    else:
        st.info(f"No Individual priority saved for {email}.")

def delete_kpi(email, company_id, stage_item):
    """
    Remove the specified KPI from the database.
    """
    try:
        collection.update_one(
            {"email_coach": email, "company_id": company_id},
            {"$pull": {'s8_stage_kpis': stage_item}}
        )
        # Log the action
        log_collection = db["ScaleUpActionLogs"]
        log_entry = {
            "timestamp": datetime.now(),  # Ensure you import datetime from the datetime module
            "action": "Deleted: kpi_stage_item",
            "details": {
                "email": email,
                "company_id": company_id,
                "changes": stage_item
            }
        }
        log_collection.insert_one(log_entry)
        st.success(f"{stage_item} deleted!")
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




