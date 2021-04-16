from weatherapp_model import WeatherReport
from weatherapp_util import WeatherUtils
from geopy.geocoders import Nominatim
from datetime import datetime
import requests, os
 
ow_api_key = os.environ['OPENWEATHER_API']
 
class WeatherAppController:
 
    def getLocation(self, input_location):
        location = Nominatim(user_agent="weatherApp").geocode(input_location, language='en_US', addressdetails=True)
       
        return location.raw
 
    def getWeatherReports(self, location):
        weather_reports = []
                
        wUtil = WeatherUtils()
 
        latitude = str(location['lat'])
        longitude = str(location['lon'])
 
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+latitude+"&lon="+longitude+"&exclude=minutely,alerts&units=metric&appid="+ow_api_key)
        json_res = response.json()
        
        today = datetime.today()
        str_date = today.strftime("%B %d")
        week_day = datetime.today().strftime('%A')     
        report_date = week_day+", "+str_date
        
        curr_temp = round(json_res['current']['temp'])
        min_temp = round(json_res['daily'][0]['temp']['min'])
        max_temp = round(json_res['daily'][0]['temp']['max']) 
        summary = json_res['current']['weather'][0]['main']
        wind = round(json_res['current']['wind_speed'])
        hum = json_res['current']['humidity']
        icon = json_res['current']['weather'][0]['icon']
        
        sunrise = wUtil.getHourFormatted(json_res['current']['sunrise'], str(json_res['timezone_offset']))
        sunset = wUtil.getHourFormatted(json_res['current']['sunset'], str(json_res['timezone_offset']))
        
        ezw_wr = WeatherReport(report_date, curr_temp, max_temp, min_temp, summary, icon, wind, hum, sunrise, sunset)
 
        weather_reports.append(ezw_wr)
 
        return weather_reports
        
    def getForecastPlot(self, location):
        
        hour_x = []
        rain_y = []
        temp_y = []
        
        wUtil = WeatherUtils()
        
        latitude = str(location['lat'])
        longitude = str(location['lon'])
 
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+latitude+"&lon="+longitude+"&exclude=current,daily,minutely,alerts&units=metric&appid="+ow_api_key)
        json_res = response.json()
        
        hourly = json_res['hourly']
        
        for hourData in hourly:
            formHour = wUtil.getHourFormatted(hourData['dt'], str(json_res['timezone_offset']))
            
            temp = round(hourData['temp'])
            rain_pop = hourData['pop']*100
                      
            hour_x.append(formHour)
            rain_y.append(rain_pop)
            temp_y.append(temp)
            
        forecast_plot = wUtil.create_plot(hour_x, temp_y, rain_y)
        
        return forecast_plot
        
        