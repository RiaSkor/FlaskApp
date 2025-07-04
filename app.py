from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml, os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
import re

app = Flask(__name__)
Bootstrap(app)
CKEditor(app)

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = os.urandom(24)
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/about2')
def about2():
    return render_template('about2.html')


# @app.route('/products/')
# def listproducts():
#     return render_template('products.html')

@app.route('/products2')
def listproducts2():
    return render_template('products2.html')


# @app.route('/register2', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         user_details = request.form

#         # Проверка на пустые поля
#         if not user_details['surname_client'] or not user_details['name_client'] or not user_details['email'] or not user_details['password']:
#             flash('Пожалуйста, заполните все обязательные поля', 'danger')
#             return render_template('register2.html')

#         if user_details['password'] != user_details['confirmpassword']:
#             flash('Пароль неправильный. Попробуйте снова', 'danger')
#             return render_template('register2.html')

#         password = user_details['password']
#         if not validate_password(password):
#             flash('Пароль должен содержать минимум 8 символов, включая 1 строчную букву, 1 заглавную букву, 1 цифру и 1 специальный символ.', 'danger')
#             return render_template('register2.html')

#         cursor = mysql.connection.cursor()
#         cursor.execute("INSERT INTO clients(surname_client, name_client, patronymic_client, email, password) VALUES (%s, %s, %s, %s, %s)",
#                        (user_details['surname_client'], user_details['name_client'], user_details['patronymic_client'], user_details['email'], generate_password_hash(user_details['password'])))
#         mysql.connection.commit()
#         cursor.close()
#         flash('Регистрация пройдена успешно', 'success')
#         return redirect('/login2')
    
#     return render_template('register2.html')


@app.route('/register2', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_details = request.form

        # Проверка на пустые поля
        if not user_details['surname_client'] or not user_details['name_client'] or not user_details['email'] or not user_details['password']:
            flash('Пожалуйста, заполните все обязательные поля', 'danger')
            return render_template('register2.html', user_details=user_details)
        
        # Проверка уникальности email
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM clients WHERE email = %s", (user_details['email'],))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Этот email уже зарегистрирован. Пожалуйста, используйте другой email.', 'danger')
            return render_template('register2.html', user_details=user_details)

        # Проверка на соответствие паролей
        if user_details['password'] != user_details['confirmpassword']:
            flash('Пароли не совпадают. Попробуйте снова', 'danger')
            return render_template('register2.html', user_details=user_details)

        # Проверка на соответствие условиям пароля
        password = user_details['password']
        if not validate_password(password):
            flash('Пароль должен содержать минимум 8 символов, включая 1 строчную букву и 1 заглавную букву на EN регистре, 1 цифру и 1 специальный символ.', 'danger')
            return render_template('register2.html', user_details=user_details)

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO clients(surname_client, name_client, patronymic_client, email, password) VALUES (%s, %s, %s, %s, %s)",
                       (user_details['surname_client'], user_details['name_client'], user_details['patronymic_client'], user_details['email'], generate_password_hash(password)))
        mysql.connection.commit()
        cursor.close()
        flash('Регистрация пройдена успешно', 'success')
        return redirect('/login2')

    return render_template('register2.html', user_details={})



def validate_password(password):
    # Проверка на минимальную длину
    if len(password) < 8:
        return False
    # Проверка на наличие строчной буквы
    if not re.search(r"[a-z]", password):
        return False
    # Проверка на наличие заглавной буквы
    if not re.search(r"[A-Z]", password):
        return False
    # Проверка на наличие цифры
    if not re.search(r"[0-9]", password):
        return False
    # Проверка на наличие специального символа
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


@app.route('/login2', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_details = request.form
        email = user_details['email']
        cursor = mysql.connection.cursor()
        result_value = cursor.execute("SELECT * FROM clients WHERE email = %s", ([email]))
        if result_value > 0:
            clients = cursor.fetchone()
            if check_password_hash(clients['password'], user_details['password']):
                session['login'] = True
                session['name_client'] = clients['name_client']
                session['surname_client'] = clients['surname_client']
                flash('Добро пожаловать, ' + session['name_client'] + '!', 'success')
            else:
                cursor.close
                flash('Неверный пароль, попробуйте снова', 'danger')
                return render_template('login2.html')
        else:
            cursor.close()
            flash('Неверный логин, попробуйте снова', 'danger')
            return render_template('login2.html')
        cursor.close()        

        return redirect('/')
    return render_template('login2.html')

@app.route('/register_admin2', methods=['GET', 'POST'])
def register_admin():
    if request.method == 'POST':
        user_details = request.form

        # Проверка на пустые поля
        if not user_details['surname_staff'] or not user_details['name_staff'] or not user_details['login_staff'] or not user_details['password_staff']:
            flash('Пожалуйста, заполните все обязательные поля', 'danger')
            return render_template('register_admin2.html', user_details=user_details)        

         # Проверка уникальности login
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM staff WHERE login_staff = %s", (user_details['login_staff'],))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Этот логин уже зарегистрирован. Пожалуйста, используйте другой логин.', 'danger')
            return render_template('register_admin2.html', user_details=user_details)

        # Проверка на соответствие условиям пароля
        password_staff = user_details['password_staff']
        if not validate_password_staff(password_staff):
            flash('Пароль должен содержать минимум 8 символов, включая 1 строчную букву и 1 заглавную букву на EN регистре, 1 цифру и 1 специальный символ.', 'danger')
            return render_template('register_admin2.html', user_details=user_details)        

        # Проверка на соответствие паролей
        if user_details['password_staff'] != user_details['confirmpassword']:
            flash('Пароли не совпадают. Попробуйте снова', 'danger')
            return render_template('register_admin2.html', user_details=user_details)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO staff(surname_staff, name_staff, patronymic_staff, login_staff, password_staff, id_roles) VALUES (%s, %s, %s, %s, %s, %s)",
                       (user_details['surname_staff'], user_details['name_staff'], user_details['patronymic_staff'], user_details['login_staff'], generate_password_hash(user_details['password_staff']), user_details['id_roles']))
        mysql.connection.commit()
        cursor.close()
        flash('Регистрация пройдена успешно', 'success')
        
    return render_template('register_admin2.html', user_details={})


def validate_password_staff(password_staff):
    # Проверка на минимальную длину
    if len(password_staff) < 8:
        return False
    # Проверка на наличие строчной буквы
    if not re.search(r"[a-z]", password_staff):
        return False
    # Проверка на наличие заглавной буквы
    if not re.search(r"[A-Z]", password_staff):
        return False
    # Проверка на наличие цифры
    if not re.search(r"[0-9]", password_staff):
        return False
    # Проверка на наличие специального символа
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password_staff):
        return False
    return True


@app.route('/logadmin2', methods=['GET', 'POST'])
def logadmin():
    if request.method == 'POST':
        staff_details = request.form
        login_staff = staff_details['login_staff']
        # id_roles = staff_details['id_roles']
        cursor = mysql.connection.cursor()
        result_value = cursor.execute("SELECT * FROM staff WHERE login_staff = %s", ([login_staff]))
        if result_value > 0:
            staff = cursor.fetchone()
            if check_password_hash(staff['password_staff'], staff_details['password_staff']):
                session['login'] = True
                session['id_roles'] = staff['id_roles']
                session['login_staff'] = staff['login_staff']
                session['surname_staff'] = staff['surname_staff']
                flash('Сессия сотрудника ' + session['surname_staff'] + ' - активна', 'success')
            else:
                cursor.close
                flash('Неверный пароль, попробуйте снова', 'danger')
                return render_template('logadmin2.html')
        else:
            cursor.close()
            flash('Неверный логин, попробуйте снова', 'danger')
            return render_template('logadmin2.html')
        cursor.close()        

        return redirect('/')
    return render_template('logadmin2.html')

@app.route('/logout/')
def logout():
    session.clear()
    flash('Вы успешно вышли', 'info')
    return redirect('/')


@app.route('/lacquer2')
def lacquer():
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT id_product, name_product, name_type_material, name_type_coloring_agent, name_color, name_gloss, name_method_application, price, volume FROM products JOIN type_material ON products.id_type_material = type_material.id_type_material JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent JOIN type_color ON products.id_type_color = type_color.id_type_color JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE id_categories = 1 GROUP BY id_product ORDER BY 1 ASC")
    if result_value > 0:
        products = cursor.fetchall()
        cursor.close()
        return render_template("lacquer2.html", products=products)
    return render_template("lacquer2.html", products=None)

    #return render_template('lacquer.html')

@app.route('/paints2')
def paints():
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT id_product, name_product, name_type_material, name_type_coloring_agent, name_color, name_gloss, name_method_application, price, volume FROM products JOIN type_material ON products.id_type_material = type_material.id_type_material JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent JOIN type_color ON products.id_type_color = type_color.id_type_color JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE id_categories = 2 GROUP BY id_product ORDER BY 1 ASC")
    if result_value > 0:
        products = cursor.fetchall()
        cursor.close()
        return render_template("paints2.html", products=products)
    return render_template("paints2.html", products=None)

@app.route('/pestilence2')
def pestilence():
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT id_product, name_product, name_type_material, name_method_application, price, volume FROM products JOIN type_material ON products.id_type_material = type_material.id_type_material JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE id_categories = 3 GROUP BY id_product ORDER BY 1 ASC")
    if result_value > 0:
        products = cursor.fetchall()
        cursor.close()
        return render_template("pestilence2.html", products=products)
    return render_template("pestilence2.html", products=None)

# @app.route('/pestilence/')
# def pestilence():
#     cursor = mysql.connection.cursor()
#     result_value = cursor.execute("SELECT id_product, name_product, name_type_material, COALESCE(name_type_coloring_agent, 'NULL') as name_type_coloring_agent, COALESCE(name_color, 'NULL') as name_color, COALESCE(name_gloss, 'NULL') as name_gloss, name_method_application, price, volume FROM products JOIN type_material ON products.id_type_material = type_material.id_type_material JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent JOIN type_color ON products.id_type_color = type_color.id_type_color JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE id_categories = 3 GROUP BY id_product ORDER BY 1 ASC")
#     if result_value > 0:
#         products = cursor.fetchall()
#         cursor.close()
#         return render_template("pestilence.html", products=products)
#     return render_template("pestilence.html", products=None)


@app.route('/selected-product<int:id>')
def products(id):
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT id_product, products.id_categories, name_product, name_type_material, name_type_coloring_agent, name_color, name_gloss, name_method_application, price, volume, name_categories FROM products LEFT JOIN type_material ON products.id_type_material = type_material.id_type_material LEFT JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent LEFT JOIN type_color ON products.id_type_color = type_color.id_type_color LEFT JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss LEFT JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application JOIN categories ON products.id_categories = categories.id_categories WHERE id_product = {}".format(id))
    
    if result_value > 0:
        products = cursor.fetchone()
        return render_template('selected-product.html', products=products)
    return 'Продукт не найден'


@app.route('/edit-product<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()        

        name_product = request.form['name_product']
        id_type_material = request.form['id_type_material']

        # id_type_coloring_agent = request.form['id_type_coloring_agent']
        # id_type_color = request.form['id_type_color']
        # id_type_gloss = request.form['id_type_gloss']

        id_type_coloring_agent = request.form.get('id_type_coloring_agent') or None
        id_type_color = request.form.get('id_type_color') or None
        id_type_gloss = request.form.get('id_type_gloss') or None

        id_type_method_application = request.form['id_type_method_application']
        price = request.form['price']
        volume = request.form['volume']

        # Проверка на пустые значения
        if not name_product or not price or not volume:
            flash('Все поля должны быть заполнены', 'danger')
            return redirect(request.url)  # Возвращаем на ту же страницу
        
         # Проверка уникальности name_product
        cursor.execute("SELECT COUNT(*) FROM products WHERE name_product = %s AND id_product != %s", (name_product, id))
        count = cursor.fetchone()['COUNT(*)']

        if count > 0:
            flash('Продукт с таким названием уже существует', 'danger')
            return redirect(request.url)
        
        # Проверка, что price и volume являются float
        try:
            price = float(price)
            volume = float(volume)
        except ValueError:
            flash('Цена и объем должны быть числовыми значениями', 'danger')
            return redirect(request.url)
        
         # Проверка, что price не отрицательный
        if price < 0:
            flash('Цена не может быть отрицательной', 'danger')
            return redirect(request.url)

        # Проверка, что volume находится в диапазоне от 0.25 до 10
        if volume < 0.25 or volume > 10:
            flash('Объем должен быть в диапазоне от 0.25 до 10', 'danger')
            return redirect(request.url)

        result_value = cursor.execute("UPDATE products LEFT JOIN type_material ON products.id_type_material = type_material.id_type_material LEFT JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent LEFT JOIN type_color ON products.id_type_color = type_color.id_type_color LEFT JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss LEFT JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application SET name_product = %s, products.id_type_material = %s, products.id_type_coloring_agent = %s, products.id_type_color = %s, products.id_type_gloss = %s,  products.id_type_method_application = %s, price = %s, volume = %s WHERE id_product = %s", (name_product, id_type_material, id_type_coloring_agent, id_type_color, id_type_gloss,  id_type_method_application, price, volume, id))

        mysql.connection.commit()
        cursor.close()
        flash('Продукт успешно обновлён', 'success')
        return redirect('/selected-product{}'.format(id))
    
    cursor = mysql.connection.cursor()
    result_value = cursor.execute("SELECT * FROM products LEFT JOIN type_material ON products.id_type_material = type_material.id_type_material LEFT JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent LEFT JOIN type_color ON products.id_type_color = type_color.id_type_color LEFT JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss LEFT JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE id_product = {}".format(id))
    if result_value > 0:
        products = cursor.fetchone()
        product_form = {}        
        product_form['id_categories'] = products['id_categories']
        product_form['name_product'] = products['name_product']
        product_form['id_type_material'] = products['id_type_material']
        product_form['id_type_coloring_agent'] = products['id_type_coloring_agent']
        product_form['id_type_color'] = products['id_type_color']
        product_form['id_type_gloss'] = products['id_type_gloss']
        product_form['id_type_method_application'] = products['id_type_method_application']
        product_form['price'] = products['price']
        product_form['volume'] = products['volume']

        cursor.execute("SELECT * FROM type_material")
        type_material = cursor.fetchall()

        cursor.execute("SELECT * FROM type_coloring_agent")
        type_coloring_agent = cursor.fetchall()

        cursor.execute("SELECT * FROM type_color")
        type_color = cursor.fetchall()

        cursor.execute("SELECT * FROM type_gloss")
        type_gloss = cursor.fetchall()

        cursor.execute("SELECT * FROM type_method_application")
        type_method_application = cursor.fetchall()


        return render_template('edit-product.html', product_form=product_form, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

    return render_template('edit-product.html', id_product=id)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():

    cursor = mysql.connection.cursor() 

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM type_material")
    type_material = cursor.fetchall()

    cursor.execute("SELECT * FROM type_coloring_agent")
    type_coloring_agent = cursor.fetchall()

    cursor.execute("SELECT * FROM type_color")
    type_color = cursor.fetchall()

    cursor.execute("SELECT * FROM type_gloss")
    type_gloss = cursor.fetchall()

    cursor.execute("SELECT * FROM type_method_application")
    type_method_application = cursor.fetchall()

    if request.method == 'POST':
        addproduct = request.form        
        name_product = addproduct['name_product']

        #id_categories = addproduct['id_categories']
        #id_type_material = addproduct['id_type_material']

        # id_type_coloring_agent = addproduct['id_type_coloring_agent']
        # id_type_color = addproduct['id_type_color']
        # id_type_gloss = addproduct['id_type_gloss']
        id_categories = addproduct.get('id_categories', '')
        id_type_material = addproduct.get('id_type_material', '')        

        id_type_coloring_agent = addproduct.get('id_type_coloring_agent') or None
        id_type_color = addproduct.get('id_type_color') or None
        id_type_gloss = addproduct.get('id_type_gloss') or None

        #id_type_method_application = addproduct['id_type_method_application']
        id_type_method_application = addproduct.get('id_type_method_application', '')

        price = addproduct['price']
        volume = addproduct['volume']

        # Валидация
        if not name_product or not price or not volume:
            flash("Все поля должны быть заполнены", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        # Проверка уникальности name_product
        cursor.execute("SELECT * FROM products WHERE name_product = %s", (name_product,))
        if cursor.fetchone():
            flash("Продукт с таким названием уже существует", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        # Проверка, что price и volume являются float
        try:
            price = float(price)
            volume = float(volume)
        except ValueError:
            flash("Цена и объем должны быть числовыми значениями", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        # Проверка на отрицательную цену
        if float(price) < 0:
            flash("Цена не может быть отрицательной", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        # Проверка на допустимый объем
        if not (0.25 <= float(volume) <= 10):
            flash("Объём должен быть в диапазоне от 0.25 до 10 литров", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
        
         # Проверка на выбранные значения в зависимости от категории
        if not id_categories:
            flash("Не выбрана категория", 'danger')
            return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        # Проверка обязательных полей в зависимости от категории
        if id_categories in ['1', '2']:  # Для категорий 1 и 2
            if not id_type_material:
                flash("Не выбран тип материала", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
            if not id_type_method_application:
                flash("Не выбран метод нанесения", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
            # Проверка на наличие красящего вещества, цвета и блеска
            if not id_type_coloring_agent:
                flash("Не выбрано красящее вещество", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
            if not id_type_color:
                flash("Не выбран цвет", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
            if not id_type_gloss:
                flash("Не выбран блеск", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        elif id_categories == '3':  # Для категории 3
            if not id_type_material:
                flash("Не выбран тип материала", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)
            if not id_type_method_application:
                flash("Не выбран метод нанесения", 'danger')
                return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)

        cursor = mysql.connection.cursor()        

        cursor.execute("INSERT INTO products (name_product, id_categories, id_type_material, id_type_coloring_agent, id_type_color, id_type_gloss, id_type_method_application, price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name_product, id_categories, id_type_material, id_type_coloring_agent, id_type_color, id_type_gloss, id_type_method_application, price, volume))
                
        mysql.connection.commit()
        cursor.close()

        flash("Продукт успешно добавлен", 'success')

        return redirect("/products2")

    return render_template('add-product.html', categories=categories, type_material=type_material, type_coloring_agent=type_coloring_agent, type_color=type_color, type_gloss=type_gloss, type_method_application=type_method_application)


@app.route('/delete-product/<int:id>')
def delete_product(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM products WHERE id_product = {}".format(id))
    mysql.connection.commit()
    flash("Продукт успешно удалён", 'success')
    return redirect("/products2")





# 1 модальное окно

@app.route('/add_type_material/', methods=['GET', 'POST'])
def add_type_material():
    cursor = mysql.connection.cursor() 

    if request.method == 'POST':
        addproduct = request.form
        
        # Обновление существующих материалов
        for key in addproduct.keys():
            if key.startswith('material_'):
                id_type_material = key.split('_')[1]  # Извлекаем ID из ключа
                name_type_material = addproduct[key]
                cursor.execute("UPDATE type_material SET name_type_material = %s WHERE id_type_material = %s", (name_type_material, id_type_material))

        # Добавление новых материалов
        for key in addproduct.keys():
            if key.startswith('new_material_'):
                name_type_material = addproduct[key]
                if name_type_material:  # Вставляем только если поле не пустое
                    cursor.execute("INSERT INTO type_material (name_type_material) VALUES (%s)", (name_type_material,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(request.url)
    
    # flash("Материалы успешно обновлены", 'success')
    
    cursor.execute("SELECT * FROM type_material")
    type_material = cursor.fetchall()
    return render_template('add_type_material.html', type_material=type_material)


@app.route('/delete_type_material/<int:id>')
def delete_type_material(id):
    cursor = mysql.connection.cursor()
    try:
        result = cursor.execute("DELETE FROM type_material WHERE id_type_material = {}".format(id))
        mysql.connection.commit()
        if result > 0:
            flash("Материал успешно удалён", 'success')
    except Exception as e:
        flash("Ошибка при удалении материала (нельзя удалять используемые материалы)", 'danger')
    
    return redirect("/products2")



# 2 модальное окно

@app.route('/add_type_method_application/', methods=['GET', 'POST'])
def add_type_method_application():
    cursor = mysql.connection.cursor() 

    if request.method == 'POST':
        addproduct = request.form
        
        # Обновление существующих материалов
        for key in addproduct.keys():
            if key.startswith('material_'):
                id_type_material = key.split('_')[1]  # Извлекаем ID из ключа
                name_type_material = addproduct[key]
                cursor.execute("UPDATE type_method_application SET name_method_application = %s WHERE id_type_method_application = %s", (name_type_material, id_type_material))

        # Добавление новых материалов
        for key in addproduct.keys():
            if key.startswith('new_material_'):
                name_type_material = addproduct[key]
                if name_type_material:  # Вставляем только если поле не пустое
                    cursor.execute("INSERT INTO type_method_application (name_method_application) VALUES (%s)", (name_type_material,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(request.url)
    
    # flash("Материалы успешно обновлены", 'success')
    
    cursor.execute("SELECT * FROM type_method_application")
    type_method_application = cursor.fetchall()
    return render_template('add_type_material.html', type_method_application=type_method_application)


@app.route('/delete_type_method_application/<int:id>')
def delete_type_method_application(id):
    cursor = mysql.connection.cursor()
    try:
        result = cursor.execute("DELETE FROM type_method_application WHERE id_type_method_application = {}".format(id))
        mysql.connection.commit()
        if result > 0:
            flash("Материал успешно удалён", 'success')
    except Exception as e:
        flash("Ошибка при удалении материала (нельзя удалять используемые материалы)", 'danger')
    return redirect("/products2")



# 3 модальное окно

@app.route('/add_type_coloring_agent/', methods=['GET', 'POST'])
def add_type_coloring_agent():
    cursor = mysql.connection.cursor() 

    if request.method == 'POST':
        addproduct = request.form
        
        # Обновление существующих материалов
        for key in addproduct.keys():
            if key.startswith('material_'):
                id_type_material = key.split('_')[1]  # Извлекаем ID из ключа
                name_type_material = addproduct[key]
                cursor.execute("UPDATE type_coloring_agent SET name_type_coloring_agent = %s WHERE id_type_coloring_agent = %s", (name_type_material, id_type_material))

        # Добавление новых материалов
        for key in addproduct.keys():
            if key.startswith('new_material_'):
                name_type_material = addproduct[key]
                if name_type_material:  # Вставляем только если поле не пустое
                    cursor.execute("INSERT INTO type_coloring_agent (name_type_coloring_agent) VALUES (%s)", (name_type_material,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(request.url)
    
    # flash("Материалы успешно обновлены", 'success')
    
    cursor.execute("SELECT * FROM type_coloring_agent")
    type_coloring_agent = cursor.fetchall()
    return render_template('add_type_material.html', type_coloring_agent=type_coloring_agent)


@app.route('/delete_type_coloring_agent/<int:id>')
def delete_type_coloring_agent(id):
    cursor = mysql.connection.cursor()
    try:
        result = cursor.execute("DELETE FROM type_coloring_agent WHERE id_type_coloring_agent = {}".format(id))
        mysql.connection.commit()
        if result > 0:
            flash("Материал успешно удалён", 'success')
    except Exception as e:
        flash("Ошибка при удалении материала (нельзя удалять используемые материалы)", 'danger')
    return redirect("/products2")



# 4 модальное окно

@app.route('/add_type_color/', methods=['GET', 'POST'])
def add_type_color():
    cursor = mysql.connection.cursor() 

    if request.method == 'POST':
        addproduct = request.form
        
        # Обновление существующих материалов
        for key in addproduct.keys():
            if key.startswith('material_'):
                id_type_material = key.split('_')[1]  # Извлекаем ID из ключа
                name_type_material = addproduct[key]
                cursor.execute("UPDATE type_color SET name_color = %s WHERE id_type_color = %s", (name_type_material, id_type_material))

        # Добавление новых материалов
        for key in addproduct.keys():
            if key.startswith('new_material_'):
                name_type_material = addproduct[key]
                if name_type_material:  # Вставляем только если поле не пустое
                    cursor.execute("INSERT INTO type_color (name_color) VALUES (%s)", (name_type_material,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(request.url)
    
    # flash("Материалы успешно обновлены", 'success')
    
    cursor.execute("SELECT * FROM type_color")
    type_color = cursor.fetchall()
    return render_template('add_type_material.html', type_color=type_color)


@app.route('/delete_type_color/<int:id>')
def delete_type_color(id):
    cursor = mysql.connection.cursor()
    try:
        result = cursor.execute("DELETE FROM type_color WHERE id_type_color = {}".format(id))
        mysql.connection.commit()
        if result > 0:
            flash("Материал успешно удалён", 'success')
    except Exception as e:
        flash("Ошибка при удалении материала (нельзя удалять используемые материалы)", 'danger')
    return redirect("/products2")



# 5 модальное окно

@app.route('/add_type_gloss/', methods=['GET', 'POST'])
def add_type_gloss():
    cursor = mysql.connection.cursor() 

    if request.method == 'POST':
        addproduct = request.form
        
        # Обновление существующих материалов
        for key in addproduct.keys():
            if key.startswith('material_'):
                id_type_material = key.split('_')[1]  # Извлекаем ID из ключа
                name_type_material = addproduct[key]
                cursor.execute("UPDATE type_gloss SET name_gloss = %s WHERE id_type_gloss = %s", (name_type_material, id_type_material))

        # Добавление новых материалов
        for key in addproduct.keys():
            if key.startswith('new_material_'):
                name_type_material = addproduct[key]
                if name_type_material:  # Вставляем только если поле не пустое
                    cursor.execute("INSERT INTO type_gloss (name_gloss) VALUES (%s)", (name_type_material,))
        
        mysql.connection.commit()
        cursor.close()
        return redirect(request.url)
    
    # flash("Материалы успешно обновлены", 'success')
    
    cursor.execute("SELECT * FROM type_gloss")
    type_gloss = cursor.fetchall()
    return render_template('add_type_material.html', type_gloss=type_gloss)


@app.route('/delete_type_gloss/<int:id>')
def delete_type_gloss(id):
    cursor = mysql.connection.cursor()
    try:
        result = cursor.execute("DELETE FROM type_gloss WHERE id_type_gloss = {}".format(id))
        mysql.connection.commit()
        if result > 0:
            flash("Материал успешно удалён", 'success')
    except Exception as e:
        flash("Ошибка при удалении материала (нельзя удалять используемые материалы)", 'danger')
    return redirect("/products2")




@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM products WHERE name_product LIKE %s", ('%' + query + '%',))
    cur.execute("SELECT id_product, name_product, name_type_material, name_type_coloring_agent, name_color, name_gloss, name_method_application, price, volume FROM products LEFT JOIN type_material ON products.id_type_material = type_material.id_type_material LEFT JOIN type_coloring_agent ON products.id_type_coloring_agent = type_coloring_agent.id_type_coloring_agent LEFT JOIN type_color ON products.id_type_color = type_color.id_type_color LEFT JOIN type_gloss ON products.id_type_gloss = type_gloss.id_type_gloss LEFT JOIN type_method_application ON products.id_type_method_application = type_method_application.id_type_method_application WHERE name_product LIKE %s", ('%' + query + '%',))
    results = cur.fetchall()
    cur.close()
    return render_template('results.html', results=results)







if __name__ == '__main__':
    app.run(debug=True, port=5001)