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