# Vision2.0

Steps to Setup / Run / Code the Files :

    1. Download Visual Studio Code from https://code.visualstudio.com/

    2. Add Python as an extention in and on Visual Studio Code

    3. Download the Recomended file (Python 3.10) from this website (If you are using windows) - https://www.python.org/downloads/release/python-3100/
    
    4. Run the .exe file to download it

    5. In a Visual Studio Code file - At the top left of the window (next to the "file", "edit", and "selection" drop down menues) click the "view" drop down menue

    6. In the view drop down menue select the "Command Palette" and search for and select "python: select interpreter" and change the python version to python 3.10

    7. Select "Command Palette" again and seach for and select "python: create envirnment" and select ".venv" for python 3.10

    8. Close and reopen the powershell in Visual Studio Code and run the following commands in order :
        8a. pip install numpy == 1.24.4
        8b. pip install tensorflow == 2.11.0
        8c. pip install keras-ocr == 0.8.8
        8d. pip install opencv-python

    9. Due to issues with compatibility you may have to run these two commands in the powershell as well (This is due to the fact that, at least for me, installing tensorflow instals a version of numpy that is in the 2.xx.x which is not compatible with keras-ocr) :
        9a. pip install numpy == 1.24.4
        9b. pip install -- no-deps tensorflow == 2.11.0

    10. Go to the explorer tab or welcome tab is Visual Studio Code and create new python files for each of the files

    11. Go to this Github link - https://github.com/RobocupBSM2025/Vision2.0

    12. Copy the code from the respective files and paste it into visual studio code

    Additonal Info :

        To run things in Visual Studio Code in python you will need to instal the "Python Debugger"

        In addition I have something call "Pylance" installed and while I do not know if it is nessary, it might be so it could be helpful to insall it.
