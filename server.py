from flask import Flask, send_from_directory, request, jsonify
import subprocess, os

WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=WEBSITE_DIR)

@app.route('/')
def index():
    return send_from_directory(WEBSITE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(WEBSITE_DIR, filename)

@app.route('/cmd', methods=['POST'])
def run_cmd():
    cmd = request.json.get('cmd', '')
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30, cwd=WEBSITE_DIR)
        return jsonify({'stdout': result.stdout, 'stderr': result.stderr, 'code': result.returncode})
    except Exception as e:
        return jsonify({'stdout': '', 'stderr': str(e), 'code': 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
