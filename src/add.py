from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    try:
        sum = float(num1) + float(num2)
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400
    return jsonify({"sum": sum})

@app.route('/hello', methods=['GET'])
def hello():
    return "hello!"

if __name__ == '__main__':
    app.run(host='::', port=8080)
