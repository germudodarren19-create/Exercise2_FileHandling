try:
    note1 = input("Enter your first note: ")

    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")

    print("\nSaved successfully!")

    with open("notes.txt", "r") as file:
        print("\nCurrent Content:")
        print(file.read())

    note2 = input("\nEnter another note: ")

    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")

    with open("notes.txt", "r") as file:
        print("\nUpdated Content:")
        print(file.read())

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)
    