from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User, Product
from . import db
import logging
from flask import current_app, session

routes = Blueprint('routes', __name__)

def add_products():
    # Verificar si ya existen productos en la base de datos
    if not Product.query.first():  # Solo agrega productos si no hay ninguno en la base de datos
        product1 = Product(name="Zapatilla Sport", description="Comodidad y estilo en un solo calzado.", price=200000, image="img/zapatilla1.jpg")
        product2 = Product(name="Zapatilla Running", description="Ideales para tus entrenamientos.", price=119000, image="img/zapatilla2.jpg")
        product3 = Product(name="Zapatilla Casual", description="Perfectas para el día a día.", price=69000, image="img/zapatilla3.jpg")
        product4 = Product(name="Zapatilla Deportiva", description="Ligereza y durabilidad garantizadas.", price=90000, image="img/zapatilla4.jpg")

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)
        db.session.commit()

@routes.route('/')
def home():
    try:
        add_products()
        products = Product.query.all()
        current_app.logger.info(f"[DEBUG] Productos en home(): {len(products)}")

        return render_template('index.html', products=products)
    except Exception as e:
        print(f"ERROR en home(): {e}")
        return "Error cargando productos"

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id          # <-- esto guarda la sesión
            flash(f"Bienvenido, {user.email}!")
            print(f"Inicio de sesión del usuario: {email}, {password}")
            return redirect(url_for('routes.home'))
        else:
            flash('Usuario o contraseña incorrectos.')
            return render_template('login.html')
    return render_template('login.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('El correo ya está registrado.')
            return redirect(url_for('routes.signup'))

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Cuenta creada correctamente. Ahora haz login.')
        user = User.query.filter_by(email=email).first()
        if user:
            print(f"Usuario creado: {user.email}, {user.password}")
        else:
            print("Error al crear el usuario.")
        print(f"Usuario guardado: {user.email}")
        return redirect(url_for('routes.login'))
    return render_template('signup.html')
@routes.route('/producto/<int:product_id>')
def producto(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('producto.html', product=product)
@routes.route('/productos')
def products_list():
    add_products()            # si quieres poblarlos aquí
    products = Product.query.all()
    return render_template('index.html', products=products)
@routes.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión.')
    return redirect(url_for('routes.home'))

