from flask import Flask, render_template, request
import requests
from assets import config

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city']

        url = f"http://api.weatherapi.com/v1/current.json?key={config.KEY}&q={city_name}"
        response = requests.get(url.format(city_name)).json()

        name = response['location']['name']
        country = response['location']['country']
        temp_c = response['current']['temp_c']
        temp_f = response['current']['temp_f']
        wind_direction = response['current']['wind_dir']
        humidity = response['current']['humidity']
        clouds = response['current']['cloud']
        icon = response['current']['condition']['icon']

        return render_template("city.html", name=name,
        country=country,
        temp_c=temp_c,
        temp_f=temp_f,
        wind_direction=wind_direction,
        humidity=humidity,
        clouds=clouds,
        icon=icon)

    else:

        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)