General system overview

Arduino:
- Used purely for hardware interfacing
- Reads reed switches
- Communicates switch states as 64 bit bitmap strings to the raspberry pi
- Recieves UI commands from the pi
- Only sends bitmap when it changes
- Has a "store" of lighting functions that the ui can call upon



Raspberry Pi:
- Brains of the operation
- Interprets the bitmaps sent from the arduino
- Uses changes in the bitmaps to determine the changes to the physical board and thus the intention of the users


Pi Code:
Agent:
- Concerned only with the interpretation of the bitmaps it recieves
- As far as the game logic is concerned, the agent is a player
- Essentially deciefers the moves made by the player in the real world
- Can be configured as either AI or as a human player with possibility to extend to other agent types
- AI player generates moves based on the current board state, then by reading the bitmaps, ensures the correct moves have been undergone in the real world to make the move happen
- Human player interprets moves in the real world to figure out the move intended by the human player
- Agents are not concerned with what colour they are, only that it is their turn, and that they have seen behaviour indicitive of a move

Player:
- The player acts as the interface between an agent and the rest of the game
- It holds metadata important to understanding the moves detected by the agents
- This allows the generation of moves by the agents in what ever way they do it, either by ai or human bitmap interpretation, to be abstracted from the move of a player
- This means to the rest of the system, a player simply provides moves when it is its turn, and the rest of the system doesnt know if its ai or human or what

Game:
- Concerned with the current state of the chess board, moves proposed by players and the legality of those moves
- Recieves moves from a player, but doesnt care how they were generated (AI or Human), as far as it is concerned a player is just a move generator
- Doesnt care about the physical board or bitmaps, only chess moves

Engine:
- A single chess ai which can be accessed by any agent to suggest moves
- Reconfigurable to different difficuly levels
- Used by AI agent to generate moves as an opponent, difficulty level selected by the human player at the beginning of the game
- Used by Human agent to suggest moves as a hint at the users request, difficulty level at its highest to suggest the best move
- Only accessed by agents, not concerned with any other module


UI:
- Observes players and the game to determine which lights need to light up on the board
- Sends instructions via serial to the pi to light up squares
- Decifers metadata from players to determine how to act in that moment

Bitmap:
- Object which acts as the single source of bitmap truth
- Recieves bitmaps via serial
- Is read by the agents to extract move information






















  
