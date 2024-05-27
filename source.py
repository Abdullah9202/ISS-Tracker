import requests

# ------------------- Request to ISS ------------------- #
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # It will raise an exception error if something went wrong
# Getting the json data
# data = response.content # It can also be used to get json data

# Getting the ISS position
data1 = response.json()["iss_position"] # It's a dict

# Getting the latitude and longitude separately
iss_Lattitude = response.json()["iss_position"]["longitude"]
iss_Longitude = response.json()["iss_position"]["latitude"]
# Creating a tuple
iss_Position = (iss_Lattitude, iss_Longitude)
print(iss_Position)
