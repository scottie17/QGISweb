import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import jieba

# Define the cities we're interested in
cities = ['南京', '蘇州', '杭州', '北京', '揚州', '濟南', '湖州']


def scrape_rulin_waishi():
    # Base URL for The Scholars on ctext.org
    base_url = 'https://ctext.org/rulin-waishi/zh'
    chapters_data = []

    # Headers to mimic browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and process each chapter
        for chapter in range(1, 21):  # Processing first 20 chapters
            chapter_url = f'{base_url}/{chapter}'
            chapter_response = requests.get(chapter_url, headers=headers)
            chapter_soup = BeautifulSoup(chapter_response.text, 'html.parser')

            # Extract chapter text
            text = chapter_soup.find('div', class_='text').get_text()

            # Count city occurrences
            city_counts = {city: text.count(city) for city in cities}
            city_counts['chapter'] = chapter

            chapters_data.append(city_counts)

    except Exception as e:
        print(f"Error occurred: {e}")

    return pd.DataFrame(chapters_data)


# Process the data
df = scrape_rulin_waishi()

# Save to CSV
df.to_csv('rulin_waishi_cities.csv', index=False)

# Create location data with coordinates
locations = {
    '南京': {'lat': 32.0603, 'lon': 118.7969},
    '蘇州': {'lat': 31.2989, 'lon': 120.5853},
    '杭州': {'lat': 30.2741, 'lon': 120.1551},
    '北京': {'lat': 39.9042, 'lon': 116.4074},
    '揚州': {'lat': 32.3947, 'lon': 119.4142},
    '濟南': {'lat': 36.6512, 'lon': 117.1201},
    '湖州': {'lat': 30.8927, 'lon': 120.0881}
}

# Create GeoJSON format data
geojson_data = {
    "type": "FeatureCollection",
    "features": []
}

for city, coords in locations.items():
    city_total = df[city].sum()
    feature = {
        "type": "Feature",
        "properties": {
            "name": city,
            "count": int(city_total)
        },
        "geometry": {
            "type": "Point",
            "coordinates": [coords['lon'], coords['lat']]
        }
    }
    geojson_data["features"].append(feature)

# Save GeoJSON
import json

with open('city_locations.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=2)