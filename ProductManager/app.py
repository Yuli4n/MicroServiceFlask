from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import Config
from models import db
import locale

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

db.init_app(app)

# Configurar la localización para el formato de moneda
locale.setlocale(locale.LC_ALL, '')

# Definir el filtro personalizado
@app.template_filter('currency')
def currency_filter(value):
    return locale.currency(value, grouping=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    email = request.form.get('email')
    print(f"Searching for email: {email}")  # Imprimir el correo electrónico buscado
    query = """
    SELECT financial_products.product_name, financial_products.quota
    FROM customers
    JOIN financial_products ON customers.id = financial_products.customer_id
    WHERE customers.email = :email
    """
    results = db.session.execute(query, {'email': email}).fetchall()
    print(f"Products found: {results}")  # Imprimir los productos encontrados
    return render_template('index.html', products=results, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
