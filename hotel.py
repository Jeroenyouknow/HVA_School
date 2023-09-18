# • variabelen van minimaal de datatypen: boolean, int, string, float
# • leest en bewerkt input
# • schrijft informatie naar de output
# • bewerkt en toont informatie van minimaal 1 list.
# • bevat controle- en lus-structuren
# • maakt gebruik van minimaal één externe module
# • bevat minimaal één functie.
# • voldoet aan de coding conventions
# Maker: Jeroen Huiskes Programma Doel: Simpel programma waarin een boeking kan worden gemaakt, verwijderd en worden aangepast. Daarnaast kan er worden ingecheckt en uitgechekt
import random
import time
import datetime
import json


def main_menu():
    print("Welkom bij Hotel Huiskes!\n Wat wilt u doen vandaag?\n")
    print("1. Boek een kamer")
    print("2. inchekcen")
    print("3. Uitchecken")
    print("4. Afsluiten\n")
    choice_main_menu = input("--> ")
    return choice_main_menu


def main_menu_choice(number):
    if number == "1":
        room_booking()

    elif number == "2":
        check_in()


    elif number == "3":
        check_out()


    elif number == "4":
        exit()


def room_booking():
    print("U heeft gekozen om een kamer te boeken. Hiervoor hebben we wat gegevens nodig:\n")
    booking_name = input("Uw naam:\n --> ")
    age_on_booking = input("Geef uw leeftijd:\n --> ")
    booked_nights = input("Hoeveel nachten wilt u verblijven:\n --> ")
    total_persons = input("Met hoeveel personen wilt u " + booked_nights + " nachten blijven:\n --> ")
    booking_number = random.randrange(111111, 999999).__str__()
    room_number = room_assign(total_persons, booked_nights)

    print("Bedankt voor je boeking " + booking_name + " hieronder nemen we uw boeking door:")
    print("Persoonlijke gegevens: \n Naam: " + booking_name + "\n Geboortedatum:" + age_on_booking)
    print("Verblijf gegevens: \n Aantal nachten:" + booked_nights + "\n Aantal personen:" + total_persons)

    check = input("Klopt dit? Y/N \n --> ").lower()
    if check == "y":
        print("Bedankt voor uw boeking!\n Uw boekingsnummer is: " + booking_number +
              " en uw kamernummer is: " + room_number)
        booking_conformation = {
            "NameonBooking": booking_name,
            "Age": age_on_booking,
            "NightsonBooking": booked_nights,
            "PersonsonBooking": total_persons,
            "Bookingsnumber": booking_number,
            "Roombooked": room_number
        }
        file = open("bookings.txt", "a")
        file.write(booking_conformation.__str__())
        file.close()
    elif check == "n":
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    else:
        print("U heeft geen geldige waarde ingevoerd u word terug gestuurd!")
        time.sleep(5)
        main_menu_choice(main_menu())


def change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number):
    choice = int(input("Welke gegevens wilt u veranderen?\n"
                       "1. Naam op de boeking \n"
                       "2. Geboorte datum \n"
                       "3. Aantal geboekte nachten \n"
                       "4. Aantal personen \n"
                       "5. Niks, verder met boeken \n"
                       "--> "))
    if choice == 1:
        new_booking_name = input("Geef de naam op de boeking: \n --> ")
        booking_name = new_booking_name
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 2:
        new_age_on_booking = input("Geef uw leeftijd: \n --> ")
        age_on_booking = new_age_on_booking
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 3:
        new_booked_nights = input("Geef de aantal nachten: \n --> ")
        booked_nights = new_booked_nights
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 4:
        new_total_persons = input("Geef de aantal personen")
        total_persons = new_total_persons
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 5:
        room_number = room_assign(total_persons, booked_nights)
        check = input("Klopt dit? Y/N \n --> ").lower()
        if check == "y":
            print("Bedankt voor uw boeking!\n Uw boekingsnummer is: " + booking_number +
                  " en uw kamernummer is: " + room_number)
            booking_conformation = {
                "NameonBooking": booking_name,
                "Age": age_on_booking,
                "NightsonBooking": booked_nights,
                "PersonsonBooking": total_persons,
                "Bookingsnumber": booking_number,
                "Roombooked": room_number
            }
            file = open("bookings.txt", "a")
            file.write(booking_conformation.__str__())
            file.close()
    else:
        print("U heeft geen geldige waarde ingevoerd u word terug gestuurd!")
        time.sleep(5)
        main_menu_choice(main_menu())


def room_assign(persons, nights):
    room_101 = ["101", 2, 25.50, True]
    room_102 = ["102", 4, 50.75, True]
    room_103 = ["103", 6, 60.99, True]
    room_104 = ["104", 8, 75.20, True]
    room_105 = ["105", 10, 100.99, True]
    rooms = room_101 + room_102 + room_103 + room_104 + room_105
    print(room_101[1])
    # room_cost(nights, rooms
    # room_number = "We konden geen kamer vinden"
    if int(persons) <= room_101[1]:
        room_number = "101"
    elif int(persons) <= room_102[1]:
        room_number = "102"
    elif int(persons) <= room_103[1] and room_103[2] == True:
        room_number = "103"
    elif int(persons) <= room_104[1] and room_104[2] == True:
        room_number = "104"
    elif int(persons) <= room_105[1] and room_105[2] == True:
        room_number = "105"

    return room_number


def room_cost(nights, rooms):
    print(rooms)


def check_in():
    print("U heeft gekozen om in te checken, houd u boekingsnummer bij de hand.")
    bookings = open("bookings.txt")
    booking_number = input("Geef uw boekingsnummer:\n --> ")
    lines_in_file = bookings.readlines()
    for line in lines_in_file:
        if line.find(booking_number) != -1:
            print(booking_number, "Boekingsnummer bestaat!")
            print("Gegevens van uw boeking: \n", line)
    exit()


def check_out():
    bookings = open("bookings.txt")
    booking_number = input("Geef uw boekingsnummer: \n")
    lines = bookings.readlines()
    for line in lines:
        if line.find(booking_number) != -1:
            print(booking_number, "Boekingsnummer bestaat!")
            print("U had het volgende geboekt: \n", line)
            print("U gaat nu uitchecken moment geduld.....")
            time.sleep(1)
            print("Bedankt voor uw bezoek aan Hotel Huiskes")
            exit()


if __name__ == '__main__':
    main_menu_choice(main_menu())
