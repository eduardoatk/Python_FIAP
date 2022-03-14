from geopy.geocoders import Nominatim
from Funcoes_JSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent = "wazeyes")  # Nome do seu aplicativo
dicionario = ler_arquivo("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + "," + lista[1] + "," + lista[2]
location = geolocator.geocode(endereco)
saida = {"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida, "saida.json")
