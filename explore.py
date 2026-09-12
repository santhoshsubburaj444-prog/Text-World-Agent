    # ==============================
    # PART 4 : AI EXPLORATION
    # ==============================


    # -------------------------
    # START AI EXPLORATION
    # -------------------------

    # ==============================
# AI AUTOMATIC EXPLORATION
# ==============================

def start_ai_exploration(self):

    print("\n===================================")
    print("       AI AGENT STARTED")
    print("===================================")

    # Start DFS exploration
    self.explore_room(self.current_room)

    print("\n===================================")
    print("     EXPLORATION COMPLETED")
    print("===================================")

    print("\nRooms Visited:", len(self.visited_rooms))
    for room in self.visited_rooms:
        print("-", room)

    print("\nObjects Collected:", len(self.inventory))
    for obj in self.inventory:
        print("-", obj)

    print("\nMission Status:")
    self.check_mission()


# ==============================
# DFS EXPLORATION
# ==============================

def explore_room(self, room_name):

    # Stop after required rooms and objects
    if len(self.visited_rooms) >= self.max_rooms and self.object_count >= self.max_objects:
        return

    # Move agent
    self.current_room = room_name

    # Store visited room
    if room_name not in self.visited_rooms:
        self.visited_rooms.append(room_name)

    print("\n-----------------------------------")
    print("AI Entered :", room_name)
    print("-----------------------------------")

    # Observe room
    self.look()

    # Update world model if available
    if hasattr(self, "observe_environment"):
        self.observe_environment()

    # Collect all objects
    room = self.rooms[self.current_room]

    while room["objects"] and self.object_count < self.max_objects:
        item = room["objects"][0]
        self.take(item)

    # Explore neighbouring rooms
    for direction, next_room in room["exits"].items():

        # Skip visited rooms
        if next_room in self.visited_rooms:
            continue

        # Skip locked laboratory
        if next_room == "Laboratory" and not self.lab_unlocked:
            continue

        print(f"\nAI Moving {direction.upper()} -> {next_room}")

        self.explore_room(next_room)

        # Stop if objective reached
        if len(self.visited_rooms) >= self.max_rooms and self.object_count >= self.max_objects:
            return