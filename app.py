from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_segura'

# CONEXIÓN A SQL SERVER
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6RA3OO5\\SQLEXPRESS;'
    'DATABASE=MinimartLaFavorita;'
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
        cliente = request.form['cliente']
        prenda = request.form['prenda']
        talla = request.form['talla']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Ventas (cliente, prenda, talla, cantidad, precio)
            VALUES (?, ?, ?, ?, ?)
        """, (cliente, prenda, talla, cantidad, precio))
        conn.commit()
        mensaje = "✅ Venta registrada con éxito"

    cursor = conn.cursor()
    cursor.execute("SELECT id, cliente, prenda, talla, cantidad, precio, fecha FROM Ventas")
    ventas = [
        {
            "id": row[0],
            "cliente": row[1],
            "prenda": row[2],
            "talla": row[3],
            "cantidad": row[4],
            "precio": row[5],
            "fecha": row[6]
        } for row in cursor.fetchall()
    ]
    return render_template('Formulario.html', ventas=ventas, mensaje=mensaje)

# ---------------- ACTUALIZAR ----------------
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    cliente = request.form['cliente']
    prenda = request.form['prenda']
    talla = request.form['talla']
    cantidad = request.form['cantidad']
    precio = request.form['precio']

    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Ventas
        SET cliente = ?, prenda = ?, talla = ?, cantidad = ?, precio = ?
        WHERE id = ?
    """, (cliente, prenda, talla, cantidad, precio, id))
    conn.commit()
    return redirect(url_for('index'))

# ---------------- ELIMINAR ----------------
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ventas WHERE id = ?", (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
