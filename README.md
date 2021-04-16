# WeatherApp
A simple weather web application using python

## Requirements
 - Python installed
 - Python packages:
	- flask
	- flask-cors
	- requests
	- geopy
	- ipinfo
	- plotly
	- chart-studio

## Quick start
$cd weatherapp

$export OPENWEATHER_API={your openweatherapi key}  - https://openweathermap.org/api

$export IPINFO_API={your ipinfo key} - https://ipinfo.io/developers

$export FLASK_APP=./weatherapp.py

$export FLASK_ENV=development

$python -m flask run --host=0.0.0.0