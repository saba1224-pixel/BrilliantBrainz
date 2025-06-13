age=20
print("Age:",age)
#integer

Name= "JianHaoTan";
print("name:", Name)
#string

Height= 6.8
print("Height", Height)
#float

is_student=False
print("Is a student:", is_student)
#boolean

countries={"South Africa","Australia","India","Amaaniland","America"}
print("countries:",countries)

heights={6.8,5.2,3.4,6.7,8.3}
print("heights:",heights)

student={"name":"Alice", "age":20}
print("student info:",student)

player={"name":"Amaani","height":6.8}
print("player name and height:",player)

book={"title":"Amaani is the greatest","pages":10000, "author":"Amoney", "available":True}
print(book["available"])

student={"name": "Amaani","age":33}
student["age"]=16 #update value
print(student)
student["grade"]=10 #add/modify
print(student)

del student["age"]
print(student)

#STRING MANIPULATION
message="Hello, Python World!"
print("Original message:",message)
print("Length of messsage: ",len(message))

print("Uppercase:",message.upper())
print("Lowercase",message.lower())

print("Does this message contain world?", "world" in message)

print("First 5 characters:",message[:5])
print("Last 6 characters:",message[-6:])

greeting="Hi there!"
combined=greeting + " "+ message
print(combined)

print(message[2:6])

new_message=combined.replace("there!","Saba")
print(new_message)