import socket
from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')

# Applications Routes
def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@bp.route("/health")
def health():
    host_name, host_ip = fetchDetails()
    return jsonify(
        host=host_name,
        ip=host_ip,
        status="Up"
    )
    
# Add your routes here ensure they return api json