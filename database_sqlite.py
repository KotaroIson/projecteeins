import sqlite3 
conn = sqlite3.connect('hackathon1.db')
cursor = conn.cursor()
cursor.execute('SELECT Ранг, Название FROM groups')
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
conn.close()

html_table = "<table border='1'>\n<tr>"
for column in column_names:
    html_table += f"<th>{column}</th>"
html_table += "</tr>\n"

for row in rows:
    html_table += "<tr>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>\n"
html_table += "</table>"

with open('table.html', 'w') as file:
    file.write(html_table)