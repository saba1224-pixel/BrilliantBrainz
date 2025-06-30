colors=["red","green","blue","yellow"]
print(colors[0])
print(colors[-1])

numbers=1
print(f"Numbers table that increases by {numbers}:")
for i in range(0,5):
    print(f"{numbers}+{i}={numbers+i}")
    
fruits=["apple","banana","kiwi","mango"]
print(fruits)
fruits.remove("banana")
fruits.remove("mango")
print(fruits)

number_list1=[5,4,8,9,15]
number_list1.sort()
print(number_list1)

number_list2=[1,2,3,4,5]
number_list2.remove(1)
number_list2.remove(5)
print(number_list2)

number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24]
for x in number1:
    print(f"{x} is even")
    if x==16:
        break
    
number2 = [5,10,15,20,25,30,35]
number3 = 1
print("This is the multiplication table of 5 until 25:")
for n in number2:
    print(f"{number3}*{n}={number3*n}")
    if n==25:
        break


    

    

   