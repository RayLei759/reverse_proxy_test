from flask import Flask, request,abort

app = Flask(__name__)

@app.route('/Hello')
def index():
    return "Hubs"
trusted_ip = ['127.0.0.0', '172.17.0.1']
@app.route('/client')
def get_ip():
    ip_addr = request.remote_addr
    while ip_addr in trusted_ip:
        return ip_addr
    while ip_addr not in trusted_ip:
        abort(403)
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    while ip_addr in trusted_ip:
        return ip_addr
    while ip_addr not in trusted_ip:
        abort(403)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8001)