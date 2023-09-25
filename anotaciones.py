variable_a = "hola mundo"
print(variable_a)

variable_a = 3.1415
print(variable_a)

# anotaciones de tipo 
# permiten indicar que tipo de dato tendra nuestra variable

# str indica que es stirng
a: str = 'hola, esto es un string'
b: int = 30
c: float = 3.14
d: bool = True

# indicamos tipos para los parametros y con -> el valor que retorna la funcion
def suma(numero1: int, numero2:int) -> int:
    return numero1 + numero2

valor1: int = 10
valor2: int = 20

resultado: int = suma(valor1, valor2)
print(resultado)

# si no queremos asignar un valor pero si su tipo
valor3: int


class User():

    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password
    
    def saluda(self) -> str:
        return f'Hola {self.username}'
    

cody = User('Cody', '123')

print(cody.saluda())


###-----------------listas-----------------###
from typing import List

calificaciones: List[int] = [ 10, 9, 5, 5, 7, 9, 9 ]

def promedio(calificaciones: List[int]) -> float:
    return sum(calificaciones) / len(calificaciones)

print(promedio(calificaciones))

###----------------tupla-----------------------##
from typing import Tuple
configuraciones: Tuple[str] = ('localhost', '3306', 'root')

print(configuraciones)


###-----------------Union---------------------------##
from typing import Union

config: Tuple[Union[str, str, bool, int]] = ('root', 'localhost', 3306, True)
print(config)

###-----------------diccionario----------------------------###
from typing import Dict

# llave string : valor entero
usuarios: Dict[str, int] = {
    'eduardo': 10,
    'cody': 10
}
print(usuarios)




###-------------------------Pydantic----------------------------------###
# pipenv install pydantic
from pydantic import BaseModel
from typing import Optional

# esta extension de la clase se encarga de recibir siempre el tipo de dato que le indicamos
class User(BaseModel):
    username: str # al indicarlos aqui decimos que son requeridos
    password:str
    email: str
    age: Optional[int] = None # con el Optional ya no es obligatorio

user1 = User(
    username='eduardo',
    password='123',
    email='info@codigofacilito.com',
    age=10
)
print(user1)






