import streamlit as st

def calculate_gpa(marks, total_marks, credits):
    total_points = 0
    total_credits = 0
    for mark, total, credit in zip(marks, total_marks, credits):
        percentage = (mark / total) * 100
        # GPA scale
        if percentage >= 90:
            grade_point = 4.0
        elif percentage >= 85:
            grade_point = 3.7
        elif percentage >= 80:
            grade_point = 3.3
        elif percentage >= 75:
            grade_point = 3.0
        elif percentage >= 70:
            grade_point = 2.7
        elif percentage >= 65:
            grade_point = 2.3
        elif percentage >= 60:
            grade_point = 2.0
        elif percentage >= 50:
            grade_point = 1.5
        else:
            grade_point = 0.0

        total_points += grade_point * credit
        total_credits += credit

    return round(total_points / total_credits, 2) if total_credits != 0 else 0


def calculate_cgpa(gpas, credits_list):
    total_points = 0
    total_credits = 0
    for gpa, credit in zip(gpas, credits_list):
        total_points += gpa * credit
        total_credits += credit
    return round(total_points / total_credits, 2) if total_credits != 0 else 0


st.title("GPA & CGPA Calculator")

option = st.selectbox("Choose an option:", ["Calculate GPA", "Calculate CGPA"])

if option == "Calculate GPA":
    num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)
    
    marks = []
    total_marks = []
    credits = []
    
    for i in range(int(num_subjects)):
        marks.append(st.number_input(f"Marks obtained for subject {i+1}:", min_value=0, step=1))
        total_marks.append(st.number_input(f"Total marks for subject {i+1}:", min_value=1, value=100, step=1))
        credits.append(st.number_input(f"Credit hours for subject {i+1}:", min_value=1, step=1))
    
    if st.button("Calculate GPA"):
        gpa = calculate_gpa(marks, total_marks, credits)
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
