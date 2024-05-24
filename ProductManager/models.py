from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    financial_products = db.relationship('FinancialProduct', backref='customer', lazy=True)

class FinancialProduct(db.Model):
    __tablename__ = 'financial_products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False)  # Asegúrate de que el nombre del campo coincide
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
