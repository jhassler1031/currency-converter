
#Currency converter
#Actors: Money
#Money - needs to accept an amount and initial currency type (USD)
#       then needs to have methods available to run to return the amount
#       converted into another currency

class Money:

#Start of __init__ method
    def __init__(self, amount, currency):
        self.amount = amount
        self.current = currency

        
