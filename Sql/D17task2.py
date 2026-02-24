import sqlite3
import pandas as pd

# Create / connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Drop tables if they already exist (start fresh)
cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("DROP TABLE IF EXISTS mentors")

# Create mentors table
cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# Create interns table
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT
)
""")

# Insert data into mentors
mentors_data = [
    (1, 'Alice', 'Data Science'),
    (2, 'Bob', 'Machine Learning'),
    (3, 'Charlie', 'Data Analytics')
]

cursor.executemany("INSERT INTO mentors VALUES (?, ?, ?)", mentors_data)

# Insert data into interns
interns_data = [
    (101, 'Srinith', 'Data Science'),
    (102, 'Rahul', 'Machine Learning'),
    (103, 'Priya', 'Data Analytics'),
    (104, 'Anita', 'Data Science')
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?)", interns_data)

conn.commit()
query = """
SELECT 
    interns.intern_id,
    interns.intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""
df = pd.read_sql_query(query, conn)
df
conn.close()
