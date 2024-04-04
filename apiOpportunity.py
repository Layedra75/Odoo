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

# Crear una nueva oportunidad
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_name = 'crm.lead'

@app.route('/crear_oportunidad', methods=['POST'])
def crear_oportunidad():
    if request.method == 'POST':
        opportunity_data = request.json
        opportunity_id = models.execute_kw(db, uid, password, model_name, 'create', [opportunity_data])
        return jsonify({'opportunity_id': opportunity_id}), 201
    else:
        return jsonify({'error': 'Método no permitido'}), 405

if __name__ == '__main__':
    app.run(port=5002, debug=True)
