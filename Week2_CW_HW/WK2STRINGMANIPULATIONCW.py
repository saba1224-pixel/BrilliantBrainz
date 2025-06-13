#integer
age=20
print("age", age)
#string
name="arjun"
print("name:", name)
#float
height=5.8
print("height:", height)
#boolean
is_student=True
print("is_student:", is_student)
#list
fruits= {"mango","banana","apple"}
print("fruits:", fruits)
#float #list
temperatures= {"88.7","64.2","71.9"}
print("temperatures:", temperatures)
#dictionary
biography={"age":"22", "name":"Nihar"} 
print("biography:", biography)
#dictionary
book= {"title":"Percy Jackson","pages": 309, "author": "Rick Riordan", "available":True, "book rating":4.8}
print(book["available"])
biography["age"]=23
print(biography)
biography["grade"]= 17
print(biography)
del biography["age"]
print(biography)
#string manipulation
message= "Hello, Python World!"
print("Length of message:", len(message))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Does the message contain world?","World" in message)
print("First 5 characters:", message[:5])
message[-6:]
greeting= "Hi there!"
combined= greeting+" "+message
print(combined)
print(message[2:6])
new_message=combined.replace("there!", "arjun")
print(new_message)