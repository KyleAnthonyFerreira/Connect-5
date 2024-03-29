# Connect-5

Our take on the classic Connect-5 game!

## Navigation
<a name="top"></a> 
1. [Game Description](#intro) 
2. [How to Play](#feature)
    - [Screenshots](#screen)
3. [How to Install Connect-5](#install)
4. [Documentation](#documen)
5. [Authors](#Authors)
6. [Individual Contributions](#Contributions)
7. [License Information](#license)

## <a name="intro"></a>Game Description 

Connect 5 is a simple yet challenging strategical game that will put one’s critical thinking and analytical skills to the test.

The game has a main menu, settings menu, and a playing board. The main menu will be the first thing shown to the user. The main menu acts as a hub to all the other modes this game has. From the menu, the player can choose to enter the settings menu, play a game, or close the application.

If the player launches a game, a new Connect 5 game will begin. It should be noted that the type of opponent you will face is predetermined before the game launches. The default opponent is another Local Human Player. This can be changed by clicking on the opponent to cycle through the possible options. This current build contains a Human Opponent as well as an Easy, Medium, and Hard AI.

To win this game, a player must get 5 of their pieces in a line in any possible direction. You (the player) can make a move with a mouse. A left-click on an empty tile on the board will place your piece there, assuming it is your turn to move. If the opponent is another player, then this player can also make moves with a mouse. However, if the opponent is the computer, the computer will generate a move based on its difficulty setting which is predetermined by the user before the game begins.

While in a game, the game can be reset via the RESTART button. This action will reset the game. Your opponent, piece color, and board color will remain the same. Pressing the MENU button will exit the game and will return you to the main menu. If you don’t want to lose your progress, you can save the current game by pressing the SAVE button on the right-hand side of the screen. This action will save the game for further use. This action also overrides all previous saves, so be careful when using it. The saved game can be loaded by pressing the LOAD button located under the SAVE button.

The settings menu can be assessed from the main menu. While in the settings menu, the user can modify the color of the board and the color of every player's pieces. This can be reset via the USE DEFAULT SETTINGS button located within the settings menu.

This application is designed to mimic the experience of playing Connect 5 over a real board. As such we have employed a variety of settings and features to make the most enjoyable playing experience. This application build has different computer opponents to simulate playing people at different strengths, a customization option to allow for a more personalized experience, and a saving feature to allow for users to return back to a game in progress.

[Back to top](#top)

## <a name="feature"></a>How to Play

Connect 5 is a strategic turn based game played between two players. The main objective of this game is to create a linear line of five of your own pieces before the other player does. This line can be either horizontal, vertical, or diagonal.

In this game, the "playing board" is laid down flat, and so, game play pieces can be positioned anywhere on the board as long as it is placed within the dimensions of the board, and if that posistion is unoccupied.

When you first "start up" the game, you will see the main menu which will consist of the following options: Play Game, Player vs Player, Settings, and Exit Game.

Before you begin playing, you can choose one of four different modes to play with, Player vs Player, Player vs AI(Easy), Player vs AI(Medium), and Player vs AI(Hard). You can select a mode by clicking on the second row of cyan-coloured text until you the screen is revealing your desired mode.

Before you start the game, you can select what colour your own pieces will be in the settings menu. In addition to this, you can change the colour of your opponenet's (player2's) pieces as well, plus the colour of the playing board. We do not suggest that you make none of these three elements have the same colour because that can make playing the game confusing. Once you are done selecting the colours, you can leave the settings menu by clicking the "Back to menu option" located at the top left of the screen.

Once you are ready to begin playing the game, click on "Start Game".

At your given turn, you can "click" on a coordinate where you want to place your game piece. Once you place your piece down, it is the other player's turn to put down a piece. This pattern will continue until someone has won, or there if the board is completely filled.

[Back to top](#top)

## <a name="screen"></a>Screenshots

![Main Menu](https://i.imgur.com/3TRc59Y.png)
![Settings](https://i.imgur.com/osn6TOb.png)
![Playing State](https://i.imgur.com/8ivsWAL.png)


[Back to top](#top)

## <a name="install"></a>How to Install Connect-5

### `Windows`

1.  Install [Pygame.](https://www.pygame.org/download.shtml)
2.  [Download Connect-5 zip file.](https://github.com/KyleAnthonyFerreira/Connect-5/archive/master.zip)
3.  Extract from the zip file.
4.  Open extracted files in IDE of choice.
5.  Run `Connect-5.py`.

[Back to top](#top)


## <a name="documen"></a>Documentation

The game and all of its files are located in the src folder. Outside of the src folder is the license and the readme. There should be 8 files in src in total.

### `Files`

1. Board.py
2. Connect5.py
3. Game.py
4. Player.py
5. blue button.png
6. red button.png
7. colour line.png
8. obj.pickle

The last 4 files correspond are either images for buttons or colour wheels in game, or data sturtures to hold saved games. The most important are the first 4. These first 4 contain all the code which runs the logic of the game, and provide structure for easy change.

### `Board.py`

the file Board.py has the class Board which acts as a virtual representation of the game board for connect5.

#### `Board`

**Attributes**

- dimension: int
    - dimension represents the width and height of the board where the number is the number of squares
- board: List
    - board is a list of lists. The length of the outer list is dimension and the lengths of the inner lists are dimension each. This inner lists contain empty strings that are changed as new pieces are placed.
- last_move: (int, int)
    - this tuple stores the x, y of where the last player places their piece

**Functions**

- is_valid(x: int, y: int) -> bool
    - is_valid takes in an (x,y) coordinate and checks if it goes beyond the board (index out of bound). If it is within the boundary it returns true, else returns false
- get_piece(x: int, y:int) -> str
    - get_piece takes in an (x,y) coordinate and returns a string representation of that spot on the board; the empty string means that spot is empty
- set_piece(player: Player,x: int, y:int) -> None
    - set_piece takes in a player object, and an (x,y) coordinate. If that spot is empty then the player.name attribute is placed in that position in board.
- remove_piece(x: int, y:int) -> None
    - remove_piece overwrites the (x, y) coordinate with an empty string on the board
- is_empty(x: int, y: int) -> bool
    - is_empty returns true when the corresponding (x, y) coordinate has an empty string. It also returns true if the coordinate is not valid. It will return false only when the coordinate is valid and not an empty string
- all_round() -> (int, int)
    - all_round returns a random (x, y) coordinate around the last piece placed. If no coordinates are empty then (-1, -1) is returned
- has_connect5(player1: Player, player2: Player) -> str
    - has_connect5 returns the string representation of the player who has 5 pieces in a row in any direction. has_connect5 returns an empty string if no player has accieved this yet
- _connect_n(player: Player) -> int
    - _connect_n returns the greatest amount of pieces in a row that that player has placed down
- sum_in_line(player: Player, row: int, col: int, d1: int, d2: int, is_player1: bool) -> (int, int, int)
    - sum_in_line is a complex function that determines the coordinate after a line of pieces and length of a line given a player, a starting position for the x direction, a starting position for the y direction, a step value for the x direction, a step value for the y direction, and lastly a boolean that is used to determine if the function should track the player's pieces or the opponent's pieces


### `Connect5.py`

This file contains no functions but rather runs the main game loop and instantiates several objects that are needed to run the game.

**Important Globals**

- WIDTH = int(pygame.display.Info().current_w)
    - Width of the screen; int(pygame.display.Info().current_w) sets the screen to the maximum width of the users monitor
- HEIGHT = int(pygame.display.Info().current_h)
    - Height of the screen; int(pygame.display.Info().current_w) sets the screen to the maximum height of the users monitor
- DIMENSION = 19
    - Determines how many places pieces can be placed on the game board. 19 x 19 is the standard for most connect 5 games
- GAME_STATE = 0 
    - This variable is used in the main function to determine the program should show the user the menu, settings, or the game. 0 is the menu.
- GAME_MODE = 0
    - This variable is used to determine what game mode the user wishes to play. 0 is player vs player. 1 is player vs easy AI. 2 is player vs medium AI. 3 is player vs hard AI.
- PLAYER1_COLOUR = (0, 0, 0)
    - default colour (black) for player 1; the integers represent RGB
- PLAYER2_COLOUR = (255, 255, 255)
    - default colour (white) for player 2; the integers represent RGB
- BOARD_COLOUR = (121, 122, 125)
    - colour of the board; the integers represent RGB
- BOARD_LINES_COLOUR = (255, 255, 255)
    - colour of the board lines; the integers represent RGB

**Functions**
- set_up_game() -> Game
    - set_up_game() initialized objects needed for a new game and then returns a new Game object. It initializes 2 Players, 1 Board, and 1 Game
- draw_menu() -> dict
    - draw_menu() shows the visualization of the menu to the screen and also returns a dictionary of clickable regions
- start_menu() -> None
    - start_menu() uses the regions from draw_game() to listen for user input via mouse click on what to do next 
- draw_settings() -> dict
    - draw_settings() shows the visualization of the settings to the screen and also returns a dictionary of clickable regions
- start_settings() -> None
    - start_settings() uses the regions from draw_settings() to listen for user input via mouse click on what to do next 
- draw_game(game_board: Board) -> dict
    - draw_game() draws the game board (given a Board object) to the menu and returns a dictionary of clickable regions
- update(row: int, col: int, player: Player) -> None
    - update() draws a single piece to the board given an (x, y) coordinate and a Player object
- is_clicked(click_able: dict, mouse_position: (int, int), new_game: Game) -> None
    - is_clicked() uses dictionaries from the draw functions to determine what to do upon the user clicking buttons
- start_game() -> None
    - start_game() starts a new game by calling set_up_game and has a loop that runs through the logic of the game using the Game object.

**if __name__ == "__main__"**
- Main creates the screen and sets it to full screen. Main also has the main loop that holds the menu, game, and settings together



### `Game.py`

The file Game.py only has the Game class. This class is used for starting a new game and handling the interactions between the players and the board.

#### `Game`

**Attributes**

- player1: Player
    - This is player 1 (can be Human)
- player2: Player
    - This is player 2 (can be Human or AI)
- next: Player
    - This object indicates which Player goes next
- board: Board
    - A board instance that the class can manipulate

**Functions**

- whose_turn() -> Player
    - returns the player object who's turn it currently is
- who_goes_next() -> Player
    - returns the player object who's turn is next
- is_winner() -> bool
    - returns true if a player has won the game, else false
- is_game_over() -> bool
    - returns true if a player has won or the game is tied and no one can make moves anymore, else returns false
- make_move(x: int, yL int) -> bool
    - given an x and y position a move is attempted. It returns true if the move was successful, else returns false

### `Player.py`

This file has 5 classes.

- Player
- Human
- EasyAI
- MediumAI
- HardAI

The 4 last classes extend Player. Player is considered to be abstract and is not to be  instantiated.

#### `Player`

**Attributes**

- name: str
    - string representation of the player; a name
- board: Board
    - board instance that the player can interact with
- colour: (int, int, int) # default is (0, 0, 0)
    - RGB value for the player's pieces

**Functions**

- make_a_move(x: int, y:int) -> None
    - make_a_move places a piece on the board givin an (x, y) coordinate that is both empty and valid
- get_move() -> None
    - get_move() is unimplemented in the Player class. This function passes.
- set_colour(colour: (int, int, int)) -> None
    - set_colour changes the player's colour to the new colour

The Human class is a represenation of an actual person playing the game

#### `Human`

**Attributes**

- # Same as Player except colour defaults to (65, 255, 65)

**Functions**

- # Same as Player

The easyAI is an easy AI who only seeks to play around where the other player plays

#### `EasyAI`

**Attributes**

- # Same as Player except colour defaults to (65, 65, 255)

**Functions**

- get_move()
    - get_move() is implemented in EasyAI. It preforms little board analysis and can only randomly place moves and play around the other player.

The mediumAI is a medium AI that seeks to block the other players whenever and sometimes tries to win

#### `MediumAI`

**Attributes**

- # Same as Player except colour defaults to (255, 65, 65)

**Functions**

- get_move()
    - get_move() is implemented in MediumAI. It preforms complex board analysis and attempts to block the other player from winning. It also tries to win.

The hardAI is a hard AI that seeks to block the other player when they are close to winning but otherwise attempts to win

#### `HardAI`

**Attributes**

- # Same as Player except colour defaults to (65, 65, 255)

**Functions**

- get_move()
    - get_move() is implemented in HardAI. It preforms complex board analysis and attempts to block the other player from winning. It also tries to win.



[Back to top](#top)

## <a name="Authors"></a>Authors

-	Shae Simeoni
-	Joshua Liam Pell Nelson
-	Kyle Anthony Ferreira
-	Jule Tran
-	Brandon Mackel

[Back to top](#top)

## <a name="Contributions"></a>Individual Contributions

**Shae Simeoni**

I took it upon myself to organize the group early on in hopes of alleviating stress. To do so, I initially created a rough skeleton of all classes and their respective functions. I was personally responsible for completing and documenting the Game class. As everyone worked on their designated classes, it became clear that Kyle's Connect5 class was the longest class to write. Since I finished the Game class quite early on, I focused my efforts on assisting Kyle. I restructured the GUI (theme & button alignment), wrote the update() function which visually updates the board and simplified/removed unecessary code. With regards to the Player class, I designed and coded the EasyAI algorithm. For the README file, I wrote the rough outline and "How to Install Connect-5". Lastely I aided anyone who had any Git related issues. 

**Joshua Nelson**

With respect to the coding part of this assignment, I worked on numerous functions in the board class, created the Medium AI class (which was once the HardAI), and developed the Player class. Additionally, I worked on documenting many of the functions and classes. Besides coding, I created the outline for the first group presentation project. To be more specific, I fully created the Meduim AI class (which was once the Hard AI). Additionally, I created the Player class (which was only a few lines of code). Lastly, I specifically created and or worked on the is_valid(), get_piece(), remove_piece(), has_connect5(), _connect_n(), sum_in_line(), connect_x(), and other_direction() functions. 

**Jule Tran**

Overall, my main role in this group project was begin the 'organizer' which meant that I helped the group determine when and where we would meeting for our group meetings. In addition to this, I would create a taskslist for each of the componenets of our group assignemnts to help the group stay in scope for the project. With respect to the coding aspect of this project, I was assigned to the Board class located within the file Board.py. This class contains the functions get_piece, set_piece, is_empty, has_connect5, and has_connect4, all of which I created and work on. However, when I was working on has_connect5 and has_connect4, both of them fail to work properly. As a result of this struggle, I had to pass on the finalization of these functions to my groupmates, so I cannot take credit for the current form of those functions. Regarding the README portion of this project, I was responsible for the "How to Play" section, as well as adding the screenshots.

**Brandon Mackel**

During the start of the work on Connect 5, I was responsible for making a rough outline of the abstract player class and it's subclasses. This had the methods in the classes created, but not yet implemented. I created the entire settings menu which allows for the user to customize their game. The completion of the settings menu needed the implementation of multiple helper methods and the modification of existing code in the connect5.py file. I also created the save and load features that the player can use during game play. In the README, I was responsible for the licensing of the project repository.

**Kyle Anthony Ferreira**

For programming connnect 5 my main contributions were writing several of the functions in Connect5.py and reworking the HardAI in Player.py. For Connect5.py several of the helper functions and also the main function were either created entirely or edited by Shae and Brandon. The HardAI was nearly all my work except for using some functions in Board, like sum_in_line(). I also wrote the documentation for README.md file. 

[Back to top](#top)

## <a name="license"></a>License Information

The license we chose for our project repository is the GNU General Public License v3.0. This license allows for anyone to download and modify our code. This is important to us, as we invite anyone who plays our game to also extend the game in a way that they feel improves the overall playing experience. This license also allows for the distribution of our game. We would like for as many people to play our game as possible.

[Back to top](#top)







