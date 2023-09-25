from urllib import request


URL = 'http://localhost:8000/'

response = request.urlopen(URL)
# print(response.__dict__) # accedemos a los atributos
print(response.read()) #obtener e imprimir todo el contenido de la respuesta del servidor
