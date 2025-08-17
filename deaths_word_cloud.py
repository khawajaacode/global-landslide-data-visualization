import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('landslides.sqlite')
cur = conn.cursor()

#extract the list of countries from the database
cur.execute('SELECT country FROM Events')
countries = list()
for message_row in cur :
    if message_row[0] not in countries:
        countries.append(message_row[0])

#storing countries and its count of landslide deaths in a dictionary
deaths_number=dict()
for country in countries:
    cur.execute('SELECT sum(fatality) FROM Events where country=?',(country,))
    total=cur.fetchone()[0]
    deaths_number[country]=total

#extract the highest and lowest counts for scaling operation
x = sorted(deaths_number, key=deaths_number.get, reverse=True)
highest = None
lowest = None
for k in x:
    if highest is None or highest < deaths_number[k] :
        highest = deaths_number[k]
    if lowest is None or lowest > deaths_number[k] :
        lowest = deaths_number[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 30-130 based on the count
bigsize = 100
smallsize = 30

#write country name texts and sizes to graph_deaths.js file
fhand = open('static/deaths_word_cloud.js','w')
fhand.write("deaths_word_cloud = [")
first = True
for k in x:
    if not first : fhand.write( ",\n")
    first = False
    size = deaths_number[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    if deaths_number[k] == 0: #for countries with zero deaths set font size to 20 
        size = 20
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to deaths_word_cloud.js")
print("Open deaths_word_cloud.htm in a browser to see the vizualization")
