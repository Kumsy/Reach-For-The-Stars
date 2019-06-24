import pyrebase
import json



with open('config/config.json', 'r') as f:
    config = json.load(f)

config = { 
  'apiKey': config['apiKey'],
  'authDomain': config['authDomain'],
  'databaseURL': config['databaseURL'],
  'projectId': config['projectId'],
  'storageBucket': "",
  'messagingSenderId': config['messagingSenderId'],
  'appId': config['appId']
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Add to our database
#========================
# db.child("names").push({"name": "kristen_loves_you"})
# db.child("names").child("name").update({"name": "kumsy"})

# Get value and key from our database
#======================================
# users = db.child("names").child("name").get()
# print(users.val())
# print(users.key())

# Removes what you want specifically
#=======================================
# db.child("names").child("name").remove()

# Removes everything in your databased names
#=============================================
# db.child("names").remove()