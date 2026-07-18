# Dictionary Mini Project

dictionary = {}

while True:
    print("\n===== DICTIONARY MENU =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Meaning")
    print("4. Delete Word")
    print("5. Display All Words")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        word = input("Enter word: ").lower()
        meaning = input("Enter meaning: ")

        dictionary[word] = meaning
        print("Word added successfully!")

    elif choice == "2":
        word = input("Enter word to search: ").lower()

        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found!")

    elif choice == "3":
        word = input("Enter word to update: ").lower()

        if word in dictionary:
            meaning = input("Enter new meaning: ")
            dictionary[word] = meaning
            print("Meaning updated successfully!")
        else:
            print("Word not found!")

    elif choice == "4":
        word = input("Enter word to delete: ").lower()

        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully!")
        else:
            print("Word not found!")

    elif choice == "5":
        if len(dictionary) == 0:
            print("Dictionary is empty!")
        else:
            print("\nDictionary Contents:")
            for word, meaning in dictionary.items():
                print(word, ":", meaning)

    elif choice == "6":
        print("Thank you for using Dictionary Mini Project!")
        break

    else:
        print("Invalid choice! Please enter between 1 and 6.")