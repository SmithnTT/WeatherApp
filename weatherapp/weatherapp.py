from flask import Flask, render_template, request
from flask_cors import CORS
from weatherapp_controller import WeatherAppController
import os

import ipinfo

app = Flask(__name__)
CORS(app)

access_token = os.environ['IPINFO_API']

@app.route("/")
def index():

    wapp = WeatherAppController()
    
    ip_address = request.remote_addr
    
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)

    IP = details.ip
    city = details.city
    country = details.country
    region = details.region
    lat = details.latitude
    lon = details.longitude

    print("Your IP detail\n ")
    print("IP : {3} \nRegion : {0} \nCountry : {1} \nCity : {2} \n Latitude: {4} \n Longitude: {5} \n".format(region,country,city,IP,lat,lon))

    text_city = details.city+","+details.country

    return render_template('index.html', text_value=text_city)


@app.route('/current', methods=['POST', 'GET'])
def current():

    if request.method == 'POST':
        
        data = request.json
        input_location = data['location']

        wapp = WeatherAppController()

        geo_location = wapp.getLocation(input_location)
        if geo_location == None:
            wapp_address = "Unknown location"
            report_template = render_template('current.html', weather_address=wapp_address)
            return report_template
       
        city = geo_location['address']['city']
        country = geo_location['address']['country_code']
       
        wapp_address = city+", "+country.upper()
        print(wapp_address)
        wapp_reports = wapp.getWeatherReports(geo_location)

        report_template = render_template('current.html', weather_address=wapp_address, weather_reports=wapp_reports)

    return report_template
    
@app.route('/forecast', methods=['POST', 'GET'])
def forecast():

    if request.method == 'POST':
        
        data = request.json
        input_location = data['location']

        wapp = WeatherAppController()

        geo_location = wapp.getLocation(input_location)
            
        forecast_plot = wapp.getForecastPlot(geo_location)
        
        forecast_template = render_template('forecast.html', forecast_plot=forecast_plot)
        
    return forecast_template

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
