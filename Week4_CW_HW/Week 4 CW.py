word="Goon"
for letter in word:
    print(letter)
length=len(word)
print("Length of the word =", length)
reversed_word=word[::-1]
print(reversed_word)

number=5
sum=0
for i in range(1,101):
    if i%5==0:
        sum=sum+i
print(sum)

names=["Amaani", "Viswa", "Arjun", "Tanush"]
for i in names:
    print("Hello", i)

i=5
while i>=1:
    print(i)
    i=i-1
        