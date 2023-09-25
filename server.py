from jinja2 import Environment
from jinja2 import FileSystemLoader
# hay que instalarlos con pipenv install Jinja2

from wsgiref.simple_server import make_server


def application(env, start_response):
    headers= [ ('content-Type',  'text/html') ]

    start_response('200 ok', headers)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    HTML = template.render(
        {
            "title": "Servidor en Python",
            "name" : "santiago sierra"
        }
    )

    return [bytes(HTML, 'utf-8')]

# esta funcion recibe por obligacion 3 argumentos
# 1- direccion donde se ejecutara
# 2- puerto donde escuchara
# 3- funcion encargada de responder
server = make_server('localhost', 8000, application)
server.serve_forever() # con esto se ejecuta hasta que explicitamente lo detengamos 

# https://t.me/joinchat/AAAAAEsAMARfQ2-ooVZHog
# https://t.me/joinchat/AAAAAEsAMARfQ2-ooVZHog

# pip install Jinja2

