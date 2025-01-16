import pandas as pd

while True:
    print('''Welcome, this is a small practice program that displays City Pop Albums.
(1) Display whole table.
(2) Search for album by name.
(3) Search for album by release year.
(4) Search for album by artist.
(5) Exit program.''')
    user_input = input("Please select an action by typing a number: ")
    if user_input == '1':
        csv_file = pd.read_csv('city_pop_albums.csv')
        print(csv_file)
        input()
    elif user_input == '5':
        print("Exiting program...")
        break