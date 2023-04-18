import streamlit as st
import requests
import pandas as pd
import numpy as np

st.title("ISS info")
pos_iss = requests.get("http://api.open-notify.org/iss-now.json")
lleison_iss = pos_iss.json()
st.json(lleison_iss)
st.table(lleison_iss)
st.write("Latitud:",lleison_iss["iss_position"]["latitude"])
st.write("Longitud:",lleison_iss["iss_position"]["longitude"])
lati = lleison_iss["iss_position"]["latitude"]
longi = lleison_iss["iss_position"]["longitude"]
posicion = f"https://maps.google.com/?q={lati},{longi}"
st.write(posicion)
st.write(lati)
st.write(longi)
sitio = [lati,longi]
sitios = []
sitios.append(sitio)
sitios_df = pd.DataFrame(sitio,columns=[lat,lon])
st.map(sitios_df)
