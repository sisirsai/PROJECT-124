from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [

{
    'id': 1, 
    'name': u'Raju', 
    'contact_number': u'9864755601', 
    'done': False 
},

{ 
    'id': 2, 
    'name': u'Ravi', 
    'contact_number': u'7643218908', 
    'done': False
},

{
    'id': 3, 
    'name': u'Rafi', 
    'contact_number': u'8652323126', 
    'done': False 
},

{
    'id': 4, 
    'name': u'Manveer', 
    'contact_number': u'9543456760', 
    'done': False 
},

{
    'id': 5, 
    'name': u'Rahul', 
    'contact_number': u'9494040499', 
    'done': False 
},

]

@app.route("/add-data", methods=["POST"]) 
def add_task(): 
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400) 
    contact = { 
        'id': contacts[-1]['id'] + 1, 
        'name': request.json['title'], 
        'contact_number': request.json.get('description', ""), 
        'done': False 
    } 
    contacts.append(contact) 
    return jsonify({ "status":"success", "message": "Task added succesfully!" })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data': contacts
    }) 

if __name__ == '__main__':
    app.run()

