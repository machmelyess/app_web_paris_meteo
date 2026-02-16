from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.environ.get('WEATHER_API_KEY')
    location = "Paris,Île-de-France"
    URL = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    try:
        response = requests.get(URL)
        data = response.json()
        return render_template("index.html", weather=data)
    except Exception as e:
        return f"🛑 Error fetching weather: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)