supported_currencies = {
    "USD": "(US Dollar)",
    "CAD": "(Canadian Dollar)",
    "EUR": "(Euro)",
    "GBP": "(Great Britain Pound)"
}


# USD below here
def usd_to_cad():
    user_value = input("How many U.S. Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.77
    print(str(user_value) + " U.S. Dollars " + str(conversion) + " Canadian Dollars.")


def usd_to_eur():
    user_value = input("How many U.S. Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.90
    print(str(user_value) + " U.S. Dollars " + str(conversion) + " Euros.")


def usd_to_gbp():
    user_value = input("How many U.S. Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.77
    print(str(user_value) + " U.S. Dollars " + str(conversion) + " Euros.")


# USD above here

# CAD below here
def cad_to_usd():
    user_value = input("How many U.S. Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.77
    print(str(user_value) + " U.S. Dollars " + str(conversion) + " Euros.")


print("Welcome to currency converter.")
print("Supported currencies:")
for currency in supported_currencies:
    print(currency + " " + supported_currencies[currency])

starting_value = input("Convert: ")
end_value = input("To: ")

if starting_value == "CAD" and end_value == "USD":
    cad_to_usd()

elif starting_value == "USD" and end_value == "CAD":
    usd_to_cad()
