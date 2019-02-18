class pet:
    number_of_legs = 0

    def sleep(self):
        print("sleeping Dog")
    def count_legs(self):
        print("it has", self.number_of_legs, "legs")    


# dog = pet()
# dog.number_of_legs = 4
# # dog.sleep()
# dog.count_legs()

# spider = pet()
# spider.number_of_legs = 8
# spider.count_legs()
class dog(pet):
    def number_of_teeth(self):
        print("the dog has many teeth")
dog = dog()
dog.number_of_teeth()        