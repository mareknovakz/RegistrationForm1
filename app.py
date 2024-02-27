from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Funkce pro vytvoření spojení s SQLite databází
def get_db_connection():
    conn = sqlite3.connect('DatabaseUser.db')
    conn.row_factory = sqlite3.Row
    return conn

# Funkce pro získání všech uživatelů z databáze
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

# Endpoint pro získání všech uživatelů
@app.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    users_list = []
    for user in users:
        user_dict = dict(user)
        users_list.append(user_dict)
    return jsonify(users_list)

# Endpoint pro přidání nového uživatele
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                 (new_user['username'], new_user['email'], new_user['password']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Uživatel byl úspěšně přidán.'}), 201

# Endpoint pro zobrazení registračního formuláře
@app.route('/')
def show_registration_form():
    return render_template('RegistrationForm.html')

if __name__ == '__main__':
    app.run(debug=True)
