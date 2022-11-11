import requests 
from Geocode import Geocode

class Weather: 
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "b9ae805fd470d789469e26f46158619e"
    latitude = None
    longitude = None

    def __init__(self):
        geocode = Geocode()
        # address = "1600+Amphitheatre+Parkway,+Mountain+View,+CA"
        address = "fasdajghsdghja"
        self.latitude, self.longitude = geocode.get_coordinates_from_address(address)

    # https://api.openweathermap.org/data/2.5/weather?lat=37.4226618&lon=-122.0829302&appid=b9ae805fd470d789469e26f46158619e
    def get_weather_api_data(self): 
        request_url = f"{self.BASE_URL}?lat={self.latitude}&lon={self.longitude}&appid={self.API_KEY}"
        response = requests.get(request_url)
        # data = response.json()

        if response.status_code == 200: 
            print("[WEATHER] The API response was succcessful")
            return response.json()
        else: 
            # TODO: Return the error code and error message
            raise Exception("[WEATHER] ERROR: The API response was unsuccessful")

w = Weather() 
data= w.get_weather_api_data()
print(data)