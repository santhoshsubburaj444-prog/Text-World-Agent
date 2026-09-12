# =====================================
# PART 8 : MAIN PROGRAM
# =====================================


# ==============================
# MAIN PROGRAM
# ==============================

# ==============================
# MAIN PROGRAM
# ==============================

def main():
    try:
        # Create AI Agent
        agent = Agent()

        # Initialize World Model
        agent.create_world_model()

        # Observe starting room
        agent.observe_environment()

        # Start the game
        command_interface(agent)

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()