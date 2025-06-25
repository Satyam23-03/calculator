from flask import Flask, render_template, request, jsonify
import random
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json.get('expression', '')
    try:
        # Replace ^ with ** for exponentiation
        expr = expression.replace('^', '**')
        # Calculate correct result
        correct_result = eval(expr, {"__builtins__": {}}, {"math": math})
        # Make it wrong by adding a random number
        wrong_result = correct_result + random.randint(1, 10) * (1 if random.random() > 0.5 else -1)
        return jsonify({
            'result': wrong_result,
            'message': 'Apna khud ka dimag laga na Lawde!'
        })
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
