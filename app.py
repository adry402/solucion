from flask import Flask, jsonify

app = Flask(__name__)

# Entregar datos
from products import products

#Ruta de prueba
# Visita la ruta desde el navegador va a la funcion pong
#Proceso de testeo, para ver si el server responde

@app.route('/ping')
def ping():
    return jsonify({"message": "hola"})

@app.route('/products')
def getProducts():
    return jsonify ({"products": products, "message": "Product list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    products_Found = [product for product in products if product['name']== product_name]
    if len(products_Found) > 0:
        return jsonify(products_Found[0])
    else:
        return jsonify({"message": "Product not found"})



if __name__ == "__main__":
    app.run(debug=True, port = 4000)