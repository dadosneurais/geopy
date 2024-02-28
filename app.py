from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        result = get_location_data(address)
        return jsonify(result=result)

    return render_template('index.html')

def get_location_data(address):
    geolocator = Nominatim(user_agent="your_user_agent")
    location = geolocator.geocode(address)

    if location:
        result = {
            'address': location.address,
            'latitude': location.latitude,
            'longitude': location.longitude
        }
        return result
    else:
        return {'error': 'Endereço não encontrado'}

if __name__ == '__main__':
    app.run(debug=True)
