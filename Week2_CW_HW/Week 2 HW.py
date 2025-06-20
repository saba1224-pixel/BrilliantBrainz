#list
vowels={"a","o","u","e","i"}
print("Vowels are ", vowels)

#dictionary
movie={"Name":"Avengers", "Year":2018, "Duration":3.5, "Director":"J.J. Abrams"}
print(movie)
del movie["Director"]
print(movie)
#add
movie["Actors"]="Robert Downey Jr., Chris Evans"
print(movie)

#string manipulation
message="Avengers"
message1="Assemble"
combined=message+" "+message1
print(combined)
print("The length of the message is", len(combined))
print("Last 8 Characters:",combined[-8:])