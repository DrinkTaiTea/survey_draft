import streamlit as st
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('survey_results.db')
cursor = conn.cursor()

# Create the survey_responses table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS survey_responses (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        location TEXT,
        age_group TEXT,
        satisfaction_polks INTEGER,
        satisfaction_last_semester INTEGER,
        satisfaction_professors INTEGER,
        recommend_polks INTEGER
    )
''')
conn.commit()

# Streamlit survey form
st.title('Polk State College Survey')

name = st.text_input('Name:')
email = st.text_input('Email:')
location = st.text_input('Location:')
age_group = st.radio('Age Group:', ('18-24', '25-34', '35-44', '45-54', '60+'))

st.subheader('Question List:')
satisfaction_polks = st.radio('Rate your overall level of satisfaction with Polk State College:', [1, 2, 3, 4, 5])
satisfaction_last_semester = st.radio('Rate your level of satisfaction with your last semester:', [1, 2, 3, 4, 5])
satisfaction_professors = st.radio('Rate your level of satisfaction with your professors:', [1, 2, 3, 4, 5])
recommend_polks = st.radio('Would you recommend Polk State College:', [1, 2, 3, 4, 5])

if st.button('Submit'):
    # Insert survey response into the database
    cursor.execute('''
        INSERT INTO survey_responses (name, email, location, age_group, satisfaction_polks, 
        satisfaction_last_semester, satisfaction_professors, recommend_polks)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, location, age_group, satisfaction_polks,
          satisfaction_last_semester, satisfaction_professors, recommend_polks))
    conn.commit()

    # Thank the user
    st.success('Thank you for taking the survey!')

# Close the database connection
conn.close()
