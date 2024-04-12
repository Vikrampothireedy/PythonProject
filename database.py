import pandas as pd  ##for data manipulation
import numpy as np   # for linear algebra 
import matplotlib.pyplot as plt #for creating static, interactive, and animated visualizations in various formats. 
import seaborn as sns  # Python data visualization library

import matplotlib.image as img
# for Precision and Recall Analysis



import sqlite3

conn = sqlite3.connect('Loan_data.db')  # Connect to SQLite database
cursor = conn.cursor()

df = pd.read_csv(r"C:\Users\lazzyguy\Documents\Vscode Python\Project\loan_data.csv")

# Insert Data into SQLite Database

df.to_sql('users', conn, if_exists='append', index=False)

# Commit the transaction
conn.commit()

cursor.execute('''SELECT * FROM users''')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)


#Convert SQLite data to Pandas DataFrame
df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])



#View Data
print(df)