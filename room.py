class Room():

    name = ""
    description = None
    linked_rooms = {}
    character = None
    item = None

    def __init__(self, room_name):
        self.name = room_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_description(self, new_description):
        self.description = new_description

    def get_description(self):
        return self.description

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # comment later
        print( self.name + " linked rooms: " + repr(self.linked_rooms))
    
    # r = Room("a")
    # r.get_character()
    # r.character

    
