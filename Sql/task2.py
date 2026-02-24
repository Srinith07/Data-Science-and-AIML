import sqlite3

import pandas as pd

# Connect to the existing database
conn = sqlite3.connect("academy.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")
cursor.executemany("""
INSERT INTO mentors (mentor_id, mentor_name, track)
VALUES (?, ?, ?)
""", [
    (1, "Dr. Mehta", "Data Science"),
    (2, "Mr. Sharma", "Web Development"),
    (3, "Ms. Iyer", "UI/UX")
])

conn.commit()
query = """
SELECT 
    i.name AS intern_name,
    i.track,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""

df = pd.read_sql_query(query, conn)

# Display result
df
conn.close()
