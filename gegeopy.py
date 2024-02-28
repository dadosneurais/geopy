from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fuck")
texto = input("Digite o dendereço:")
location = geolocator.geocode(texto)
# location = geolocator.reverse("52.509669, 13.376294") <-- pesquisar geolocalização
print(location.address)
print((location.latitude, location.longitude))
# print(location.raw)