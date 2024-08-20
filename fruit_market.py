# fruit market project
fruits =['apple','banana','strawberry','cherry','mago','watermelon']

print('hello, welcome to the fruit market')
costumer_name = input('what is your Name \n')
number_fruits = len(fruits)
number_pick = len(fruits)-1

# show costumer how many fruits are available & let him pick a fruit based on list index
print('wonderful',costumer_name+', we currently have',number_fruits, 'kinds of fruits available at our market.')
costumer_pick= int(input(f"pick a number between 0 and {number_pick} to try one of them \n"))


fruit_pick = fruits[costumer_pick]
print('you picked',fruit_pick,'try it')

favourite_fruit = input("what fruit would you like to get? \n")
fruit_choice = favourite_fruit in fruits

if fruit_choice == True:
    print("we have",favourite_fruit+"s. Here you go")
else:
    print("I'm sorry but we don't have",favourite_fruit+"s. Maybe next time")


# show costumer a list of all the fruits that are available

# pick a random fruit from the list, let the costumer guess. If they are right, they will get the fruit for free
    