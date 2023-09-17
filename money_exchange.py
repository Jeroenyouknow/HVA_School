# Author: Jeroen Huiskes, Simple program for exchange of valuta

# The user puts in which currency he wats to exchange and how much. Returned will be both choices
def currency_choice_and_value():
    currency_to_exchange = int(input("Welke valuta wilt u wisselen? \n 1.US-Dollar \n 2.GB-Pounds \n 3.Yen \n --> "))
    value_to_exchange = int(input("Hoeveel wilt u wisselen?: \n --> "))
    if currency_to_exchange == 1 or currency_to_exchange == 2 or currency_to_exchange == 3:
        return currency_to_exchange, value_to_exchange
    else:
        print("U heeft geen geldige waarde gegeven, probeer het opnieuw")
        exit()


# With the give currency and value the exchange to euro will be calculated and returned
def calculate_return_to_euro(currency_to_exchange, value_to_exchange):
    usd_to_eur = 0.94
    gb_to_eur = 1.16
    yen_to_eur = 0.0063
    receive_in_euro = 0

    if currency_to_exchange == 1:
        receive_in_euro = usd_to_eur * value_to_exchange
    elif currency_to_exchange == 2:
        receive_in_euro = gb_to_eur * value_to_exchange
    elif currency_to_exchange == 3:
        receive_in_euro = yen_to_eur * value_to_exchange
    return round(receive_in_euro, 2)


# The cost of the transaction in EURO will be calculated and returned
def calculate_transaction_cost(receive_in_euro):
    transaction_percentage = 0.015
    cost_of_transaction = receive_in_euro * transaction_percentage
    if cost_of_transaction <= 2:
        cost_of_transaction = 2
    elif cost_of_transaction >= 15:
        cost_of_transaction = 15
    return round(cost_of_transaction, 2)


# The total to be returned in euro will be calculated with the withdrawal of the transaction cost
def output_calculation(receive_in_euro, cost_of_transaction):
    total_to_receive_in_euro = receive_in_euro - cost_of_transaction
    round(total_to_receive_in_euro, 2)
    print("U krijgt het volgende bedrag terug: " + receive_in_euro.__str__() + " Euro" +
          "\n De transactie kosten hiervan zijn: " + cost_of_transaction.__str__() + " Euro" +
          "\n Totaal ontvangt u: " + total_to_receive_in_euro.__str__() + " Euro")


if __name__ == '__main__':
    value_and_choice = currency_choice_and_value()
    return_in_euro = calculate_return_to_euro(value_and_choice[0], value_and_choice[1])
    transaction_cost = calculate_transaction_cost(return_in_euro)
    output_calculation(return_in_euro, transaction_cost)
