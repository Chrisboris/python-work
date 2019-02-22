from docopt import docopt, DocoptExit
import cmd
import sys


usage = '''
   Office Space Allocation CLI Applicaiton

   Usage:
       Room.py (-i | --interactive)
       Room.py create_room <room_type> <room_name>...
       Room.py add_person <person_name> <position> [<wants_accommodation>]

   Options:
   -i, --interactive  Interactive Mode
   -h, --help  Show this screen and exit.

'''
class Dojo(object):
   def __init__(self):
       self.rooms = []
   def create_room(self, room_name, purpose):
       """ method create room to add new rooms to dojo"""

       if [room for room in self.rooms
          if room_name.upper() == room.room_name.upper()]:
           print("{} already Exists in Dojo.".format(room_name.upper()))
           return "{} already Exists in Dojo.".format(room_name.upper())

       if str(purpose.upper()) == "OFFICE":
           room = Office(str(room_name.upper()))
           self.offices.append(room)
           self.rooms.append(room)
           print("{} {} created".format(room.name, room.purpose))
           return "Room Created"

       if purpose.upper() == "LIVINGSPACE":
           room = LivingSpace(room_name.upper())
           self.living_spaces.append(room)
           self.rooms.append(room)
           print("{} {} created".format(room.name, room.purpose))
           return "Room Created"

       print("{} is not a valid room type.".format(purpose))
       return "{} is not a valid room type.".format(purpose)