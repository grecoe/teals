"""
    Ok, so we've covered a lot...hope you're still
    with me on classes.

    In this section we'll talk about 'over riding' a
    parent class. We'll use most of what we've already
    learned, but lets get away from dog!

    Lets use cars :)

    Honda Accord 0-100 (62 mph) km/h in about ~8.1 seconds
    BMW x5 xDrive35i 0-100 (62 mph) km/h in about ~5.9 seconds
    Honda Formula 1 0-100 km/h in ~2.5 seconds
        F1 Fun Facts:
        - Every F1 car on the grid is capable of going from 0 to
          160 km/h (0 to 99 mph) and back to 0 in less than five seconds.
        - Acceleration from 100-200km/h is < 2 seconds because it's
          not fighting for traction...physics is hard!
        - F1 cars can go from 0-300km/h (186m/h) in <10 seconds


    Cool Videos:
    https://www.youtube.com/watch?v=5XK3QjzN560
    https://www.youtube.com/watch?v=2qWamZTy56I
"""
import time


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def accelerate_to_100(self, seconds):
        time.sleep(seconds)
        print("{} {} is done!".format(self.brand, self.model))

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class Honda(Car):
    def __init__(self, model):
        super().__init__("Honda", model)

    def go(self):
        """ Standard acceleration for Honda"""
        print("HONDA ACCELLERATING")
        self.accelerate_to_100(8.1)


class RedbullF1(Honda):
    def __init__(self):
        super().__init__("RB13")

    def go(self):
        """ Overrides Honda.go() """
        print("RB13 ACCELLERATING")
        self.accelerate_to_100(2.5)


class BMW(Car):
    def __init__(self, model):
        super().__init__("BMW", model)

    def go(self):
        """Standard acceleration for BMW"""
        print("BMW ACCELLERATING")
        self.accelerate_to_100(5.9)


"""
    Now lets create two cars (Accord and F1) and put them in a list
"""
cars = [Honda("Acura"), BMW("X5"), RedbullF1()]

"""
    Lets look again at isinstance to see the inhertiance
"""
for car in cars:
    print("Car:", car.brand, car.model)
    print("Is Car:", isinstance(car, Car))
    print("Is Honda:", isinstance(car, Honda))
    print("Is F1:", isinstance(car, RedbullF1))
    print("")

"""
    This is more than we are going to cover, but lets run them
    at the same time!
"""
input("Now lets race! Press Enter")
for car in cars:
    print("0-100KPG test for - ", car)
    start = time.perf_counter()
    car.go()
    print("Done in {} seconds\n".format(time.perf_counter() - start))
