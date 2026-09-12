===========================================================
                TEXT WORLD AI AGENT
===========================================================

Project Name:
-------------
Text World AI Agent with World Model

Description:
------------
This project is a terminal-based Text World developed in Python.
The AI agent explores an environment consisting of interconnected
rooms, collects objects, builds an internal world model, and
completes a mission automatically or through user commands.

-----------------------------------------------------------
FEATURES
-----------------------------------------------------------

• 10 interconnected rooms
• AI agent exploration
• World Model memory
• Inventory management
• Object location tracking
• Automatic room navigation
• Mission completion
• Terminal command interface
• Object reminder if already collected
• Laboratory unlocking using Golden Key

-----------------------------------------------------------
ROOMS
-----------------------------------------------------------

1. Hall
2. Kitchen
3. Bathroom
4. Dining Room
5. Storage Room
6. Library
7. Study Room
8. Garden
9. Laboratory
10. Exit Gate

-----------------------------------------------------------
OBJECTS
-----------------------------------------------------------

Hall
- Map

Kitchen
- Knife
- Apple

Bathroom
- Soap
- Towel

Dining Room
- Plate
- Cup

Storage Room
- Torch
- Battery

Library
- Golden Key
- Old Book

Study Room
- Notebook
- Pen

Garden
- Flower
- Shovel

Laboratory
- Ancient Crystal

-----------------------------------------------------------
MISSION
-----------------------------------------------------------

Mission Steps:

1. Start from Hall.
2. Explore the environment.
3. Visit at least 7 rooms.
4. Collect at least 10 objects.
5. Find the Golden Key.
6. Unlock the Laboratory.
7. Enter the Laboratory.
8. Collect the Ancient Crystal.
9. Reach the Exit Gate.
10. Mission Completed.

-----------------------------------------------------------
WORLD MODEL
-----------------------------------------------------------

The AI remembers:

• Visited rooms
• Object locations
• Collected objects
• Available exits
• Inventory
• Mission progress

-----------------------------------------------------------
AVAILABLE COMMANDS
-----------------------------------------------------------

look
    Displays the current room.

go <direction>
    Moves the agent.

Example:
go north

take <object>

Example:
take golden key

drop <object>

Example:
drop apple

inventory

Displays collected objects.

find <object>

Example:
find torch

world

Displays the AI World Model.

status

Displays mission status.

explore

Starts automatic AI exploration.

help

Displays available commands.

quit

Exits the game.

-----------------------------------------------------------
REQUIREMENTS
-----------------------------------------------------------

Python 3.9 or above

No external libraries are required.

-----------------------------------------------------------
HOW TO RUN
-----------------------------------------------------------

Open Terminal or Command Prompt.

Navigate to the project folder.

Example:

cd Text.World

Run the program:

python agent.py

-----------------------------------------------------------
EXPECTED OUTPUT
-----------------------------------------------------------

TEXT WORLD AI

Current Room : Hall

Objects:
- Map

Commands:
look
go north
take map
inventory
explore
quit

-----------------------------------------------------------
PROJECT STRUCTURE
-----------------------------------------------------------

Text.World/

│── agent.py
│── README.txt

-----------------------------------------------------------
AUTHOR
-----------------------------------------------------------

Project:
Text World AI Agent

Language:
Python

Environment:
Terminal / Command Prompt

===========================================================
END OF FILE
===========================================================