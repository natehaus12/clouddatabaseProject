import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

#######################################################################

# initialize the database and connect this project to the database
def initialize():

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "clouddatabaseProject\key.json"

    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'football-database-43114',
    })

    db = firestore.client()
    return db

#############################################################################

# add to the database
def add(db):
    name = input("Your Name: ")
    team = input("Your Favorite Team: ")


    result = db.collection("people").document(name).get()
    if result.exists:
      print("Name already exists!")
      return

    data = {"fav_team": team}
    db.collection("people").document(name).set(data)
    print("Successfully added!")

##############################################################################

# delete a person and their data from the database
def delete(db):
    name = input("Your name: ")

    result = db.collection("people").document(name).get()
    if result.exists:
        db.collection("people").document(name).delete()
        print("Successfully Deleted!")
    else:
        print("Inavlid name")

#################################################################################

# allow the user to update their favorite team
def modify(db):
    name = input("Your Name: ")
    doc_ref = db.collection("people").document(name)

    doc = doc_ref.get()
   
    if doc.exists:
        print("Your current favorite team is set to: ")
        print(f'{doc.to_dict()}')
        team = input("Your New Favorite Team: ")
        data = {"fav_team": team}
        db.collection("people").document(name).update(data)
        print("Successfully updated!")
        

    else: 
        print("Invalid Name.")

####################################################################################

# allow the user to view their favorite team
def view(db):
        name = input("Your Name: ")
        doc_ref = db.collection("people").document(name)

        doc = doc_ref.get()

        if doc.exists:
            print("Your current favorite team is set to: ")
            print(f'{doc.to_dict()}')

        else: 
            print("Invalid Name.")

#####################################################################################


# set up database
db = initialize()

# use prints as menu to select what the user wants to do

print("I have created a database that stores your name and your favorite football team!")
print("1: Add To Database")
print("2: Delete Yourself From Database")
print("3: Change Your Favorite Team")
print("4: View Favorite Teams")

decision = input("Enter a Number: ")

# menu

if decision == "1":
    add(db)
elif decision == "2":
    delete(db)
elif decision == "3":
    modify(db)
elif decision == "4":
    view(db)
else:
    print("Invalid input")











