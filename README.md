# WhatsTheCatch
Engr100 Project  &lt;3

=== Alpha Release Notes ===

To run the game, run Tester.py in Eclipse

Please note that due to time constraints on the alpha release, some of the controls of the game have changed from what was written in the user manual. Specifically:

* Use the up, down arrow keys to move the fishing hook. 
* Use the right, left arrow keys to move the fishing boat. 
* The fishing hook can catch only 1 fish, and you must raise it to the surface, whether or not you caught the fish you wanted.
* If the fish you caught has a correct word for the given sentence, then a blank will be filled in. If the fish you caught has an incorrect word, then nothing happens. 
* If the fishing hook touches an electric eel, you lose a life and the fishing hook goes back to the surface.
* If the fishing line touches an electric eel, you lose a life and the fishing hook goes back to the surface.
* If you run out of lives, the game stops running and you must close the window and restart to try again.

=== Beta Release Notes ===

To run the game, import the project into Eclipse, and run Menu.py

* All Alpha Release controls still apply (up, down, right left arrow keys) 
* Attractive graphics
* Menu with instructions
* More sentences (if you're bored, feel free to make your own in sample.txt, but follow the formatting correctly - note: if the game crashes because you misformatted a sentence, it's not our fault)
* You get 50 points per correct word
* You get an additional 25 points per sentence that is completed
* You lose 50 points per incorrect word
* If you catch an incorrect fish (bring it to the surface), you'll hear an awful sound
* If you hook a fish you don't want, press SPACE to release it
* If you catch a correct fish, you'll hear a pleasing sound
* If an eel hits your fishing line or hook, you'll hear an electric sound
* As you complete more sentences, the fish and eels will move faster
* If you do catch too many incorrect fish, we feel sorry for you, and eventually, there will only be correct fish left for you to catch
* If you lose all three of your lives, the game ends, and you will be offered to return to the main menu. There, if you click "Play Game," the game will restart
* If the game is still going on and you exit the game screen, it will pause and bring you back to the main menu. You can resume your game by clicking "Play Game"

=== Final Release notes ===

To run the game, import the project into Eclipse, and run Menu.py

* All Alpha Release controls still apply (up, down, right left arrow keys)
* All Beta Release notes still apply
* New game starts a new game, continue game continues the last game you started (or starts a new game if there was no previous game)
* Instrutions are now improved
* Select a sentence set you want to play in "Sentences"
* Select the boat avatar in "Customizations"
* Create your own sentence sets following the structure outlined in sample.txt
* Best scores on sentence sets are recorded after you complete a sentence set. 
* Background music
* Last incorrect fish is shown with a red X over it

=== Grading rubric ===
* Non-trivial Implementation (18)
  * Sound and/or music: We have sounds (played when you catch a fish) and background music. The background music works if the pygame on your computer can work with it. It works on ours. +2
  * Graphics: We have graphics. They're not the best, but they're decent. +3
  * Physics: No physics. +0
  * Multiple levels/difficulties: We have multiple sentence sets allowing the user to choose whatever difficulty/subject s/he wants. We also have multiple difficulties within each sentence set. As the user completes more sentences, the fish and eels speed up. +4
  * Complex interactions between player and other objects: Hook interacts with fish and Eel. The eels interact with the fishing line and hook. Colliding the eel with the variable length fishing line was nontrivial. +2
  * Complex properties of player (health, shields,...): We have lives. +1
  * Multiple players: We have a hidden 2-player mode. +1
  * Universe bigger than screen: No. +0
  * Other: Sentence generation is nontrivial and is a big part of our game. It does not fit in any category though. It uses a lot of File I/O which was not covered in lecture and it is capable of recording scores, number of sentence sets mastered, as well as allows you to create any sentence sets you want in the sentences folder. This gives our game a much wider target audience. +5
* Game Play (20)
  * Larger gameplay goals past single level of goals: You want to master (get perfect score) all the sentence sets, and the game records your overall progress and best score. +2
  * Originality of the game: Seems original... +3
  * Dynamic difficulty adjustment: If you get too many wrong fish, only correct fish will be left for you to catch. This removes any possible source of frustration. In our opinion, this is pretty clever, elegant, and original. If you complete many sentences, the fish and eels swim faster. +4
  * Availability of cheat codes: You can toggle two hidden modes, jetpack and 2-player, on/off in the menu screen. +2
* Customer Focus (20)
  * Goals are well understood, well integrated, and appropriately rewarding: By design, the game seems simple to understand: catch the right fish, don't catch the wrong fish, avoid the eels. You probably don't even need to read the instructions to figure it out. You get rewarded for catching the right fish (mastery of the sentence set, getting points, hearing nice sound), and are punished for getting the wrong fish (hearing awful sound, incorrect fish has an X over it). +2
  * Feedback informs players of what is important: You hear sounds (good/bad) depending on whether you caught the right fish or not. The last wrong fish remains on the screen reminding you of what you did incorrectly. +2
  * User modifiable settings: You can change your boat color and you can change the sentence set that you want to play. If you are an instructor, you can make your own sentence sets in whatever language you want and tailor the game to whatever severity of ASD your student has. We think that's pretty sophisticated. +5
  * Menu functionality: We have New Game, Continue Game, Instructions, Sentences, Customizations, Credits, Quit. The instructions are modular with next and prev buttons, the sentences let you select whatever set you want from existing sets, and the customizations let you highlight the avatar that you want. This seems pretty decent. +3
 
Total: 98
