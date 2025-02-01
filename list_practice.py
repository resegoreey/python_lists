print()
fruits_list = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Granadilla", "Strawberry"]
print(f"Fruits = {fruits_list}")
print()
print("Which fruit index do you want to access?")
user_choice = int(input("Enter an index  from 0-6: "))
accessed = fruits_list[user_choice]
print()
print(f"Your fruit is {accessed}")