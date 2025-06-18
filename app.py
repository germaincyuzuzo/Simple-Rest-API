from flask import Flask, request, jsonify
import uuid

#INITIATE THE FLASK APP
app = Flask(__name__)

#IN-MEMORY DATA STORAGE
users = {}

#POST USER ENDPOINT
#PARSING DATA AND STORING IT TO A VARIABLE
@app.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()

    #BASIC DATA VALIDATION
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email' in request"}), 400
    
    #CREATE A UNIQUE USER ID
    user_id = str(uuid.uuid4())

    #CREATE A USER OBJECT TO STORE IN THE users dict
    user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email']
    }

    #INSERT USER IN MEMORY
    users[user_id] = user

    return jsonify(user), 201

#GET USER ENDPOINT
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    #SIMPLE VALIDATION
    if not user:
        return jsonify({"error": "User is not found"}), 404
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)