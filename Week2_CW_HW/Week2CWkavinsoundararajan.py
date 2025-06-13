#Integer
age=14
print("Age:",age)
#String
name="Kavin"
print("Name:",name)
#Float
height=5.20
print("Height:",height)
#Boolean
is_student=True
print("Is a student:",is_student)
#Lists because multiple strings
fruits={"apple","banana","mango"}
print("Fruits:",fruits)
#Lists because multiple strings
heights={"5.1","5.2","6.8"}
print("Peoples heights in this room:",heights)
#Dictionary stores values for words
student={"name":"Alice","age":20}
print(student)
#Dictionary stores values for words
description={"Name":"Kavin","height":5.85}
print(description)
#Dictionary stores values for words
favorite_subjects_and_ratings={"Math":10,"ELA":1}
print(favorite_subjects_and_ratings)
#Dictionary for book availability
book={"title":"I Am Number 4","pages":450,"author":"Pittacus Lore","available":True}
print(book["available"])
student={"Name":"Kavin","Age":59,"Grade":12}
#Update value
student["Age"]=14
print(student)
student["Grade"]=9 
print(student)
del student["Age"]
print(student)
#String Maniupulation
message="Hello, Python World!"
print("Length of message:", len(message))
print("Uppercase:",message.upper())
print("Lowercase:",message.lower())
print("Does the message contain'World?","World" in message)
print("First 5 characters:",message[:5])
print("Last 6 characters:",message[-6:])
greeting="Hi there!"
combined=greeting+" "+message
print(combined)
print("Characters 2 to 6:",message[2:6])
new_message=combined.replace("there!","Kavin.")
print(new_message)