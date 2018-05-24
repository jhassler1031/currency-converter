
#Currency converter
#Actors: Money
#Money - needs to accept an amount and initial currency type (USD)
#       then needs to have methods available to run to return the amount
#       converted into another currency

class Money:

#Start of __init__ method
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.jpy_rate = 110.2
        self.eur_rate = 0.85
        self.xbt_rate = 0.00013


#Start of __str__ method
    def __str__(self):
        return str(self.amount) + " " + self.currency

#Start of convert method

    def convert(self, to_currency):
        conv_amount = 0
        conv_currency = ""

        if to_currency == "JPY":
            conv_amount = self.amount * self.jpy_rate
            conv_currency = "JPY"
        elif to_currency == "EUR":
            conv_amount = self.amount * self.eur_rate
            conv_currency = "EUR"
        elif to_currency == "XBT":
            conv_amount = self.amount * self.xbt_rate
            conv_currency = "XBT"
        else:
            if self.currency == "JPY":
                conv_amount = self.amount / self.jpy_rate
            elif self.currency == "EUR":
                conv_amount = self.amount / self.eur_rate
            elif self.currency == "XBT":
                conv_amount = self.amount / self.xbt_rate
            else:
                conv_amount = self.amount
            conv_currency = "USD"

        return Money(conv_amount, conv_currency)

#Start of conversion to Japanese Yen (JPY)

    def conv_to_jpy(self):
        if self.currency == "JPY":
            return Money(self.amount, self.currency)
        else:
            if self.currency != "USD":
                temp = self.conv_to_usd()
                return temp.conv_to_jpy()
            else:
                return self.convert("JPY")

#Start of conversion to Euro (EUR)

    def conv_to_eur(self):
        if self.currency == "EUR":
            return Money(self.amount, self.currency)
        else:
            if self.currency != "USD":
                temp = self.conv_to_usd()
                return temp.conv_to_eur()
            else:
                return self.convert("EUR")

#Start of conversion to Bitcoin (XBT)

    def conv_to_xbt(self):
        if self.currency == "XBT":
            return Money(self.amount, self.currency)
        else:
            if self.currency != "USD":
                temp = self.conv_to_usd()
                return temp.conv_to_xbt()
            else:
                return self.convert("XBT")

#Start of coversion to US Dollars (USD)

    def conv_to_usd(self):
        if self.currency != "USD":
            return self.convert("USD")
        else:
            return Money(self.amount, self.currency)

#Begin operator overloads

    def __ge__(self, other):
        return self.conv_to_usd().amount >= other.conv_to_usd().amount

    def __gt__(self, other):
        return self.conv_to_usd().amount > other.conv_to_usd().amount

    def __le__(self, other):
        return self.conv_to_usd().amount <= other.conv_to_usd().amount

    def __lt__(self, other):
        return self.conv_to_usd().amount < other.conv_to_usd().amount

    def __eq__(self, other):
        return self.conv_to_usd().amount == other.conv_to_usd().amount

    def __ne__(self, other):
        return self.conv_to_usd().amount != other.conv_to_usd().amount

    def __add__(self, other):
        return Money(self.conv_to_usd().amount + other.conv_to_usd().amount, "USD")

    def __sub__(self, other):
        return Money(self.conv_to_usd().amount - other.conv_to_usd().amount, "USD")

    def __mul__(self, other):
        return Money(self.conv_to_usd().amount * other.conv_to_usd().amount, "USD")

    def __div__(self, other):
        return Money((self.conv_to_usd().amount) / (other.conv_to_usd().amount), "USD")

#Start of main

x = Money(50, "USD")
y = Money(60, "EUR")

print(x)
print(y)
print(x / y)

"""
print(x.conv_to_xbt())
print(x.conv_to_eur())
print(x.conv_to_jpy())
"""
#print(x.conv_to_jpy().conv_to_usd())
