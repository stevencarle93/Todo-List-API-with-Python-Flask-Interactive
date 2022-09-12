from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label":"Sacar al perro", "done": True },
    { "label":"Cocinar frijoles", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data 
    decoded_body = json.loads(request_body)
    todos.append(decoded_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos) 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ", position)
    return jsonify(todos)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=3245, debug=True)