import sqlite3

conn = sqlite3.connect('landslides.sqlite')
cur = conn.cursor()

#extract the list of countries from the database
cur.execute('SELECT country FROM Events')
countries = list()
for message_row in cur :
    if message_row[0] not in countries:
        countries.append(message_row[0])

#storing countries and its count of landslide events in a dictionary
events_country= dict()
for country in countries:
    cur.execute('SELECT count(id) FROM Events where country=?',(country,))
    count=cur.fetchone()[0]
    events_country[country]=count

#storing countries and its count of landslide deaths in a dictionary
deaths_number=dict()
for country in countries:
    cur.execute('SELECT sum(fatality) FROM Events where country=?',(country,))
    total=cur.fetchone()[0]
    deaths_number[country]=total

#print out sorted  data:1- landslide events count. 2- fatality count
evts =sorted([(v,k) for k,v in events_country.items()],reverse=True)
print("\nLandslide events count: \n ")
for line in evts:
    print(line[1],line[0])

deaths = sorted([(v,k) for k,v in deaths_number.items()],reverse=True)
print("\nFatality count caused by landslide events: \n ")
for line in deaths:
    print(line[1],line[0])

print("run deaths_word_cloud.py to create a deaths count vizualization")
print("run events_line_chart.py  to create an event count vizualization ")