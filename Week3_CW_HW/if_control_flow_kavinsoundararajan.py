text="Hello"
#To find the first character
print(text[0])
#To find the last character
print(text[-1])
#To find any character
print(text[1])
#Range
print(text[1:4])
print(text[0:4])
#List Manipulation
fruits=["apple","banana","cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
numbers=[1,2,3,4,5]
print(numbers[:3])
#Add cherry
fruits=["apple","banana"]
fruits.append("cherry")
print(fruits)
#Insert kiwi
fruits.insert(1,"kiwi")
print(fruits)
#Remove banana
fruits.remove("banana")
print(fruits)
#Remove first character of list
popped=fruits.pop(0)
print(popped)
print(fruits)
#Reverse and sort
fruits.reverse()
print(fruits)
numbers=[5,90009,90010,3,1]
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
#If statement
age=18
if age>=18:
    print("You can vote!")
else:
    print("You cannot vote!")
number=2
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
