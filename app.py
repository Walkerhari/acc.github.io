from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('RTMS4.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    if request.method == 'POST':
        # Replace 'main.py' with the path to your Python script
        script_path = 'main.py'
        try:
            result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            output = result.stdout
            return jsonify({'output': output})
        except subprocess.CalledProcessError as e:
            error_message = e.stderr
            return jsonify({'error': error_message})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

