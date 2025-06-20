#List of vowels
Vowels=["A","E","I","O","U"]
print(Vowels)
#Movie Dictionary
Avengers_Dictionary={"name":"Avengers","year":"2018","duration":"3.5","director":"J.J.Abrams"}
print(Avengers_Dictionary["name"])
del Avengers_Dictionary["director"]
print(Avengers_Dictionary)
Avengers_Dictionary["actors"]="Chris Evans, Chris Hemsworth"
print(Avengers_Dictionary)
print(Avengers_Dictionary["actors"])
#String Concatenation
title="Avengers"
message="Assemble"
full_message=title+" "+message
print(full_message)
#Length of String Concatenation
print("Length of full message:",len(full_message))
print("Last 8 letters:",full_message[-8:])