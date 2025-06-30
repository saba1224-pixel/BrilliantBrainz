grade=65
if grade>=70:
    print("you passed")
else:
    print("you fail")
    
number=25
if number%5==0:
    print("number is a multiple of 5")
else:
    print("number is not a multiple of 5")
    
numbers=[1,2,3,4,5]
sum=0
for i in range (1,6):
    sum=sum+i
print(sum)

numbers=[1,2,3,4,5]
sum=0
for i in numbers:
    sum=sum+i
print(sum)

word="JianHao Tan"
for letter in word:
    print(letter)

print(len(word))
print(word[::-1])

number=5
sum=0
print(f"Multiplication table of {number}:")
for i in range (1,101):
    print(f"{number}*{i}={number*i}")
    if i%5==0:
        print("number is a multiple of 5")
        sum=sum+i
    else:
        print("number is not a multiple of 5")
print(sum) 

name=["Amaani","Arjun","Viswa","Tanush"]
for i in name:
    print("Hello",i)

count=5
while count>0:
    print(count)
    count=count-1
    print(count)