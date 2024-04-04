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

# Crear un nuevo ticket
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_name = 'helpdesk.ticket'

@app.route('/crear_ticket', methods=['POST'])
def crear_ticket():
    if request.method == 'POST':
        ticket_data = request.json
        ticket_id = models.execute_kw(db, uid, password, model_name, 'create', [ticket_data])
        return jsonify({'ticket_id': ticket_id}), 201
    else:
        return jsonify({'error': 'Método no permitido'}), 405

