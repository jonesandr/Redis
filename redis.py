import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def add_word():
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    r.set(word, meaning)

def search_word():
    word = input("Enter the word to search for its meaning: ")
    meaning = r.get(word)
    if meaning:
        print(meaning.decode("utf-8"))
    else:
        print("This word does not exist")

def delete_word():
    word = input("Enter the word to delete: ")
    r.delete(word)

def list_words():
    words = r.keys("*")
    for word in words:
        print(word.decode("utf-8"))

def edit_word():
    word = input("Enter the word to edit: ")
    meaning = input("Enter the new meaning: ")
    r.set(word, meaning)

while True:
    print("\n......MENU.......\n")
    print("1. Add a word")
    print("2. Search for a word")
    print("3. Delete a word")
    print("4. List all words")
    print("5. Edit a word")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_word()
    elif choice == 2:
        search_word()
    elif choice == 3:
        delete_word()
    elif choice == 4:
        list_words()
    elif choice == 5:
        edit_word()
    elif choice == 6:
        break
    else:
        print("Invalid choice")