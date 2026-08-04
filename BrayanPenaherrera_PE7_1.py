# Brayan Penaherrera, 04/27/2026, BrayanPenaherrera_PE7_1.py
# This program reads World Series Winners from a csv file and it allows the user to search winners by team or by a range of years.

import csv


def load_data():
    winners = []

    with open("WorldSeriesWinners.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            year = int(row[0])
            team = row[1]
            winners.append([year, team])

    return winners


def display_menu():
    print()
    print("World Series Winners")
    print("1. Display winners by team")
    print("2. Display winners by years")
    print("3. End program")


def display_by_team(winners):
    team_name = input("\nenter team name ")

    years_won = []

    for item in winners:
        year = item[0]
        team = item[1]

        if team_name.lower() in team.lower():
            years_won.append(year)

    if len(years_won) == 0:
        print("\nNo winners found for that team.")
    else:
        print()
        print("The " + team_name.title() + " won the series in")

        count = 0

        for year in years_won:
            print(year, end=" ")
            count += 1

            if count == 5:
                print()
                count = 0

        print()


def display_by_years(winners):
    beginning_year = int(input("\nenter beginning year "))
    ending_year = int(input("enter ending year "))

    print()
    print("World Series Winners by Year")

    found = False

    for item in winners:
        year = item[0]
        team = item[1]

        if year >= beginning_year and year <= ending_year:
            print(str(year) + " >> " + team)
            found = True

    if found == False:
        print("No winners found for those years.")


def main():
    winners = load_data()

    choice = "0"

    while choice != "3":
        display_menu()
        choice = input("enter choice ")

        if choice == "1":
            display_by_team(winners)
        elif choice == "2":
            display_by_years(winners)
        elif choice == "3":
            print("\nProgram ended.")
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


main()
