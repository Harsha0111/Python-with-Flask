from flask import Flask, jsonify, request

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'name': "Abi"},

    {
        'id': 2,
        'name': "Balu"
    }
]
# home


@app.route('/')
def home():
    return "Hello, Welcome to My Channel"


# GET
@app.route('/persons')
def get_all_persons():
    return jsonify({'persons': persons})


# GET by Id
@app.route('/person/<int:id>')
def get_person(id):
    for person in persons:
        if person['id'] == id:
            return person
    return {'msg': 'person not found'}, 404


# POST
@app.route('/person', methods=['POST'])
def create_person():
    req_data = request.get_json()
    global persons

    if "id" not in persons:
        # If "id" key is not present in the data, generate a new unique ID
        if persons:
            # Get the last ID from the list and increment it by 1
            new_id = persons[-1]["id"] + 1
        else:
            # If the list is empty, start with ID 1
            new_id = 1

    new_person = {
        'id': new_id,
        'name': req_data['name']
    }

    persons.append(new_person)
    return jsonify(new_person)

# UPDATE


@app.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    req_data = request.get_json()
    for person in persons:
        if person['id'] == id:
            update = {
                'name': req_data['name']
            }
            person.update(update)
            return (person)
    return jsonify({'msg': 'person not found'})

# DELETE


@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person_to_delete = next(
        (person for person in persons if person['id'] == id), None)

    if person_to_delete:
        # If the person is found, remove them from the list
        persons.remove(person_to_delete)
        # Return a response indicating success (Optional)
        return jsonify({"message": f"Dictionary with id={id} deleted successfully."}), 200
    else:
        # Return a response indicating failure (Optional)
        return jsonify({"error": f"Dictionary with id={id} not found in the list."}), 404


app.run(port=5050, debug=True)
