# Maker: Jeroen Huiskes Programma Goal: Simple program where you can book a room, check in and check out
# Please note that a file bookings.txt will made by the first RUN
import json
import random
import time


# This function is a simple menu where the programm always will go back, i return the choice made by the user.
def main_menu():
    print(
        "Welkom bij Hotel Huiskes \n" + "Wat wilt u doen vandaag? \n" + "1. Boek een kamer\n" + "2. Inchecken\n" + "3. Uitchecken\n" + "4. Afsluiten")
    choice_main_menu = int(input("--> "))
    return choice_main_menu


# Given the choice made in main_menu() the function connected to it will run.
def main_menu_choice(number):
    if number == 1:
        room_booking()
    elif number == 2:
        check_in()
    elif number == 3:
        check_out()
    elif number == 4:
        exit()


# This function makes the booking, in the function the fucntion room_assing() will be called
# This will give the room number and cost of the total stay.
# A user need to be over 18 to book! When the user is not satisfied with the data he can change it trough function change booking
# If the user agrees with the data the booking and data is stored as JSON in bookings.txt
def room_booking():
    print("Leuk om te horen dat u een kamer wilt boeken! Wilt u de volgende gegevens invullen?\n")
    booking_name = input("Geef uw naam:\n --> ")
    age_on_booking = int(input("Geef uw leeftijd:\n --> "))
    if age_on_booking < 18:
        print("Sorry onder de 18 kunt u niet boeken!")
        exit()
    booked_nights = input("Hoeveel nachten wilt u verblijven:\n --> ")
    total_persons = input("Met hoeveel personen wilt u " + booked_nights + " nachten blijven:\n --> ")
    booking_number = random.randrange(111111, 999999).__str__()
    room_number = room_assign(total_persons, int(booked_nights))

    print(
        "Bedankt voor je boeking " + booking_name + " hieronder nemen we uw boeking door:\n" + "Persoonlijke gegevens: \n Naam: " + booking_name + "\n Leeftijd:" + age_on_booking.__str__() + "\n" + "Verblijf gegevens: \n Aantal nachten:" + booked_nights + "\n Aantal personen:" + total_persons + "\n" + "De totale prijs voor " + booked_nights + " nachten komt met kamernummer " +
        room_number[0] + " uit op een totaal van: " + room_number[1].__str__() + " euro.")

    check = input("Klopt dit? Y/N \n --> ").lower()
    if check == "y":
        print("Bedankt voor uw boeking!\n Uw boekingsnummer is: " + booking_number + " en uw kamernummer is: " +
              room_number[0])
        booking_conformation = {"NameonBooking": booking_name, "Age": age_on_booking, "NightsonBooking": booked_nights,
            "PersonsonBooking": total_persons, "Bookingsnumber": booking_number, "Roombooked": room_number[0],
            "Totalprice": room_number[1], "Activebooking": True}
        booking_conformation_json = json.dumps(booking_conformation)
        file = open("bookings.txt", "a")
        file.write(booking_conformation_json + "\n")
        file.close()
        main_menu_choice(main_menu())
    elif check == "n":
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    else:
        print("U heeft geen geldige waarde ingevoerd u word terug gestuurd!")
        time.sleep(5)
        main_menu_choice(main_menu())


# This is a same function as room_booking() only in this fucntion evrey part can be changed before the booking is made
# When the data is correct it is stored as JSON in bookings.txt
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
        new_age_on_booking = int(input("Geef uw leeftijd: \n --> "))
        if new_age_on_booking < 18:
            print("Sorry onder de 18 kunt u niet boeken!")
            exit()
        age_on_booking = new_age_on_booking
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 3:
        new_booked_nights = input("Geef de aantal nachten: \n --> ")
        booked_nights = new_booked_nights
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 4:
        new_total_persons = input("Geef de aantal personen: \n -->")
        total_persons = new_total_persons
        change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    elif choice == 5:
        room_number = room_assign(total_persons, int(booked_nights))
        print(
            "Bedankt voor je boeking " + booking_name + " hieronder nemen we uw boeking door:\n" + "Persoonlijke gegevens: \n Naam: " + booking_name + "\n Leeftijd:" + age_on_booking.__str__() + "\n" + "Verblijf gegevens: \n Aantal nachten:" + booked_nights + "\n Aantal personen:" + total_persons + "\n" + "De totale prijs voor " + booked_nights + " nachten komt met kamernummer " +
            room_number[0] + " uit op een totaal van: " + room_number[1].__str__() + " euro.")
        check = input("Klopt dit? Y/N \n --> ").lower()

        if check == "y":
            print("Bedankt voor uw boeking!\n Uw boekingsnummer is: " + booking_number + " en uw kamernummer is: " +
                  room_number[0])
            booking_conformation = {"NameonBooking": booking_name, "Age": age_on_booking,
                "NightsonBooking": booked_nights, "PersonsonBooking": total_persons, "Bookingsnumber": booking_number,
                "Roombooked": room_number[0], "Totalprice": room_number[1], "Activebooking": True}
            booking_conformation_json = json.dumps(booking_conformation)
            file = open("bookings.txt", "a")
            file.write(booking_conformation_json + "\n")
            file.close()
        elif check == "n":
            change_booking(booking_name, age_on_booking, booked_nights, total_persons, booking_number)
    else:
        print("U heeft geen geldige waarde ingevoerd u word terug gestuurd!")
        time.sleep(5)
        main_menu_choice(main_menu())


# In this function the rooms are made and set as follow: number of room, max persons, price per night
# With the nighst there is calculated a cost, the room number is chosen by the persons
# The cost and room number are returned
def room_assign(persons, nights):
    room_101 = ["101", 2, 25.50]
    room_102 = ["102", 4, 50.75]
    room_103 = ["103", 6, 60.99]
    room_104 = ["104", 8, 75.20]
    room_105 = ["105", 10, 100.99]

    if int(persons) <= room_101[1]:
        room_number = "101"
        cost_of_room = nights * room_101[2]
    elif int(persons) <= room_102[1]:
        room_number = "102"
        cost_of_room = nights * room_102[2]
    elif int(persons) <= room_103[1]:
        room_number = "103"
        cost_of_room = nights * room_103[2]
    elif int(persons) <= room_104[1]:
        room_number = "104"
        cost_of_room = nights * room_104[2]
    elif int(persons) <= room_105[1]:
        room_number = "105"
        cost_of_room = nights * room_105[2]
    else:
        print("Helaas hebben wij geen kamer kunnen vinden voor: " + persons + " personen!")
        main_menu_choice(main_menu())

    return room_number, round(cost_of_room, 2)


# This function will check if the bookingsnumber exists and "Check in" the guest
# The data is gotten from bookings.txt in JSON format
# In this current version it only shows text
def check_in():
    bookings = open("bookings.txt", "r")
    booking_number = input("Geef uw boekingsnummer: \n --> ")
    lines = bookings.readlines()
    for line in lines:
        bookings_json = json.loads(line)
        all_booking_numbers = bookings_json["Bookingsnumber"]
        if all_booking_numbers == booking_number and bookings_json["Activebooking"] == True:
            print("we hebben uw boeking gevonden!")
            print("Weet u zeker dat u wilt inchecken van de volgende boeking: \n" + "Boekingsnummer: " + str(
                bookings_json["Bookingsnumber"]) + "\n" + "Naam op boeking: " + str(
                bookings_json["NameonBooking"]) + "\n" + "Leeftijd op boeking: " + str(
                bookings_json["Age"]) + "\n" + "Aantal nachten: " + str(
                bookings_json["NightsonBooking"]) + "\n" + "Aantal personen: " + str(bookings_json["PersonsonBooking"]))
            accept_booking = input("Wilt u inchecken? Y/N\n" + "--> ").lower()

            if accept_booking == "y":
                print("U bent ingecheckt wij wensen u een fijne dag verder!")
                time.sleep(10)
                print("U keert nu terug naar het menu")
                main_menu_choice(main_menu())

            elif accept_booking == "n":
                print("U bent niet ingecheckt, u keert terug naar het menu.")
                main_menu_choice(main_menu())

            else:
                print("U heeft geen geldige invoer gegeven, u keert terug naar het menu")
                main_menu_choice(main_menu())
        elif all_booking_numbers == booking_number and bookings_json["Activebooking"] == False:
            print(
                "Helaas is uw boeking niet meer geldig! \n" + "Wij verzoeken u om naar een medewerker te gaan met uw boekingsnummer: " + booking_number)
            main_menu_choice(main_menu())

    else:
        print("Helaas hebben we uw boeking niet kunnen vinden")
        main_menu_choice(main_menu())


# This function will check if the bookingsnumber exists and "Check out" the guest
# The data is gotten from bookings.txt in JSON format
# In this current version it only shows text
def check_out():
    bookings = open("bookings.txt", "r")
    booking_number = input("Geef uw boekingsnummer: \n")
    lines = bookings.readlines()
    for line in lines:
        bookings_json = json.loads(line)
        all_booking_numbers = bookings_json["Bookingsnumber"]
        if all_booking_numbers == booking_number and bookings_json["Activebooking"] == True:
            print("we hebben uw boeking gevonden!")
            print("Weet u zeker dat u wilt uitchecken van de volgende boeking: \n" + "Boekingsnummer: " + str(
                bookings_json["Bookingsnumber"]) + "\n" + "Naam op boeking: " + str(
                bookings_json["NameonBooking"]) + "\n" + "Leeftijd op boeking: " + str(
                bookings_json["Age"]) + "\n" + "Aantal nachten: " + str(
                bookings_json["NightsonBooking"]) + "\n" + "Aantal personen: " + str(bookings_json["PersonsonBooking"]))
            delete_booking = input("Wilt u uitchecken? Y/N" + "--> ").lower()

            if delete_booking == "y":
                print("U bent uitgecheckt wij wensen u een fijne dag verder!")
                main_menu_choice(main_menu())

            elif delete_booking == "n":
                print("U bent niet uitgecheckt, u keert terug naar het menu.")
                main_menu_choice(main_menu())

            else:
                print("U heeft geen geldige invoer gegeven, u keert terug naar het menu")
                main_menu_choice(main_menu())
        elif all_booking_numbers == booking_number and bookings_json["Activebooking"] == False:
            print(
                "Helaas is uw boeking niet meer geldig! \n" + "Wij verzoeken u om naar een medewerker te gaan met uw boekingsnummer: " + booking_number)
            main_menu_choice(main_menu())

    else:
        print("Helaas hebben we uw boeking niet kunnen vinden")
        main_menu_choice(main_menu())


# Starting of the program
if __name__ == '__main__':
    main_menu_choice(main_menu())
