from pygeocoder import Geocoder

endereco = input("Digite um endereco com número e cidade. "
                 "Exemplo: 100, avenida paulista, Sao Paulo, SP: ")
resultado = (Geocoder('AIzaSyDGzl5O7AJfb14zAFDRJzU_NYVdhyUn7Uk').geocode(endereco).coordinates)

print(resultado)
