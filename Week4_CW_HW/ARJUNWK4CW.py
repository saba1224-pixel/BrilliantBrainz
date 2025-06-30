number=50
if number % 5==0:
    print("This number is a multiple of 5!")
else:
    print("This number is NOT a multiple of 5!")
numbers=[1,2,3,4,5]
sum=0
for i in numbers:
    sum=sum+i
print(sum)

word="MANGO"
for letter in word:
    print(letter)
reversed_word = word[::-1]
print(reversed_word)
print("Length of word:", len(word))

number=5
sum=0
for i in range(1,101):
    if i % 5==0:
        sum=sum+i
print(sum)


names=["Amaani", "Vishva", "Arjun", "Tanush"]

for i in names:
    print("Hello", i)
i=1
while i<=5:
    print(i)
    i=i+1


count=5
while count>0:
    print(count)
    count=count-1