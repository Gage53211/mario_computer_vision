# Mario 1-1 Completer

This is a small collection of python scripts designed to complete the first level of Nintendo's "Super Mario Bros" via a technique known as template matching to find the position of things on the screen.


## Prerequisites

This program looks for an application called "Mesen" which is an NES emulator

you can download it from this link here:
https://www.mesen.ca/

You must also have Python and Pip installed.

You must also source your own super mario bros (non PAL) rom.


## Running This Program (Windows)

First, make sure that you are on the windows branch (main). Then install the dependencies for the code using the commands below.
    
    #in ..\<Root Of Repo> 
    
    python -m venv venv     # creates virtual enviornment
    cd venv\Scripts         # cd to activation script
    activate                # activates virtual enviornment
    cd ..                   # go back to root |
    cd ..                   # go back to root |
    pip install -r req.txt  # installs dependencies


Next, you must name your super mario .nes file "Super Mario Bros" so that the emulator can be detected by the program. 

    #file name should be...
    Super Mario Bros.nes

Then run the emulator. If the emulator is being run for the first time, select only the arrow keys as the control scheme.

<img width="392" height="506" alt="first_time_run_mesen_img" src="https://github.com/user-attachments/assets/cde25935-1f43-4c70-b451-d541db3192f0" />

Then click on the "File" option at the top of the toolbar and click "Open". Once your file explorer opens, find your "Super Mario Bros.nes" file and double click it to start the game.


Now back in your console, navigate to the “bin” folder of this application code. Once inside, use…

	#in ..\<Root Of Repo>\bin  
    python play.py 

    #or from ..\<Root Of Repo>
    python3 bin\play.py

To run the code.

Once the code is running, don't touch your mouse or the keyboard and watch as the program completes 1-1.


## Running This Program (Mac)

First, make sure that you are on the windows branch (main). Then install the dependencies for the code using the commands below.
    
    #in ..\<Root Of Repo> 
    
    python3 -m venv venv                    # creates virtual enviornment
    source  venv/bin/activate               # activates virtual enviornment
    python3 -m pip install -r req.txt       # installs dependencies

Next, you must name your super mario .nes file "Super Mario Bros" so that the emulator can be detected by the program. 

    #file name should be...
    Super Mario Bros.nes

The emulator requests that SDL2 is on your computer which can be aquired with a package manager known as brew.

You can get brew by using the following command inside of your terminal...

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Once brew is installed, run the following command to install "SDL2"...

    brew install sdl2


When that finishes installing, run the emulator. If the emulator is being run for the first time, select only the arrow keys as the control scheme.

<img width="392" height="506" alt="first_time_run_mesen_img" src="https://github.com/user-attachments/assets/cde25935-1f43-4c70-b451-d541db3192f0" />


Due to technical reasons and time constraints you will need to go to "Settings" in the tool bar and then "preferances" at the bottom of the list and then "Shortcut Keys" to change some of the keybinds. below is a list of keybinds that need to be changed.

    Action        Default Keybind           New Keybind

    Reset:            Ctrl+R         ---->      r
    Set Scale 1x:     Alt+1          ---->      1
    Set Scale 2x:     Alt+2          ---->      2
    Set Scale 3x:     Alt+3          ---->      3
    Set Scale 4x:     Alt+4          ---->      4
    Set Scale 5x:     Alt+5          ---->      5
    Set Scale 6x:     Alt+6          ---->      6
    Set Scale 7x:     Alt+7          ---->      7
    Set Scale 8x:     Alt+8          ---->      8
    Set Scale 9x:     Alt+9          ---->      9


Once your keybinds are setup, back out of the settings and click on the "File" option at the top of the toolbar and click "Open". Once your file explorer opens, find your "Super Mario Bros.nes" file and double click it to start the game.


Now back in your console, navigate to the “bin” folder of this application code. Once inside, use…

	#in ..\<Root Of Repo>\bin  
    python3 play.py 

    #or from ..\<Root Of Repo>
    python3 bin\play.py

To run the code.

Once the code is running, It may ask for some permissions relating to controling your keyboard. Accept them, then don't touch your mouse or the keyboard and watch as the program completes 1-1.
