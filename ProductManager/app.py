from flask import Flask
from config import Config
from models import db, Customer, FinancialProduct

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    return "Welcome to the Financial Products Service!"

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    products = FinancialProduct.query.filter_by(customer_id=id).all()
    return {
        'name': customer.name,
        'email': customer.email,
        'products': [{'product_name': p.product_name, 'balance': p.balance} for p in products]
    }

if __name__ == '__main__':
    app.run(debug=True)
