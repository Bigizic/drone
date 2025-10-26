# MY Journey into drone programming

Youtube vide watched: https://youtube.com/playlist?list=PLgiealSjeVyx3t4N9GroE29SbVwhYrOtL&si=R1vkn3LYNTPVLyZk

Tools used:

- [x] Ardupilot

## Day 1:

1. I downloaded Ardupilot from the ardupilot github i swtiched to the ``Copter-4.5`` branch and use the command to clone the ardupilot directory

```bash
git clone -b Copter-4.5 https://github.com/ArduPilot/ardupilot.git
```

2. from the ``Tools/autotest`` dir i ran the command

```bash
git submodule update --init --recursive
```

to update the directories that are git repos to their latest version

3. then i ran the command below in the ardupilot dir to see a list of the different hardware boards that are available to us and to see different hardware types we can compile to


```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot$ ./waf list_boards
```

4. i ran the command below to find the sitl drone software that would be used 
```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot$ ./waf list_boards | grep sitl
```

5. in this step i ran my first sitl drone using the sim_vehicle.py in the ``drone/ardupilot/Tools/autotest`` dir 
```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot/Tools/autotest$ ls
aircraft                   fakepos.py         README
antennatracker.py          fg_plane_view.bat  rover.py
arducopter.py              fg_plane_view.sh   run_in_terminal_window.sh
ArduCopter_Tests           fg_quad_view.bat   run_mission.py
arduplane.py               fg_quad_view.sh    sailboat.py
ArduPlane_Tests            Generic_Missions   "sim_vehicle.py"
ArduRover_Tests            helicopter.py      swarminit.txt
ardusub.py                 __init__.py        template
ArduSub_Tests              jsb_sim            test_build_options.py
autotest.py                junit.xml          tilecache
balancebot.py              locations.txt      validate_board_list.py
bisect-helper.py           logger_metadata    vehicle_test_suite.py
blimp.py                   models             web
check_autotest_speedup.py  param_metadata     web-firmware
default_params             pysim              win_sitl
examples.py                quadplane.py       XPlane
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot/Tools/autotest$
```
then i ran the vehicle simulator in the ArduCopter dir, which tells sim_vehicle i would like to build the AduCopter vehicle. Vehicles can be built by running sim_vehicle from the current dir of the Vehicle, for example

```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot$ ls
AntennaTracker  Blimp               Dockerfile   modules         tests
"ArduCopter"      build               docs         pyproject.toml  Tools
"ArduPlane"       BUILD.md            Doxyfile.in  README.md       Vagrantfile
"ArduSub"         CODE_OF_CONDUCT.md  libraries    Rover           waf
benchmarks      COPYING.txt         Makefile     tasklist.json   wscript
```

ArduCopter, ArduPlanem ArduSub are vehicles and i can ``cd`` into any and run sim_vehicle from the dir

6. i wrote an alias for sim_vehicle so i don't have to know the path it's in everytime i want to run it:

```bash
echo "alias sim_vehicle='python3 /home/lex/drone/ardupilot/Tools/autotest/sim_vehicle.py'" >> ~/.bashrc 

source ~/.bashrc
```






