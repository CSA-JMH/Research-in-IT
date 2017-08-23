#Joshua Hinojoas
#8/25/16
#Mr. Davis
#Basic Python Review
def main():

    class Car:
        def __init__(self,color=input("What is the color for the car?"), year=input("What is the year for the car?"),topspeed=input("What is the topspeed for the car?")):
            self.color=color
            self.year=year
            self.topspeed=topspeed
    car=Car()
    print("You have a " + car.color + " car from " + car.year + " that can go " + car.topspeed + " miles per hour.")
main()