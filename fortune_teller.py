import random

class FortuneTeller:
    def __init__(self, name, luck, fortune):
        self.name = name
        self.luck = luck
        self.fortune = fortune

    def tell_fortune(self, fortune):
        return self.fortune

    def get_name(self, name):
        return self.name()
    
    def get_luck(self, luck):
        return self.luck
    
    def __repr__(self):
        return f"Your name is {self.name} and your luck today is {self.luck}. \nYour fortune for the day is: {self.fortune}."

fortunes = ["You will make someone's day better", "Good fortune awaits you.", "You will soon find your soulmate.", "Love is in the air.", "Seize your next opportunity!", "Your hardwork will pay off.", "A stranger will cross your path who later becomes your friend.", "A chance happening will reveal your destiny", "Little by little, one travels far.", "What good are wings without the courage to fly?", "Don't let yesterday take up too much of today", "A great honor will be bestowed upon you in the upcoming year.", "True friendship multiplies the good in life and divides its evils.", "Turn your wounds into wisdom.", "Every exit is an entrance to new experiences."]
luck_types = ["terrible", "bad", "moderate", "good", "excellent"]

customer = FortuneTeller(input("What is your name? "), random.choice(luck_types), random.choice(fortunes))
print(customer)