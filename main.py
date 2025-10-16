import streamlit as st

def calculate_gpa(marks, credits):
    total_points = 0
    total_credits = 0
    for mark, credit in zip(marks, credits):
        # Convert marks to grade points (simple scale)
        if mark >= 90:
            grade_point = 4.0
        elif mark >= 80:
            grade_point = 3.5
        elif mark >= 70:
            grade_point = 3.0
        elif mark >= 60:
            grade_point = 2.5
        elif mark >= 50:
            grade_point = 2.0
        else:
            grade_point = 0.0

        total_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        return 0
    return round(total_points / total_credits, 2)


def calculate_cgpa(gpas, credits_list):
    total_points = 0
    total_credits = 0
    for gpa, credit in zip(gpas, credits_list):
        total_points += gpa * credit
        total_credits += credit

    if total_credits == 0:
        return 0
    return round(total_points / total_credits, 2)


st.title("GPA & CGPA Calculator")

option = st.selectbox("Choose an option:", ["Calculate GPA", "Calculate CGPA"])

if option == "Calculate GPA":
    num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)
    
    marks = []
    credits = []
    
    for i in range(int(num_subjects)):
        marks.append(st.number_input(f"Marks for subject {i+1}:", min_value=0, max_value=100, step=1))
        credits.append(st.number_input(f"Credit hours for subject {i+1}:", min_value=1, step=1))
    
    if st.button("Calculate GPA"):
        gpa = calculate_gpa(marks, credits)
        st.success(f"Your GPA for this semester is: {gpa}")


elif option == "Calculate CGPA":
    num_semesters = st.number_input("Enter number of semesters:", min_value=1, step=1)
    
    gpas = []
    sem_credits = []
    
    for i in range(int(num_semesters)):
        gpas.append(st.number_input(f"GPA for semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01))
        sem_credits.append(st.number_input(f"Total credit hours for semester {i+1}:", min_value=1, step=1))
    
    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa(gpas, sem_credits)
        st.success(f"Your CGPA is: {cgpa}")
