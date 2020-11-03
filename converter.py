# Copyright: PestControl Labs LLP (d.b.a P.C. Labs // P.C. Lbs)
supported_currencies = {
    "USD": "(US Dollar)",
    "CAD": "(Canadian Dollar)",
    "EUR": "(Euro)",
    "GBP": "(Great Britain Pound)"
}
# Currencies above here

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
    print(str(user_value) + " U.S. Dollars " + str(conversion) + " GBP.")


# USD above here

# CAD below here
def cad_to_usd():
    user_value = input("How many Canadian Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.77
    print(str(user_value) + " Canadian Dollars " + str(conversion) + " U.S. Dollars.")


def cad_to_eur():
    user_value = input("How many Canadian Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.69
    print(str(user_value) + " Canadian Dollars" + str(conversion) + " Euros.")


def cad_to_gbp():
    user_value = input("How many Canadian Dollars? ")
    amount = float(user_value)
    conversion = amount * 0.59
    print(str(user_value) + " Canadian Dollars" + str(conversion) + " GBP.")


# CAD above here

# EUR below here
def eur_to_usd():
    user_value = input("How many Euros? ")
    amount = float(user_value)
    conversion = amount * 1.12
    print(str(user_value) + " Euros " + str(conversion) + " U.S. Dollars.")


def eur_to_cad():
    user_value = input("How many Euros? ")
    amount = float(user_value)
    conversion = amount * 1.12
    print(str(user_value) + " Euros " + str(conversion) + " Canadian Dollars.")


def eur_to_gbp():
    user_value = input("How many Euros? ")
    amount = float(user_value)
    conversion = amount * 0.86
    print(str(user_value) + " Euros " + str(conversion) + " GBP.")

# EUR above here

# GBP below here


def gbp_to_usd():
    user_value = input("How many Pound? ")
    amount = float(user_value)
    conversion = amount * 1.30
    print(str(user_value) + " pounds " + str(conversion) + " U.S. Dollars.")


def gbp_to_cad():
    user_value = input("How many Pound? ")
    amount = float(user_value)
    conversion = amount * 1.70
    print(str(user_value) + " pounds " + str(conversion) + " Canadian Dollars.")


def gbp_to_eur():
    user_value = input("How many Pound? ")
    amount = float(user_value)
    conversion = amount * 1.17
    print(str(user_value) + " pounds " + str(conversion) + " Euros.")


print("Welcome to currency converter.")
print("Supported currencies:")
for currency in supported_currencies:
    print(currency + " " + supported_currencies[currency])

starting_value = input("Convert: ")
end_value = input("To: ")

# USD conversion below here
if starting_value == "USD" and end_value == "CAD":
    usd_to_cad()

elif starting_value == "USD" and end_value == "EUR":
    usd_to_eur()

elif starting_value == "USD" and end_value == "GBP":
    usd_to_gbp()
# USD conversion above here

# CAD conversion below here
elif starting_value == "CAD" and end_value == "USD":
    cad_to_usd()
elif starting_value == "CAD" and end_value == "EUR":
    cad_to_eur()
elif starting_value == "CAD" and end_value == "GBP":
    cad_to_gbp()
# CAD conversion above here

# EUR conversion below here
elif starting_value == "EUR" and end_value == "USD":
    eur_to_usd()
elif starting_value == "EUR" and end_value == "CAD":
    eur_to_cad()
elif starting_value == "EUR" and end_value == "GBP":
    eur_to_gbp()
# EUR conversion above here

# GBP conversion below here
elif starting_value == "GBP" and end_value == "USD":
    gbp_to_usd()
elif starting_value == "GBP" and end_value == "CAD":
    gbp_to_cad()
elif starting_value == "GBP" and end_value == "EUR":
    gbp_to_eur()
# GBP conversion above here

