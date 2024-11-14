from flask import Flask, jsonify

users = {
    "1": {'id':1, "name":"John"},
    "2": {'id':2, "name":"Mary"}
}

app = Flask(__name__)

@app.route('/', methods=['GET'])
def top_url():
    temp = list(users.values())
    return jsonify(temp)


app.run(host='0.0.0.0', port=5000, debug=True)
