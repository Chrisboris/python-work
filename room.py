class Room:
    room_count = 0


    def __init__(self,name=None,occupants=None,capacity=None,purpose=None):
       self.name = room_name
       self.id = room_count
       room_count =+ 1
       self.capacity = room_capacity
       self.purpose = room_purpose
       self.occupants = []

    def add_occupants(self,occupant):
        if self.occupants is full ():
            return False
        self.occupants.append(occupant)
        return True

    def remove_occupant(self,occupant):
        if self.occupants is an_occupant(occupant):
            self.occupants.remove(occupant)
            return True
        return False

    def is_full(self):
        if len(self.occupants) >= room_capacity:
            return "room full"  


    def __repr__(self):
        return '%s(name=%s, purpose=%s, max_capacity=%s)' % (
            self.__class__.__name__, 
            self.name,
            self.purpose,
            self.room_capacity
        )
    def __str__(self):
        return Self.name        


class officespace(Room):
    def __init__(self,name=None,room_capacity = 6):
        self.purpose = "OFFICE"
        room_capacity = 6

class Livingspace(Room):
    def __init__(self,name=None,room_capacity = 4):
        self.purpose = "LIVINGSPACE"
        room_capacity = 4

class Person:
    def __init__(self,my_name=None,my_id=None,my_role=None):
       self.name = my_name
       self.id = my_id
       self.role = my_role
       self.room = []

    def occupy_room(self, Room):
       self.room.append

    def remove_from_room(self, Room):
       self.occupant.remove(Room)
    
    def __repr__(self):
        return '%s(name=%s, want_accomodation=%s)' % (
            self.__class__.__name__, 
            self.name,
            self.want_accomodation
        )
    def __str__(self):
        return Self.name   

    
class Fellow(Person):
    def __init__(self,my_name=None,wants_accomodation=None,my_id=None):
        self.accomodation = wants_accomodation
        self.role = "Fellow"
        self.has_accomodation = False
        self.has_an_office = False

    def give_accomodation(self):
           if self.accomodation is True:
               print("Room created")

class Staff(Person):
    def __init__(self,role,my_name=None,my_id=None,wants_accomodation=None):
        self.role = "Staff"
        self.has_an_office = False
        

      