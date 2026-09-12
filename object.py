    # ==============================
    # PART 3 : OBJECT MANAGEMENT
    # ==============================


    # -------------------------
    # TAKE OBJECT
    # -------------------------
 # -------------------------
# TAKE OBJECT
# -------------------------

def take(self, item):

    room = self.rooms[self.current_room]

    # Already collected?
    if item.lower() in self.object_memory:

        data = self.object_memory[item.lower()]

        print("\n================================")
        print(f"{item} has already been collected.")
        print(f"Collected from : {data['room']}")
        print(f"Status : {data['status']}")
        print("================================")
        return

    # Search in current room
    for obj in room["objects"]:

        if obj.lower() == item.lower():

            self.inventory.append(obj)
            room["objects"].remove(obj)

            self.object_count += 1

            self.object_memory[obj.lower()] = {
                "room": self.current_room,
                "status": "Collected"
            }

            print("\n================================")
            print(f"{obj} collected successfully.")
            print(f"Location : {self.current_room}")
            print(f"Objects Collected : {self.object_count}/{self.max_objects}")
            print("================================")

            if obj == "Golden Key":
                self.lab_unlocked = True
                print("\nLaboratory has been unlocked!")

            if obj == "Ancient Crystal":
                print("\nMission Object Collected!")
                print("Go to Exit Gate to complete the mission.")

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

            if obj.lower() in self.object_memory:
                self.object_memory[obj.lower()]["status"] = "Dropped"

            print(f"\n{obj} dropped in {self.current_room}")
            return

    print("\nYou don't have that object.")


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

    print("===============================")


# -------------------------
# FIND OBJECT
# -------------------------

def find_object(self, item):

    # Already remembered?
    if item.lower() in self.object_memory:

        info = self.object_memory[item.lower()]

        print("\n================================")
        print(f"Object : {item}")
        print(f"Collected From : {info['room']}")
        print(f"Status : {info['status']}")
        print("================================")
        return

    # Search all rooms
    for room_name, room in self.rooms.items():

        for obj in room["objects"]:

            if obj.lower() == item.lower():

                print("\n================================")
                print(f"Object : {obj}")
                print(f"Located In : {room_name}")
                print("Status : Available")
                print("================================")
                return

    print("\nObject does not exist.")