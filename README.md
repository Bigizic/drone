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

7. I tried to compile ArduCopter vehicle simulation with the command ``simvehicle --map --console``and got an error:
> you need to install empy with 'python -m pip install empy==3.3.4'

```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot/ArduCopter$ simvehicle --map --console
SIM_VEHICLE: Start
SIM_VEHICLE: Killing tasks
SIM_VEHICLE: Starting up at SITL location
SIM_VEHICLE: WAF build
SIM_VEHICLE: Configure waf
SIM_VEHICLE: "/home/lex/drone/ardupilot/modules/waf/waf-light" "configure" "--board" "sitl"
Setting top to                           : /home/lex/drone/ardupilot 
Setting out to                           : /home/lex/drone/ardupilot/build 
Autoconfiguration                        : enabled 
Checking for program 'python'            : /usr/bin/python 
Checking for python version >= 3.6.9     : 3.8.10 
Setting board to                         : sitl 
Using toolchain                          : native 
Checking for 'g++' (C++ compiler)        : /usr/bin/g++ 
Checking for 'gcc' (C compiler)          : /usr/bin/gcc 
Checking for c flags '-MMD'              : yes 
Checking for cxx flags '-MMD'            : yes 
CXX Compiler                             : g++ 9.4.0 
Checking for need to link with librt     : not necessary 
Checking for feenableexcept              : yes 
Enabling -Werror                         : no 
Enabled OpenDroneID                      : no 
Enabled firmware ID checking             : no 
GPS Debug Logging                        : no 
Enabled custom controller                : yes 
Checking for HAVE_CMATH_ISFINITE         : yes 
Checking for HAVE_CMATH_ISINF            : yes 
Checking for HAVE_CMATH_ISNAN            : yes 
Checking for NEED_CMATH_ISFINITE_STD_NAMESPACE : yes 
Checking for NEED_CMATH_ISINF_STD_NAMESPACE    : yes 
Checking for NEED_CMATH_ISNAN_STD_NAMESPACE    : yes 
Checking for header endian.h                   : yes 
Checking for header byteswap.h                 : yes 
Checking for HAVE_MEMRCHR                      : yes 
Configured VSCode Intellisense:                : no 
DC_DSDL compiler                               : /home/lex/drone/ardupilot/modules/DroneCAN/dronecan_dsdlc/dronecan_dsdlc.py 
Source is git repository                       : yes 
Update submodules                              : yes 
Checking for program 'git'                     : /usr/bin/git 
Checking for program 'size'                    : /usr/bin/size 
Benchmarks                                     : disabled 
Unit tests                                     : enabled 
Scripting                                      : maybe 
Scripting runtime checks                       : enabled 
Debug build                                    : disabled 
Coverage build                                 : disabled 
Force 32-bit build                             : disabled 
Checking for program 'rsync'                   : /usr/bin/rsync 
'configure' finished successfully (1.279s)
{'model': '+', 'waf_target': 'bin/arducopter', 'default_params_filename': 'default_params/copter.parm', 'sitl-port': True}
SIM_VEHICLE: Building
SIM_VEHICLE: "/home/lex/drone/ardupilot/modules/waf/waf-light" "build" "--target" "bin/arducopter"
Waf: Entering directory `/home/lex/drone/ardupilot/build/sitl'
Embedding file locations.txt:Tools/autotest/locations.txt
Embedding file models/Callisto.json:Tools/autotest/models/Callisto.json
Embedding file models/plane-3d.parm:Tools/autotest/models/plane-3d.parm
Embedding file models/plane.parm:Tools/autotest/models/plane.parm
Embedding file models/xplane_heli.json:Tools/autotest/models/xplane_heli.json
Embedding file models/xplane_plane.json:Tools/autotest/models/xplane_plane.json
you need to install empy with 'python -m pip install empy==3.3.4'
SIM_VEHICLE: Build failed
SIM_VEHICLE: Killing tasks

```

i already have python3 installed but i had to create a symlink bettwen ``python`` and ``python3`` so python resolves to python3 by default
```bash
sudo ln -s /usr/bin/python3 /usr/bin/python
```
then i tried to fix the error:
```bash
lex@lex-HP-EliteBook-x360-1030-G2:~/drone/ardupilot/ArduCopter$ python -m pip install empy==3.3.4
Collecting empy==3.3.4
  Downloading empy-3.3.4.tar.gz (62 kB)
     |████████████████████████████████| 62 kB 161 kB/s 
Building wheels for collected packages: empy
  Building wheel for empy (setup.py) ... done
  Created wheel for empy: filename=empy-3.3.4-py3-none-any.whl size=29329 sha256=4cdffc52e2efc180e897cf13c43b936ff9d673f9223ba05630de5d55c7b6e3de
  Stored in directory: /home/lex/.cache/pip/wheels/b0/d7/80/0e8ad4f073e05b2435c3b4c12c230cb219135bae4f59978612
Successfully built empy
Installing collected packages: empy
Successfully installed empy-3.3.4
```


got another error:

```bash

Waf: Leaving directory `/home/lex/drone/ardupilot/build/sitl'
Build failed
Traceback (most recent call last):
  File "/home/lex/drone/ardupilot/modules/waf/waflib/Task.py", line 350, in process
    ret = self.run()
  File "/home/lex/drone/ardupilot/Tools/ardupilotwaf/mavgen.py", line 54, in run
    from pymavlink.generator import mavgen
  File "/home/lex/drone/ardupilot/modules/mavlink/pymavlink/generator/mavgen.py", line 28, in <module>
    from future import standard_library
ModuleNotFoundError: No module named 'future'

SIM_VEHICLE: Build failed
SIM_VEHICLE: Killing tasks
```

different one this time:

fixed it with ``pip install future``

### Day 2

There was no GUI interface so i donwloaded python libraries to work with MavProxy, official documentation [here](https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html)

command used to fix GUI issue

```bash
sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame
python3 -m pip install PyYAML mavproxy --user
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc
```

then update

```bash
python3 -m pip install mavproxy pymavlink --user --upgrade
python3 -m pip install mavproxy --user git+https://github.com/ArduPilot/mavproxy.git@master
```

run ``simvehicle --map --console`` and the GUI loads up










