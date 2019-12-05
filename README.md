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

Board.py is a virtual representation of the game board for connect5.
**Attributes**
- dimension: int
    dimension represents the width and height of the board where the number is the number of squares
- board: List
    board is a list of lists. The length of the outer list is dimension and the lengths of the inner lists are dimension each. This inner lists contain empty strings that are changed as new pieces are placed.
- last_move: Tuple(int, int)
    this tuple stores the x, y of where the last player places their piece
**Functions**
- is_valid(x: int, y: int) -> bool
    is_valid takes in an x position and y position and checks if it goes beyond the board (index out of bound). If it is within the boundary it returns true, else returns false
- get_piece(x: int, y:int) -> str:
    get_piece takes in an x position and y position and returns a string representation of that spot on the board; the empty string means that spot is empty
- set_piece(player: Player,x: int, y:int) -> None:
    set_piece takes in a player object, x position, and y position. If that spot is empty then the player.name attribute is placed in that position in board.



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

**Jule Tran**

With respect to the coding aspect of this project, I was assigned to the Board class located within the file Board.py. This class contains the functions get_piece, set_piece, is_empty, has_connect5, and has_connect4, all of which I created and work on. However, when I was working on has_connect5 and has_connect4, both of them fail to work properly. As a result of this struggle, I had to pass on the finalization of these functions to my groupmates, so I cannot take credit for the current form of those functions. Regarding the README portion of this project, I was responsible for the "How to Play" section, as well as adding the screenshots.

**Brandon Mackel**

During the start of the work on Connect 5, I was responsible for making a rough outline of the abstract player class and it's subclasses. This had the methods in the classes created, but not yet implemented. I created the entire settings menu which allows for the user to customize their game. The completion of the settings menu needed the implementation of multiple helper methods and the modification of existing code in the connect5.py file. I also created the save and load features that the player can use during game play. In the README, I was responsible for the licensing of the project repository.

**Kyle Anthony Ferreira**

For programming connnect 5 my main contributions were writing several of the functions in Connect5.py and reworking the MediumAI in Player.py. For Connect5.py several of the helper functions and also the main function were either created entirely or edited by Shae and Brandon. 

[Back to top](#top)

## <a name="license"></a>License Information

The license we chose for our project repository is the GNU General Public License v3.0. This license allows for anyone to download and modify our code. This is important to us, as we invite anyone who plays our game to also extend the game in a way that they feel improves the overall playing experience. This license also allows for the distribution of our game. We would like for as many people to play our game as possible.

[Back to top](#top)
