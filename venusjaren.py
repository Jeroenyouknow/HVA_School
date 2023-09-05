# Auteur Jeroen Huiskes  Goal: Asking a user for his name and age, so it can calculate his age and his venus age.
import datetime


# Ask the user for his age and name, This will be returned for the functions calculate_age and calculate_venus_age.
def input_information():
    name = input("Hoe heet je? \n --> ")
    age = input("Wat is je geboortejaar? \n --> ")
    return name, int(age)


# The given age(year) needs to be given with this function, then the current date and year are being made.
# The current age is calculated by current year - the age that is given (2023-1997) for example.
# The number and current year are returned in the function, only the age_on_earth is given as INT because this needs to be calculated after
def calculate_age(age):
    current_date = datetime.date.today()
    current_year = current_date.year
    age_on_earth = current_year - age
    return int(age_on_earth), current_year


# The given age (age_on_earth) is used to calculate the venus age. This is done by the formula age_on_earth * 1.62
# The age on venus is given back as float as is shown in the example
def calculate_venus_age(age_on_earth):
    age_on_venus = age_on_earth * 1.62
    return float(age_on_venus)


# In the main i start with calling the first fucntion Input Information, The return values are stored in the variable input
# The variable age_on_earth calls the function calculate age, i use from input the return function and i want the given age so in the given list use [1]
# The variable age_on_venus calls the function calculate_venus_age, i use from age_on_earth the retun function and i want the given age in the giveb list use [0]
# Then i print the text as shown in the exmaple i use __str__() to change the INT and Float to Strings.
if __name__ == '__main__':
    input = input_information()
    age_on_earth = calculate_age(input[1])
    age_on_venus = calculate_venus_age(age_on_earth[0])
    print("Beste " + input[0] + ", in " + age_on_earth[1].__str__() + " zal je leeftijd op aarde " + age_on_earth[
        0].__str__() + " zijn.")
    print("En je leeftijd is dan " + age_on_venus.__str__() + " in Venusjaren")
