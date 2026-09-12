    # ==============================
    # PART 6 : WORLD MODEL SYSTEM
    # ==============================


    # -------------------------
    # INITIALIZE WORLD MODEL
    # -------------------------
# -------------------------
# CREATE WORLD MODEL
# -------------------------

def create_world_model(self):

    self.world_model = {
        "rooms": {},
        "objects": {}
    }

    print("\nWorld Model Created Successfully.")


# -------------------------
# UPDATE ROOM MEMORY
# -------------------------

def update_room_memory(self):

    room = self.rooms[self.current_room]

    self.world_model["rooms"][self.current_room] = {
        "description": room["description"],
        "exits": room["exits"].copy(),
        "visited": True
    }

    for obj in room["objects"]:

        self.world_model["objects"][obj.lower()] = {
            "name": obj,
            "location": self.current_room,
            "status": "Available"
        }


# -------------------------
# UPDATE OBJECT MEMORY
# -------------------------

def update_object_memory(self):

    for obj, info in self.object_memory.items():

        self.world_model["objects"][obj] = {
            "name": obj.title(),
            "location": info["room"],
            "status": info["status"]
        }


# -------------------------
# SHOW WORLD MODEL
# -------------------------

def show_world_model(self):

    print("\n========== AI WORLD MODEL ==========")

    print("\nKnown Rooms:")

    if len(self.world_model["rooms"]) == 0:
        print("None")

    else:
        for room, details in self.world_model["rooms"].items():

            print(f"\nRoom : {room}")
            print("Description :", details["description"])
            print("Visited :", details["visited"])
            print("Exits :", ", ".join(details["exits"].keys()))

    print("\nKnown Objects:")

    if len(self.world_model["objects"]) == 0:
        print("None")

    else:
        for obj, details in self.world_model["objects"].items():

            print(f"{details['name']} -> {details['location']} ({details['status']})")

    print("===================================")


# -------------------------
# OBSERVE ENVIRONMENT
# -------------------------

def observe_environment(self):

    self.update_room_memory()
    self.update_object_memory()

    print(f"\nAI observed {self.current_room}")