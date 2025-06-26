# Chat Application - Task 3

print("Welcome to Chat Application!")
print("Type 'exit' to end the chat.\n")

while True:
    user1 = input("User1: ")
    if user1.lower() == "exit":
        print("Chat ended by User1.")
        break

    user2 = input("User2: ")
    if user2.lower() == "exit":
        print("Chat ended by User2.")
        break

    print(f"\n--- Chat ---")
    print(f"User1: {user1}")
    print(f"User2: {user2}")
    print("------------\n")
