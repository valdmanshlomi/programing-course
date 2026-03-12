a = int(input("First number: "))
b = int(input("Second number: "))

print("Choose operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = input("Enter choice: ")

if choice == "1":
    print("Result:", a + b)

elif choice == "2":
    print("Result:", a - b)

elif choice == "3":
    print("Result:", a * b)

elif choice == "4":
    print("Result:", a / b)

else:
    print("Invalid choice")