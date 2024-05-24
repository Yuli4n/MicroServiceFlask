from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import Config
from models import db, Customer, FinancialProduct

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    email = request.form.get('email')
    customer = Customer.query.filter_by(email=email).first()
    products = []
    if customer:
        products = FinancialProduct.query.filter_by(customer_id=customer.id).all()
    return render_template('index.html', products=products, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
