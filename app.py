from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('rtm.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    if request.method == 'POST':
        # Replace 'main.py' with the path to your Python script
        script_path = 'main.py'
        result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
