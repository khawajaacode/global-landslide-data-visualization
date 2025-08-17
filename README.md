
# Global Landslides Analysis Project

This project analyzes a comprehensive dataset of global landslide events, providing visualizations and insights into landslide occurrences and fatalities worldwide. The analysis includes data processing, database management, and interactive visualizations.

## Features

- **Database Creation**: Processes CSV data into an SQLite database for efficient querying
- **Basic Statistics**: Generates country-wise statistics for landslide events and fatalities
- **Interactive Visualizations**:
  - Word Cloud visualization of landslide fatalities by country
  - Line chart showing temporal distribution of landslide events

## Project Structure

```
project/
├── basic_output_data.py      # Generates basic statistics from the database
├── deaths_word_cloud.py      # Creates word cloud visualization for fatalities
├── events_line_chart.py      # Generates line chart for event distribution
├── landslide_loads.py        # Processes CSV data into SQLite database
├── landslides.csv           # Raw dataset
├── d3.layout.cloud.js       # D3.js word cloud library
├── d3.v2.js                # D3.js visualization library
├── deaths_word_cloud.htm    # Word cloud visualization interface
└── events_line_chart.htm    # Line chart visualization interface
```

## Setup Instructions

1. Clone the repository
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Run the scripts in order:
```bash
python landslide_loads.py         # Create database
python basic_output_data.py       # Generate statistics
python deaths_word_cloud.py       # Create word cloud
python events_line_chart.py       # Create line chart
```

5. View the visualizations by opening in a web browser:
   - `deaths_word_cloud.htm`
   - `events_line_chart.htm`

## Example Outputs

### Landslide Events Word Cloud
[Word Cloud Visualization showing frequency of landslide events by country]

### Events Timeline
[Line Chart showing distribution of landslide events over time]

### Sample Statistics
```
Top countries by landslide events:
1. United States (2992 events)
2. India (1265 events)
3. Philippines (675 events)

Top countries by fatalities:
1. India (7069 fatalities)
2. China (4945 fatalities)
3. Afghanistan (2294 fatalities)
```

## Dataset Source

The dataset used in this project is sourced from NASA's Global Landslide Catalog (GLC). It contains comprehensive information about landslide events worldwide, including:
- Event location and date
- Trigger factors
- Impact (fatalities, injuries)
- Size and category of landslides
- Source documentation

## Author

This project was developed as part of the Python for Everybody specialization capstone project. It demonstrates skills in:
- Data processing and analysis
- Database management with SQLite
- Data visualization with D3.js
- Python programming
In this Capstone project you are required  to select, process, and visualize the data of your choice.
The data choosen was the "Global Landslide Data" by NASA's Open Data Portal.

>The Global Landslide Catalog (GLC) was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources.
https://data.nasa.gov/Earth-Science/Global-Landslide-Data-Export-Visual-Explorer/angv-aquq

From this data set  various informations about lnadslide events occurred in the period of time from 2006 to 2016 could be retrieved.Informations such as event's date,trigger, location, number of injuries and fatalities,size and ect.
With this data,the countries most affected by landslide accidents will be compared and the results will be visualised in chart graphs.
### Scripts and Process
#### landslide_loads.py
* get data of landslide events in JSON format via Socrata Open Data API
* parse the data and store it in "landslide-data" database
#### basic_output_data.py
* retrieve data from "landslide-data"
* output the list of countries sorted by the number of landslide events
* output the list of countries sorted by the number of fatalities caused by landslide events
#### deaths_word_cloud.py
* retrieve data from "landslide-data"
* write a JavaScript file with countries fatalities count releated text size, this file is to be used to visualize the number of deaths per countriy in a word cloud graph
* after running deaths_word_cloud.py, a "deaths_word_cloud.js" file will be created and would be used to visualize data with the help of D3.js library 
* run the "deaths_word_cloud.htm" to visualize data
#### events_line_chart.py
* retrieve data from "landslide-data"
* write in a JavaScript file the events count in each country per year , this file is to be used to visualize the number of deaths per countriy in a line chart graph.
* after running events_line_chart.py, a "events_line_chart.js" file will be created and would be used to visualize data with the help of D3.js library.
* run the "events_line_chart.htm" to visualize data
### Sources
[Global Landslide Data](https://data.nasa.gov/Earth-Science/Global-Landslide-Data-Export-Visual-Explorer/angv-aquq)

[NASA's Open Data Portal](https://data.nasa.gov/)

[Coursera](https://www.coursera.org/)

[Capstone Project Certificate](https://www.coursera.org/share/68c8c9c5b22d91891d48bd34780c7557)
