# Carrito de compras 

product = {
    "name":"book",
    "quantity":3,
    "price":4.99
}

person = {
    "firstName": "Agustina",
    "lastName": "Perez"
}

# print(type(person)) # me muestra el tipo de dato que es mi variable person
# print(dir(person)) # me muestra los metodos que tiene mi dict

print(person.items())
print(person.keys())

products = [
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 1000}
]

print(products)