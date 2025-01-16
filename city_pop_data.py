import pandas as pd
import os
df = pd.read_csv('city_pop_albums.csv')

while True:
    print('''Welcome, this is a small practice program that displays City Pop Albums.
    (1) Display whole table.
    (2) Search for album by name.
    (3) Search for album by release year.
    (4) Search for album by artist.
    (5) Exit program.''')
    user_input = input("Please select an action by typing a number: ")
    if user_input == '1':
        print(df)
        input()
        os.system('cls')
    elif user_input == '2':
        user_search = input("Search for album by name: ")
        results = df[df['Album Title'].str.contains(user_search, case=False)]
        if results.empty:
            print("No results found.")
        else:
            print(results)
        input()
        os.system('cls')
    elif user_input == '3':
        while True:
            try:
                user_search = input("Search for album by release year: ")
                int(user_search)
                break
            except ValueError:
                print("Please enter a number and try again.")
                continue
        results = df[(df['Release Year'] == int(user_search))]
        if results.empty:
            print("No results found.")
        else:
            print(results)
        input()
        os.system('cls')
    elif user_input == '4':
        user_search = input("Search for album by artist: ")
        results = df[df['Artist'].str.contains(user_search, case=False)]
        if results.empty:
            print("No results found.")
        else:
            print(results)
        input()
        os.system('cls')
    elif user_input == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid input, please try again.")
        input()
        continue