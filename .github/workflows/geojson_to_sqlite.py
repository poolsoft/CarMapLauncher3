import json
import sqlite3
import sys

geojson_path = 'pois.geojson'
db_path = 'pois.sqlite'

with open(geojson_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS poi_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    latitude REAL,
    longitude REAL
)''')

for feature in data['features']:
    props = feature['properties']
    coords = feature['geometry']['coordinates']
    name = props.get('name', '')
    ptype = props.get('type', '')
    lon, lat = coords
    c.execute("INSERT INTO poi_table (name, type, latitude, longitude) VALUES (?, ?, ?, ?)",
              (name, ptype, lat, lon))
conn.commit()
conn.close()
