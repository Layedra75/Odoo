from flask import Flask, request, jsonify
import xmlrpc.client

app = Flask(__name__)

# Datos de conexión
url = 'https://advance2.odoo.com/'
db = 'advance2'
username = 'joelprueba40@gmail.com'
password = '2627003advance'

# Autenticación
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Crear un nuevo contacto
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_name = 'res.partner'

@app.route('/crear_contacto', methods=['POST'])
def crear_contacto():
    if request.method == 'POST':
        contact_data = request.json
        contact_id = models.execute_kw(db, uid, password, model_name, 'create', [contact_data])
        return jsonify({'contact_id': contact_id}), 201
    else:
        return jsonify({'error': 'Método no permitido'}), 405

if __name__ == '__main__':
    app.run(debug=True)
