# RainbowsEndPy
A Python port of the [Rainbow's End](https://github.com/csshelton70/RainbowsEnd) PBEM game written by Russell Wallace.

## Description
Rainbow's End was a PBEM ( Play-By-Email ) game written by Russell Wallace in the early 2000s.  As far as I know, this may have been the last PBEM game that he created.  His past works included Atlantis, Olympia and Galaxy.  

I am porting this game to Python mainly because I want to learn how to program in python and I know the best way for me to learn something is to relate it to something I already know.  My intent is slowly convert the code, while also using a TDD approach.  The original game took in data files and processed them all at once but I want to expand upon that and be able to read email as well as expose an API that will allow the creation of a game client at some point -- hopefully also python based.

## Status
In Progress


## Libraries Used
wxPython
pyTest

## Settings Modified
Add: "python.linting.pylintArgs": ["--extension-pkg-whitelist=wx"]
Reason: To prevent pylint from giving a warning about wxPython frames


