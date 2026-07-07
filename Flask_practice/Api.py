from flask import Flask, jsonify, request

app = Flask(__name__)

# initial data in my todo list--can come from any databse
items = [
    {"id": 1, "name": "Task 1", "description": "This is task 1"},
    {"id": 2, "name": "Task 2", "description": "This is task 2"}
]


@app.route('/')
def home():
    return "Welcome to the To-DO list Application!"

# Get: to retrieve all the items in list


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)  # return the items in json format

# Get: to retrieve item by id


@app.route('/items/<int:item_id>', methods=['GET'])
def get_itemid(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "item not found"}), 404

# post : to add new item in the list , each api request have some parametres tos end the data json is one of them that we will capture - THIS IS AN API request to add item

@app.route('/items', methods=['POST'])
def add_item():
    # when json body not found
    if not request.json or not 'name' in request.json:
        return jsonify({
            "message": "Error, Item not found",
        })
    new_item={
        "id":len(items)+1,
        "name":request.json['name'],
        "description":request.json["description"]
        }
    items.append(new_item)
    return jsonify(new_item),201 #return the new jsonify item and 201 code for created

#put-to update any task in list
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next(( item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({
            "message":"item not found"
        })
        #in order to update also i have to give a new post request , so  i wil use request.json.get to get the new data from the request body instead of request.json['name'] which will give error if name is not present in the request body
    item["name"]=request.json.get("name",item["name"]) #get the new name value and update with old value
    item["description"]=request.json.get("description",item["description"])
    return jsonify(item)

#Delete-to delete any task in the list
@app.route('/items/<int:item_id>',methods=["DELETE"])
def delete_item(item_id):
    global items
    #keep every item except that of id which we want to delete
    items=[item for item in items if item["id"]!=item_id]
    return jsonify({
        "message":"item deleted successfully"
    })



# why we use json format to display data in browsers ?
# Separates Data from Layout: Server sends raw data, letting JavaScript handle the design.#Lightweight and Fast: Reduces bandwidth by sending only data instead of heavy HTML.Universal #Browser Match: Native to JavaScript, making it incredibly easy to parse.Multi-Platform #Support: One JSON response feeds web browsers, mobile apps, and APIs.


if __name__ == "__main__":
    app.run(debug=True)
