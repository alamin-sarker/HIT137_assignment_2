import requests

class Geocode: 
    def __init__(self):
        self.API_KEY = "AIzaSyB4KZkzjMoyfx0w2jIq-xk9uIbGeIwehn8" 
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # default address -> "1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyB4KZkzjMoyfx0w2jIq-xk9uIbGeIwehn8
    def get_coordinates_from_address(self, address="NT"):
        response = self.__get_geocode_api_response(address) 
        
        try:
            self.__validate_api_response(response)
        except Exception as e:
            raise e      

        latitude, longitude = self.__get_coordinates_from_response(response)
        return latitude, longitude


    def __get_geocode_api_response(self, address): 
        url = f"{self.base_url}?address={address}&key={self.API_KEY}"
        response = requests.get(url).json()

        return response

    
    def __validate_api_response(self, response): 
        if response['status'] == 'OK': 
            print("[GEOCODE] The API response was successful. ") 
        else: 
            error_message = response['error_message']
            raise Exception(f"[GEOCODE] ERROR: {error_message}")


    def __get_coordinates_from_response(self, response): 
        latitude = response['results'][0]['geometry']['location']['lat']
        longitude = response['results'][0]['geometry']['location']['lng']
        # print("[GEOCODE] Latitude: " + latitude + "\tLongitude: " + longitude)

        return latitude, longitude