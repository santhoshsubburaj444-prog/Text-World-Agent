# ==============================
# PART 5 : MISSION SYSTEM
# ==============================

# -------------------------
# CHECK MISSION STATUS
# -------------------------

def check_mission(self):

    print("\n========== MISSION STATUS ==========")

    # Check if Ancient Crystal is collected
    if "Ancient Crystal" not in self.inventory:
        print("Mission Incomplete!")
        print("Ancient Crystal has not been collected.")
        return False

    # Check if player reached Exit Gate
    if self.current_room != "Exit Gate":
        print("Ancient Crystal collected.")
        print("Go to the Exit Gate to complete the mission.")
        return False

    # Mission Complete
    self.mission_completed = True

    print("\n===================================")
    print("       MISSION COMPLETED!")
    print("===================================")
    print("Objective Achieved!")
    print("✓ Ancient Crystal Collected")
    print("✓ Exit Gate Reached")
    print("Congratulations!")
    print("===================================")

    return True


# -------------------------
# MOVE TO EXIT
# -------------------------

def reach_exit(self):

    if self.current_room == "Exit Gate":
        return self.check_mission()

    print("\nYou are not at the Exit Gate.")
    print("Current Room:", self.current_room)
    return False