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