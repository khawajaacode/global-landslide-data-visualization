import sqlite3

conn = sqlite3.connect('landslides.sqlite')
cur = conn.cursor()

#extract the list of countries from the database
cur.execute('SELECT country FROM Events')
countries = list()
for message_row in cur :
    if message_row[0] not in countries:
        countries.append(message_row[0])

#extract the list of years from the database
cur.execute('SELECT year FROM Events')
years = list()
for message_row in cur :
    if message_row[0] not in years:
        years.append(message_row[0])

#write lists to event_line_chart.js file containing lists of each year and number of landslide events in that year

#writing first row
fhand = open('static/event_line_chart.js','w') 
fhand.write("event_line_chart = [ ['Year'")
years.sort()
for country in countries:
    fhand.write(",'"+country+"'")
fhand.write("]")
#writing the rest of rows
for year in years:
    fhand.write(",\n['"+str(year)+"'")
    for country in countries:
        cur.execute('SELECT count(id) FROM Events where country=? and year = ?',(country,year))
        q=cur.fetchone()
        fhand.write(","+str(q[0]))
    fhand.write("]")

fhand.write("\n];\n")
fhand.close()

print("Output written to event_line_chart.js")
print("Open event_line_chart.htm to visualize the data")
 