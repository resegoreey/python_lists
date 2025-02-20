#Accessing List Elements
fruits_list = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Granadilla", "Strawberry"]
print(f"Fruits = {fruits_list}")
print("Which fruit index do you want to access?")
user_choice = int(input("Enter an index  from 0-6: "))
accessed = fruits_list[user_choice]
print(f"Your fruit is {accessed}")
print()

#List Slicing
#we will be using the same list as the one from the first program
print()
print(f"Fruits = {fruits_list}")
print("Provide 2 numbers (0-7) to get a new list with accessed items from the list")
range_1 = int(input("Enter the 1st number: "))
range_2 = int(input("Enter the 2nd number: "))

subset =  fruits_list[range_1:range_2]
print(f"Here is your accessed items {subset}")
print()

#List Concatenation
list1 = ["a", "b", "c", "d"]
list2 = ["e", "f", "g", "h"]
print(f"""list 1 = {list1}
list 2 = {list2}""")
list1.extend(list2)
print(f"Your new list is: {list1}")
print()

#List Repetition
print(f"List of fruits: {fruits_list}")
repeat_number = int(input("How many time would you like to repeat the list?: "))
repeated_list = fruits_list * repeat_number
print(repeated_list)
print()

#List Length
print("Let's find the length of our lists")
print(f"fruits List = {fruits_list}")
print(f"The length of the fruits list is: {len(fruits_list)}")
print(f"List 1 = {list1}")
print(f"The length of l1ist is: {len(list1)}")
print(f"List 2 = {list2}")
print(f"The length of l1ist is: {len(list2)}")
print()

#Modify List
print(f"""We will use the fruits list
fruits = {fruits_list}""")
#user should enter the index of the item they want to modify
user_index = int(input("Enter the index of the item you want to change: "))

#user then enters the value they want to replace the item with
item_replacement = input("What would you like to replace the item with?: ")
#modify the item based on the index
fruits_list[user_index] = item_replacement
print(f"""Here is the list with your replacement:
fruits = {fruits_list}""")
print()

#Add and Remove Elements
print(f"fruits = {fruits_list}")

#user chooses the fruit to add at the end of the list
add_item = input("Which fruit would you like to add? ")

#the item is added to the list using the append method
fruits_list.append(add_item)
print(f"""Here is your list with the item you added:
fruits = {fruits_list}""")

#user chooses which fruit they would like to remove
remove_item = input("Which fruit would you like to remove? ")

#the item is removed using the remove method
fruits_list.remove(remove_item)
print(f"""Here is your modified list with the item removed:
fruits = {fruits_list}""")
print()

#Find Element in List
print(f"fruits = {fruits_list}")
#user checks if a fruit is in the fruits list
check_item = input("Which fruit do you want to check? ")
if check_item in fruits_list:
    print(f"{check_item} is in fruit list")
else:
    print(f"{check_item} is not in the fruits list")

#List to String Conversion
theList = ["Hello", "World!"]
print(f"Here is the list: {theList}")
new_string = ' '.join(theList)
print(new_string)