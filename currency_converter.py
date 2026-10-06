#Currency Converter
import requests

currencies = {
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Shekel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Krona",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
}

try:
    amount = float(input("Enter amount: "))

except ValueError:
    print('Please enter a valid number')

def input():

    from_= input("Enter base currency: ")

    to = input("Enter target currency: ")
    
    return from_ and to

def currency():

    from_, to = input()

    if from_ and to in currencies:

        currency_API = requests.get(f"https://api.frankfurter.dev/v1/latest?base={from_}&symbols={to}")

        currency = currency_API.json()

        converted_amount = currency['rates'][to]*amount 

        print(f"{amount} {from_} = {converted_amount} {to}")

    else:
        print('Please enter a valid currency code')
    return
currency