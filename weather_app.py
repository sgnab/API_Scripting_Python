import urllib2
import json
import requests
"""a simple script to start developing a weather app
you can change the app to search based on zip code, you can extract more details information
In order to use the script you must create a free account with openweathermap.org and get an API
Again this is a starting point of an APP and far from a complete app
feel free to use the code"""
class Main_class:
    # city=raw_input("your city")
    def __init__(self, api, city):

        self.api=api
        self.city=city
        self.city=raw_input("your city: ")

    def json_data(self):

        url='http://api.openweathermap.org/data/2.5/weather?q='+self.city+'&appid='+self.api+''
        obj=requests.get(url)

        #just for print whole data for further development

        # print obj.text
        json_obj=obj.json()
        #here you can pull out more information such as: summary, Humidity,....
        temp_k, wind_speed = "temperature " + "=" + str((json_obj['main']['temp'])-273.15)+" C", "wind speed =" + str(json_obj['wind']['speed'])
        return temp_k, wind_speed
    # the following class does nothing it is for further development so you can create a class to get zip code instead of city name
class Data_city(Main_class):

    def __init__(self,api, city):
        Main_class.__init__(self,api, city)


Result=Data_city('your API here',"city")
print Result.json_data()





