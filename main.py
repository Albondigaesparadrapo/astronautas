import streamlit as st
import requests

st.title("ISS info")

# Obtener la posición actual de la ISS
pos_iss = requests.get("http://api.open-notify.org/iss-now.json")
pos_iss_dict = pos_iss.json()
st.write("Latitud:", pos_iss_dict["iss_position"]["latitude"])
st.write("Longitud:", pos_iss_dict["iss_position"]["longitude"])

# Crear una URL de Google Maps con las coordenadas de la ISS
lati = pos_iss_dict["iss_position"]["latitude"]
longi = pos_iss_dict["iss_position"]["longitude"]
map_url = f"https://www.google.com/maps/search/?api=1&query={lati},{longi}"
st.write("Ubicación en Google Maps:", map_url)

# Mostrar un mapa con las coordenadas de la ISS
st.map({"lat": lati, "lon": longi})
