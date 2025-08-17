import csv
import sqlite3

# Connect (or create) SQLite database
conn = sqlite3.connect('landslides.sqlite')
cur = conn.cursor()

# Drop old table (if exists, so re-runs don’t duplicate data)
cur.execute('DROP TABLE IF EXISTS Events')

# Create a new Events table
cur.execute('''
CREATE TABLE Events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    source TEXT,
    description TEXT,
    country TEXT,
    category TEXT,
    event_trigger TEXT,
    size TEXT,
    year INTEGER,
    fatality INTEGER
)
''')

# Open local CSV file (downloaded NASA dataset)
filename = 'data/landslides.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        title = row.get("event_title", "")
        source = row.get("source_name", "")
        description = row.get("event_description", "")
        country = row.get("country_name", "")
        category = row.get("landslide_category", "")
        trigger = row.get("landslide_trigger", "")
        size = row.get("landslide_size", "")
        year = row.get("event_date", "")[:4]   # first 4 chars = year
        fatality = row.get("fatality_count", 0)

        try:
            fatality = int(fatality)
        except:
            fatality = 0

        cur.execute('''
        INSERT INTO Events (title, source, description, country, category, event_trigger, size, year, fatality)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, source, description, country, category, trigger, size, year, fatality))

        count += 1

    print(f"✅ Inserted {count} landslide events into database.")

# Save and close
conn.commit()
conn.close()
