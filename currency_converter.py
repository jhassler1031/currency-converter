
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


#Start of __str__ method
    def __str__(self):
        return str(self.amount) + " " + self.currency

#Start of conversion to Japanese Yen (JPY)

    def conv_to_jpy(self):

        rate = 111.2
        if self.currency != "JPY":
            return self.amount * rate
        else:
            return self.amount

#Start of conversion to Euro (EUR)

    def conv_to_eur(self):

        rate = 0.85
        if self.currency != "EUR":
            return self.amount * rate
        else:
            return self.amount

#Start of conversion to Bitcoin (XBT)

    def conv_to_xbt(self):

        rate = 0.00013
        if self.currency != "XBT":
            return str(self.amount * rate) + "XBT"
        else:
            return self.amount

#Start of coversion to US Dollars (USD)

    def conv_to_usd(self):

        pass



#Start of main

x = Money(50, "XBT")

print(x)

print(x.conv_to_xbt())
