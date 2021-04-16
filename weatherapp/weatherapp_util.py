import datetime
import json
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go


class WeatherUtils:
    
    def create_plot(self, xScale, yScale, y2Scale):
        trace1 = go.Scatter(
            x = xScale,
            y = yScale,
            mode = 'lines',
            name = 'Temperature ºC'
        )
        
        trace2 = go.Scatter(
            x = xScale,
            y = y2Scale,
            mode = 'lines',
            name = 'Rain chance %'
        )
        
        data = [trace1, trace2]
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        
        return graphJSON
        
    def getHourFormatted(self, utcTime, strOffset):
        offset = int(strOffset)
        epoch_time = utcTime+offset
        
        dt = datetime.datetime.fromtimestamp(epoch_time)
        hourForm = str(dt.time())[0:5]
        
        return hourForm