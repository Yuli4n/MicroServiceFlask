from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

db.init_app(app)

# Definir el filtro personalizado para formatear como COP
@app.template_filter('currency')
def currency_filter(value):
    return f"${value:,.0f}".replace(",", ".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    dni = request.form.get('dni')
    print(f"Searching for dni: {dni}")  # Imprimir el correo electrónico buscado
    query = """
    SELECT customers.name, financial_products.product_name, financial_products.quota
    FROM customers
    JOIN financial_products ON customers.id = financial_products.customer_id
    WHERE customers.dni = :dni
    ORDER BY financial_products.quota
    """
    results = db.session.execute(query, {'dni': dni}).fetchall()
    print(f"Products found: {results}")  # Imprimir los productos encontrados
    customer_name = results[0][0] if results else None  # Obtener el nombre del cliente
    return render_template('index.html', products=results, dni=dni, customer_name=customer_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
