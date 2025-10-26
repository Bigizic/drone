# MY Journey into drone programming

Youtube vide watched: https://youtube.com/playlist?list=PLgiealSjeVyx3t4N9GroE29SbVwhYrOtL&si=R1vkn3LYNTPVLyZk

Tools used:

-[x] Ardupilot

### STEP 1:

I downloaded Ardupilot from the ardupilot github i swtiched to the ``Copter-4.5`` branch and use the command to clone the ardupilot directory

```bash
git clone -b Copter-4.5 https://github.com/ArduPilot/ardupilot.git
```

from the ``Tools/autotest`` dir i ran the command

```bash
git submodule update --init --recursive
```

to update the directories that are git repos to their latest version

then i ran the command

```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot$ ./waf list_boards
```

in the ardupilot dir to see a list of the different hardware boards that are available to us and to see different hardware types we can compile to
