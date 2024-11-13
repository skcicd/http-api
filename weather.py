from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '6a7b6ef9f8ef66e56e652f0ced597697'  # API ключ OpenWeatherMap

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'Город не найден'}

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
