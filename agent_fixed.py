# ==============================
# TEXT WORLD AI AGENT
# PART 1 : WORLD CREATION
# ==============================

class Agent:
    

    def __init__(self):

        # -------------------------
        # ENVIRONMENT (10 ROOMS)
        # -------------------------

        self.rooms = {

            "Hall": {
                "description": "The main entrance hall of the castle.",
                "objects": ["Map"],
                "exits": {
                    "north": "Kitchen",
                    "east": "Library",
                    "south": "Garden"
                }
            },


            "Kitchen": {
                "description": "A clean kitchen with cooking equipment.",
                "objects": ["Knife", "Apple"],
                "exits": {
                    "south": "Hall",
                    "north": "Bathroom",
                    "east": "Dining Room"
                }
            },


            "Bathroom": {
                "description": "A small bathroom with a mirror.",
                "objects": ["Soap", "Towel"],
                "exits": {
                    "south": "Kitchen"
                }
            },


            "Dining Room": {
                "description": "A large dining room with a wooden table.",
                "objects": ["Plate", "Cup"],
                "exits": {
                    "west": "Kitchen",
                    "north": "Storage Room"
                }
            },


            "Storage Room": {
                "description": "A dark storage room filled with old boxes.",
                "objects": ["Torch", "Battery"],
                "exits": {
                    "south": "Dining Room"
                }
            },


            "Library": {
                "description": "An ancient library containing many books.",
                "objects": ["Golden Key", "Old Book"],
                "exits": {
                    "west": "Hall",
                    "north": "Study Room"
                }
            },


            "Study Room": {
                "description": "A quiet room for reading and research.",
                "objects": ["Notebook", "Pen"],
                "exits": {
                    "south": "Library"
                }
            },


            "Garden": {
                "description": "A beautiful garden with trees and flowers.",
                "objects": ["Flower", "Shovel"],
                "exits": {
                    "north": "Hall",
                    "east": "Laboratory"
                }
            },


            "Laboratory": {
                "description": "A secret laboratory with advanced equipment.",
                "objects": ["Ancient Crystal"],
                "exits": {
                    "west": "Garden",
                    "east": "Exit Gate"
                }
            },


            "Exit Gate": {
                "description": "The final exit gate of the castle.",
                "objects": [],
                "exits": {
                    "west": "Laboratory"
                }
            }

        }


        # -------------------------
        # AGENT MEMORY
        # -------------------------

        # Starting location
        self.current_room = "Hall"


        # Collected objects
        self.inventory = []


        # Visited rooms memory
        self.visited_rooms = []


        # Object location memory
        self.object_memory = {}


        # Mission status
        self.lab_unlocked = False
        self.mission_completed = False


        # Counters
        self.object_count = 0
        self.max_objects = 10

        self.max_rooms = 7
            # ==============================
    # PART 2 : ROOM OBSERVATION
    # ==============================


    # -------------------------
    # DISPLAY CURRENT ROOM
    # -------------------------

    def look(self):

        room = self.rooms[self.current_room]

        print("\n================================")
        print("Current Room :", self.current_room)
        print(room["description"])

        print("\nObjects Available:")

        if room["objects"]:

            for obj in room["objects"]:
                print("-", obj)

        else:

            print("No objects available.")


        print("\nAvailable Directions:")

        for direction, destination in room["exits"].items():

            print(direction, "->", destination)


        print("================================")


    # -------------------------
    # MOVE AGENT
    # -------------------------

    def move(self, direction):

        current = self.rooms[self.current_room]


        # Check direction exists

        if direction not in current["exits"]:

            print("\nCannot move in that direction.")

            return



        next_room = current["exits"][direction]


        # Laboratory lock check

        if next_room == "Laboratory" and self.lab_unlocked == False:

            print("\nLaboratory is locked.")

            print("Find the Golden Key first.")

            return



        # Update current location

        self.current_room = next_room



        # Store visited room

        if next_room not in self.visited_rooms:

            self.visited_rooms.append(next_room)



        print("\nAI moved", direction)

        print("Reached:", next_room)



        # Display new room

        self.look()

        # Automatically check mission when Exit Gate is reached
        if self.current_room == "Exit Gate":
            self.check_mission()
            # ==============================
    # PART 3 : OBJECT MANAGEMENT
    # ==============================


    # -------------------------
    # TAKE OBJECT
    # -------------------------

    def take(self, item):

        room = self.rooms[self.current_room]


        # Check if object was already collected

        if item.lower() in self.object_memory:

            data = self.object_memory[item.lower()]

            print("\n================================")
            print(item, "was already taken.")
            print("Taken from :", data["room"])
            print("Status :", data["status"])
            print("================================")

            return



        # Search object in current room

        for obj in room["objects"]:


            if obj.lower() == item.lower():


                # Add to inventory

                self.inventory.append(obj)


                # Remove from room

                room["objects"].remove(obj)


                # Increase count

                self.object_count += 1



                # Store object memory

                self.object_memory[obj.lower()] = {

                    "room": self.current_room,

                    "status": "Collected"

                }



                print("\n================================")
                print(obj, "collected successfully.")
                print("Location :", self.current_room)
                print("Objects Collected:",
                      self.object_count,
                      "/",
                      self.max_objects)
                print("================================")



                # Golden Key unlocks laboratory

                if obj == "Golden Key":

                    self.lab_unlocked = True

                    print("\nGolden Key found!")

                    print("Laboratory has been unlocked.")



                # Ancient Crystal mission item

                if obj == "Ancient Crystal":

                    print("\nAncient Crystal obtained.")

                    print("Reach Exit Gate to complete mission.")


                return



        print("\nObject not found in this room.")



    # -------------------------
    # DROP OBJECT
    # -------------------------

    def drop(self, item):


        for obj in self.inventory:


            if obj.lower() == item.lower():


                self.inventory.remove(obj)


                self.rooms[self.current_room]["objects"].append(obj)



                self.object_memory[obj.lower()]["status"] = "Dropped"



                print("\nDropped:", obj)

                print("Location:", self.current_room)


                return



        print("\nYou don't have this object.")



    # -------------------------
    # SHOW INVENTORY
    # -------------------------

    def show_inventory(self):


        print("\n========== INVENTORY ==========")


        if self.inventory:


            for obj in self.inventory:

                print("-", obj)


        else:

            print("Inventory is empty.")


        print("==============================")



    # -------------------------
    # FIND OBJECT LOCATION
    # -------------------------

    def find_object(self, item):


        # Check memory first

        if item.lower() in self.object_memory:


            data = self.object_memory[item.lower()]


            print("\n================================")
            print("Object :", item)
            print("Found at :", data["room"])
            print("Status :", data["status"])
            print("================================")


            return



        # Search environment

        for room_name, room in self.rooms.items():


            for obj in room["objects"]:


                if obj.lower() == item.lower():


                    print("\n================================")
                    print("Object :", obj)
                    print("Located at :", room_name)
                    print("Status : Not Collected")
                    print("================================")


                    return



        print("\nObject does not exist.")
            # ==============================
    # PART 4 : AI EXPLORATION
    # ==============================


    # -------------------------
    # START AI EXPLORATION
    # -------------------------

    def start_ai_exploration(self):

        print("\n================================")
        print("       AI AGENT STARTED")
        print("================================")


        # Start exploring from Hall

        self.explore_room(self.current_room)



        print("\n================================")
        print("       EXPLORATION COMPLETE")
        print("================================")



        print("\nRooms Visited:")

        for room in self.visited_rooms:

            print("-", room)



        print("\nObjects Collected:")

        for obj in self.inventory:

            print("-", obj)



        print("\nTotal Rooms:",
              len(self.visited_rooms))


        print("Total Objects:",
              len(self.inventory))



    # -------------------------
    # DFS ROOM EXPLORATION
    # -------------------------

    def explore_room(self, room_name):


        # Stop condition

        if (len(self.visited_rooms) >= self.max_rooms
                and self.object_count >= self.max_objects):

            return



        # Move agent to room

        self.current_room = room_name



        # Add room to memory

        if room_name not in self.visited_rooms:

            self.visited_rooms.append(room_name)



        print("\n--------------------------------")

        print("AI entered:", room_name)



        self.look()



        # Collect objects in room

        room = self.rooms[room_name]


        while room["objects"]:


            if self.object_count >= self.max_objects:

                break


            item = room["objects"][0]


            self.take(item)



        # Explore connected rooms

        for direction, next_room in room["exits"].items():


            if next_room not in self.visited_rooms:


                print("\nAI moving:",
                      direction,
                      "->",
                      next_room)



                self.explore_room(next_room)



                # Return back after exploration

                if len(self.visited_rooms) >= self.max_rooms:

                    return
                    # ==============================
    # PART 5 : MISSION SYSTEM
    # ==============================


    # -------------------------
    # CHECK MISSION STATUS
    # -------------------------

    def check_mission(self):


        # Mission was already completed
        if self.mission_completed:
            return True

        print("\n========== MISSION STATUS ==========")


        # Check Ancient Crystal

        if "Ancient Crystal" not in self.inventory:


            print("❌ Ancient Crystal not collected.")

            print("Find the Laboratory and collect it.")


            return False



        # Check Exit Gate

        if self.current_room != "Exit Gate":


            print("✅ Ancient Crystal collected.")

            print("❌ Reach Exit Gate to finish the mission.")


            return False



        # Mission completed

        self.mission_completed = True


        print("\n====================================")
        print("       🎉 MISSION COMPLETED 🎉")
        print("====================================")

        print("Agent collected Ancient Crystal.")

        print("Agent reached Exit Gate.")

        print("The environment task is completed.")


        return True



    # -------------------------
    # MOVE TO GOAL CHECK
    # -------------------------

    def reach_exit(self):


        if self.current_room == "Exit Gate":


            self.check_mission()


        else:


            print("\nAgent is not at Exit Gate.")

            print("Current Location:",
                  self.current_room)
                # ==============================
    # PART 6 : WORLD MODEL SYSTEM
    # ==============================


    # -------------------------
    # INITIALIZE WORLD MODEL
    # -------------------------

    def create_world_model(self):

        self.world_model = {

            "rooms": {},

            "objects": {}

        }


        print("\nWorld model created.")



    # -------------------------
    # UPDATE ROOM MEMORY
    # -------------------------

    def update_room_memory(self):


        room = self.rooms[self.current_room]


        # Store room information

        self.world_model["rooms"][self.current_room] = {


            "description": room["description"],


            "exits": room["exits"],


            "visited": True

        }



        # Store object information

        for obj in room["objects"]:


            self.world_model["objects"][obj] = {


                "location": self.current_room,


                "status": "Available"

            }



    # -------------------------
    # UPDATE OBJECT MEMORY
    # -------------------------

    def update_object_memory(self):


        for obj, data in self.object_memory.items():


            self.world_model["objects"][obj] = {


                "location": data["room"],


                "status": data["status"]

            }



    # -------------------------
    # DISPLAY WORLD MODEL
    # -------------------------

    def show_world_model(self):


        print("\n================================")
        print("        AI WORLD MODEL")
        print("================================")


        print("\nKnown Rooms:")


        if self.world_model["rooms"]:


            for room in self.world_model["rooms"]:


                print("-", room)


        else:

            print("No rooms discovered.")



        print("\nKnown Objects:")


        if self.world_model["objects"]:


            for obj, data in self.world_model["objects"].items():


                print(
                    "-",
                    obj,
                    "| Location:",
                    data["location"],
                    "| Status:",
                    data["status"]
                )


        else:

            print("No objects discovered.")



        print("================================")



    # -------------------------
    # AGENT OBSERVATION UPDATE
    # -------------------------

    def observe_environment(self):


        # Update room knowledge

        self.update_room_memory()


        # Update object knowledge

        self.update_object_memory()


        print("\nAI updated world knowledge.")
        # =====================================
# PART 7 : TERMINAL COMMAND INTERFACE
# =====================================


def command_interface(agent):


    print("\n================================")
    print("        TEXT WORLD AI")
    print("================================")


    print("""
Available Commands:

look
go <direction>
take <object>
drop <object>
inventory
find <object>
world
status
explore
help
quit

Example:
go north
take golden key
find ancient crystal
""")


    agent.look()



    while True:


        command = input("\n> ").lower().split()



        if not command:

            continue



        # -------------------------
        # QUIT GAME
        # -------------------------

        if command[0] == "quit":


            print("\nAI session ended.")

            break



        # -------------------------
        # HELP
        # -------------------------

        elif command[0] == "help":


            print("""
Commands:

look
go north/south/east/west
take object_name
drop object_name
inventory
find object_name
world
status
explore
quit
""")



        # -------------------------
        # LOOK
        # -------------------------

        elif command[0] == "look":


            agent.look()



        # -------------------------
        # MOVE
        # -------------------------

        elif command[0] == "go":


            if len(command) > 1:


                agent.move(command[1])


            else:


                print("Give direction.")




        # -------------------------
        # TAKE OBJECT
        # -------------------------

        elif command[0] == "take":


            if len(command) > 1:


                item = " ".join(command[1:])


                agent.take(item)


            else:


                print("Give object name.")




        # -------------------------
        # DROP OBJECT
        # -------------------------

        elif command[0] == "drop":


            if len(command) > 1:


                item = " ".join(command[1:])


                agent.drop(item)


            else:


                print("Give object name.")




        # -------------------------
        # INVENTORY
        # -------------------------

        elif command[0] == "inventory":


            agent.show_inventory()




        # -------------------------
        # FIND OBJECT
        # -------------------------

        elif command[0] == "find":


            if len(command) > 1:


                item = " ".join(command[1:])


                agent.find_object(item)


            else:


                print("Give object name.")




        # -------------------------
        # SHOW WORLD MODEL
        # -------------------------

        elif command[0] == "world":


            agent.show_world_model()




        # -------------------------
        # MISSION STATUS
        # -------------------------

        elif command[0] == "status":


            agent.check_mission()




        # -------------------------
        # AI AUTO EXPLORE
        # -------------------------

        elif command[0] == "explore":


            agent.start_ai_exploration()



        else:


            print("Unknown command.")
            # =====================================
# PART 8 : MAIN PROGRAM
# =====================================


if __name__ == "__main__":


    # Create AI Agent

    agent = Agent()



    # Initialize World Model

    agent.create_world_model()



    # Initial observation

    agent.observe_environment()



    # Start terminal interface

    command_interface(agent)