from pprint import pprint

import streamlit as st
import requests as re

DEMO_KEY = "dgWJ3KrG1vj8qhSyIUFqUAlapjzrePRwlIEnshFh"

NASA_URL = f"https://api.nasa.gov/planetary/apod?api_key={DEMO_KEY}"

# Get the data as dictionary
response = re.get(NASA_URL)
data = response.json()

# Extracting the image title, date, description and url
title = data["title"]
date = data["date"]
image_url = data["url"]
description = data["explanation"]

# Downloading the image
image_filepath = "image.jpg"
with open(image_filepath, "wb") as image_file:
    image_file.write(re.get(image_url).content)

st.title(title)
st.subheader(date)
st.image(image_filepath)
st.write(description)