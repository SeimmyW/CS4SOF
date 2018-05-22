from room import Room
from character import Enemy, Character, Friend
#    file        class

kitchen = Room("Kitchen")
kitchen.set_description("A desk and dirty room buzzing with files.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny floor. Huge candlesticks guard the entrance.")

bathroom = Room("Bathroom")
bathroom.set_description("A sizeable room with golden sinks and very rich soaps")

basement = Room("Basement")
basement.set_description("A musty underground spot")

bedroom = Room("Bedroom")
bedroom.set_description("A luxurious room with a king sized bed and very fine paintings")

kitchen.link_room(dining_hall, "south")
kitchen.link_room(bathroom, "west")

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(bedroom, "south")
dining_hall.link_room(ballroom, "west")

bedroom.link_room(dining_hall, "north")
bedroom.link_room(basement, "west")

bathroom.link_room(ballroom, "south")
bathroom.link_room(kitchen, "east")

ballroom.link_room(bathroom, "north")
ballroom.link_room(basement, "south")
ballroom.link_room(dining_hall, "east")

basement.link_room(ballroom, "north")
basement.link_room(bedroom, "east")


dave = Enemy("Dave", "A smelly zombie")

# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude!")

dave.set_weakness("cheese")

dining_hall.set_character(dave)

# Add a new character

catrina = Friend("Catrina", "A friendly skeleton")

catrina.set_conversation("Why hello there.")

ballroom.set_character(catrina)

#Adding a new character

beast = Enemy("Beast", "A very violent being")

beast.set_conversation("I am the eternal ruler of the basement. You cannot hope to beat me without a sword!")

beast.set_weakness("sword")

basement.set_character(beast)

#Adding a new character

chef = Friend("Chef", "I hope he's making something good!")

chef.set_conversation("Do you want something to eat?")

kitchen.set_character(chef)

current_room = kitchen          

dead = False

while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  command = input("> ")
  
  if command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "fight":
    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is a Friend"
    if inhabitant == None or isinstance(inhabitant, Friend):
      print("There is no one here to fight with")
    else:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      if inhabitant.fight(fight_with) == True:
        # What happens if you win?
        print("Hooray, you won the fight!")
        current_room.set_character(None)
      else:
        # What happens if you lose?
        print("Oh dear, you lost the fight.")
        print("That's the end of the game")
        dead = True
  elif command == "hug":
    if inhabitant == None:
      print("There is no one here to hug :(")
    else:
      if isinstance(inhabitant, Enemy):
        print("I wouldn't do that if I were you...")
      else:
        inhabitant.hug()
#while True:		
    #print("\n")         
    #current_room.get_details()         
    #command = input("> ")    
    #current_room = current_room.move(command)  
