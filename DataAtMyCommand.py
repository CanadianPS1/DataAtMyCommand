import json
import os

filePath = "Python Code\JSON folder stuff\db.json"
if os.path.exists(filePath):
    with open(filePath, "r") as file:
        infomation = json.load(file)
else:
    infomation = {"user": []}
while True:
    command = input("DataAtMyCommand: ")
    if(command == "list"):
        for item in infomation["user"]:
            print(f"User: {item["fName"]} {item["lName"]}" )
            print(f"   PhoneNumber: {item["phoneNumber"]}")
            print("----------------------------------------")
    
    elif(command == "add"):
        firstName = ""
        lastName = ""
        phoneNumber = ""
        #checks to make sure the user inputs correct data
        while True:
            firstName = input("Whats for fist name?: ")
            if(firstName.isalpha and firstName != ""):
                break
            else:
                print("ERROR: enter a valid String")
        while True:
            lastName = input("Whats your last name?: ")
            if(lastName.isalpha and lastName != ""):
                break
            else:
                print("ERROR: enter a valid String")
        while True:
            phoneNumber = input("Whats your phone number?: ")
            if(any(char.isdigit() for char in phoneNumber) and phoneNumber != ""):
                break
            else:
                print("ERROR: enter a valid Integer")
        #puts the entered info into a dictionary
        user = {"user": firstName + " " + lastName,
                "phoneNumber": str(phoneNumber),
                "lName": lastName,
                "fName": firstName}
        infomation["user"].append(user)
        print(f"{firstName} {lastName} was added")
        with open(filePath, "w") as file:
            json.dump(infomation,file,indent=4)
    #this is my find "function"
    elif(command == "find"):
        command = input("What would you like to find?: ")
        found = False
        userItem = ""
        phoneNumberItem = ""
        for item in infomation["user"]:
            if("user" in item):
                userItem = item
            if("phoneNumber" in item):
                phoneNumberItem = item
            #this finds if any of your search turms are in the list
            if(command.lower() == str(item["fName"].lower())
            or command.lower() == str(item["lName"].lower()) 
            or command.lower() == str(item["phoneNumber"].lower()) 
            or command.lower() == str(item["user"].lower())):
                #desplays the elememnt
                print("User: ",item["user"])
                print("PhoneNumber: ",item["phoneNumber"])
                found = True
                break
        if(not found):
            print(f"{command} was not found in the Database")
    #This is my delete "function"
    elif(command == "del"):
        command = input("What would you like to delete?: ")
        found = False
        for item in infomation["user"]:
            #this finds if any of your search turms are in the list
            if(command.lower() == str(item["fName"].lower())
            or command.lower() == str(item["lName"].lower()) 
            or command.lower() == str(item["phoneNumber"].lower()) 
            or command.lower() == str(item["user"].lower())):
                #removes the element
                found = True
                print(f"{item["user"]} was deleted")
                infomation["user"].remove(item)
                with open(filePath, "w") as file:
                    json.dump(infomation,file,indent=4)
                break
        if(not found):
            print(f"{command} was not found in the Database")
    elif(command == "quit"):
        break
    else:
        print("ERROR: invalid input")