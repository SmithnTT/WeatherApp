class WeatherReport():
    def __init__(self, date, curr_temp, max_temp, 
                min_temp, summary, icon, wind, hum, sunrise, sunset):
        self.date = date
        self.curr_temp = curr_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.summary = summary   
        self.icon = icon
        self.wind = wind
        self.hum = hum
        self.sunrise = sunrise
        self.sunset = sunset