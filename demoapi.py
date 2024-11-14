from flask import Flask, jsonify

users = {
    "1": {'id':1, "name":"John"},
    "2": {'id':2, "name":"Mary"}
}

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all_users():
    temp = list(users.values())
    return jsonify(temp)

@app.route('/users/<userid>', methods=['GET'])
def get_single_user(userid):
    this_user = users[userid]
    return jsonify(this_user)


app.run(host='0.0.0.0', port=5000, debug=True)
