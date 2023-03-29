from flask import Flask, render_template, request
import requests
from assets import config
from datetime import datetime 

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            city_name = request.form['city']

            url = f"http://api.weatherapi.com/v1/forecast.json?key={config.KEY}&q={city_name}"
            response = requests.get(url.format(city_name)).json()

            name = response['location']['name']
            region = response['location']['region']
            temp_c = response['current']['temp_c']
            wind_speed = response['current']['wind_kph']
            wind_direction = response['current']['wind_dir']
            humidity = response['current']['humidity']
            clouds = response['current']['cloud']
            text = response['current']['condition']['text']
            icon = response['current']['condition']['icon']
            vis_km = response['current']['vis_km']
            uv = response['current']['uv']
            time = datetime.now()

            return render_template("city.html", name=name,
            region=region,
            temp_c=temp_c,
            wind_direction=wind_direction,
            humidity=humidity,
            clouds=clouds,
            icon=icon,
            time=time,
            wind_speed=wind_speed,
            vis_km=vis_km,
            text=text,
            uv=uv)

        except KeyError as k:

            return render_template("index.html")
    else:

        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)