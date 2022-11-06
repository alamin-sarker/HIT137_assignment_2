import requests

class Geocode: 
    API_KEY = "AIzaSyB4KZkzjMoyfx0w2jIq-xk9uIbGeIwehn8" 
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinates_from_address(self, address="1600+Amphitheatre+Parkway,+Mountain+View,+CA"):
        response = self.__get_geocode_api_response(address) 
        
        try:
            self.__validate_api_response(response)
        except:     
            # TODO: Return the error code and error message
            print("[GEOCODE] ERROR: The API response was unsuccessful")
            return 0, 0

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
            raise Exception("[GEOCODE] ERROR: The API response was unsuccessful")


    def __get_coordinates_from_response(self, response): 
        latitude = response['results'][0]['geometry']['location']['lat']
        longitude = response['results'][0]['geometry']['location']['lng']
        # print("[GEOCODE] Latitude: " + latitude + "\tLongitude: " + longitude)

        return latitude, longitude