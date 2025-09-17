print("Welcome to the Mad Libs Generator!")
print("Choose a story:")
print("1. A Day at the Zoo")
print("2. Space Adventure")

choice = input("Enter 1 or 2: ")

if choice == "1":
#Zoo Story
    adjective = input("Use an adjective to describe the day: ")
    adjective2 = input("Describe how the animal is like: ")
    adjective3 = input("Describe how the animal is like:")
    adjective4 = input("NDescribe your experience: ")

    print(f"On a beautiful {adjective} day, I went to the zoo.I saw a funny {adjective2} monkey swinging from the trees.Then, I spotted a majestic {adjective3} lion lounging in the sun. What a wild and {adjective4} experience!")

elif choice == "2":
    # Space story
    noun = input("Enter a planet: ")
    verb = input("Enter a verb: ")
    objects = input("Enter an object: ")

    print(f"I traveled to {noun} and had to {verb} with a {objects} to survive!")

else:
    print("Invalid choice. Please restart the game and choose 1 or 2.")
