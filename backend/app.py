from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'users': [
            {'name': 'luffy', 'age': 30},
            {'name': 'zorro', 'age': 25},
            {'name': 'croco', 'age': 35}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
