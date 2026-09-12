    # ==============================
    # PART 2 : ROOM OBSERVATION
    # ==============================


    # -------------------------
    # DISPLAY CURRENT ROOM
    # ---------------------
    



    # -------------------------
# DISPLAY CURRENT ROOM
# -------------------------

def look(self):

    room = self.rooms[self.current_room]

    print("\n================================")
    print("Current Room :", self.current_room)
    print("Description :", room["description"])

    print("\nObjects Available:")

    if room["objects"]:
        for obj in room["objects"]:
            print("-", obj)
    else:
        print("No objects available.")

    print("\nAvailable Directions:")

    for direction, destination in room["exits"].items():
        print(f"{direction} -> {destination}")

    print("================================")


# -------------------------
# MOVE AGENT
# -------------------------

def move(self, direction):

    direction = direction.lower()

    room = self.rooms[self.current_room]

    if direction not in room["exits"]:
        print("\nCannot move in that direction.")
        return

    next_room = room["exits"][direction]

    # Laboratory lock
    if next_room == "Laboratory" and not self.lab_unlocked:
        print("\nLaboratory is locked.")
        print("Find the Golden Key first.")
        return

    self.current_room = next_room

    if self.current_room not in self.visited_rooms:
        self.visited_rooms.append(self.current_room)

    print("\n================================")
    print("AI moved", direction.upper())
    print("Current Room:", self.current_room)
    print("================================")

    self.look()