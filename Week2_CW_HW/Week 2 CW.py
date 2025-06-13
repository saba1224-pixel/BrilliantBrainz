#integer
age=20
print("Age:",age)

#string
name="Viswa"
print("Name:",name)

#float
height=5.6
print("Height:",height)

#boolean
is_student=True
print("Is a student:",is_student)

#list
fruits={"apple", "banana", "mango"}
print("Fruits:",fruits)

#list
temperature={86, 54, 79}
print("Temperatures:",temperature)

#dictionary
student={"name":"Alice", "age":20}
print("Student info:",student)

#dictionary
points={"Jason":5.6, "Max":7.4}
print("Points:",points)

#book
book={
    "title":"Percy Jackson",
    "pages":436,
    "author":"Rick Riordian",
    "rating":9.9,
    "available":True
}
print(book["available"])

#update
student["age"]=15
print(student)

#add
student["grade"]=10
print(student)

#delete
del student["age"]
print(student)

#String Manipulation
message="Hello, Python World!"
print("Original message:",message)
print("Length of message:",len(message))
print("Uppercase:",message.upper())
print("Lowercase:",message.lower())
print("Does the message contain 'world'?", "World" in message)
print("First 5 Characters:",message[:5])
print("Last 6 Characters:",message[-6:])
print(message[2:6])

greeting="Hi There!"
combined=greeting+" "+message
print(combined)
new_message=combined.replace("There!", "Viswa!")
print(new_message)