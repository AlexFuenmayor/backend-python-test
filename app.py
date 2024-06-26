from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    # Obtiene los datos JSON del request
    data = request.get_json()

    # Extrae los números del JSON
    num1 = data.get('num1')
    num2 = data.get('num2')

    # Verifica que ambos números estén presentes
    if num1 is None or num2 is None:
        return jsonify({'error': 'Faltan uno o ambos números'}), 400

    # Calcula la suma
    total = num1 + num2

    # Retorna el resultado como JSON
    return jsonify({'result': total})


if __name__ == '__main__':
    app.run(debug=True)
