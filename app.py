from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_segura'

# CONEXIÓN A SQL SERVER
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6RA3OO5\\SQLEXPRESS;'
    'DATABASE=BoticaVentas;'
    'Trusted_Connection=yes;'
)

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Usuario y clave fijos (puedes luego conectar a una tabla)
        if username == 'admin' and password == '1234':
            session['usuario'] = username
            return redirect(url_for('index'))
        else:
            error = "⚠️ Usuario o contraseña incorrectos"
    return render_template('login.html', error=error)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# ---------------- PÁGINA PRINCIPAL ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        producto = request.form['producto']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Pedidos (nombre_cliente, producto, cantidad, precio)
            VALUES (?, ?, ?, ?)
        """, (nombre, producto, cantidad, precio))
        conn.commit()
        mensaje = "✅ Pedido registrado con éxito"

    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_cliente, producto, cantidad, precio, fecha FROM Pedidos")
    pedidos = [
        {
            "id": row[0],
            "nombre_cliente": row[1],
            "producto": row[2],
            "cantidad": row[3],
            "precio": row[4],
            "fecha": row[5]
        } for row in cursor.fetchall()
    ]
    return render_template('Formulario.html', pedidos=pedidos, mensaje=mensaje)

# ---------------- ACTUALIZAR ----------------
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    nombre = request.form['nombre_cliente']
    producto = request.form['producto']
    cantidad = request.form['cantidad']
    precio = request.form['precio']

    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Pedidos
        SET nombre_cliente = ?, producto = ?, cantidad = ?, precio = ?
        WHERE id = ?
    """, (nombre, producto, cantidad, precio, id))
    conn.commit()
    return redirect(url_for('index'))

# ---------------- ELIMINAR ----------------
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pedidos WHERE id = ?", (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
