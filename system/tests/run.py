#
#  /$$   /$$                 /$$           /$$       /$$  /$$$$$$          
# | $$$ | $$                | $$          | $$      |__/ /$$__  $$         
# | $$$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$ | $$       /$$| $$  \__//$$$$$$  
# | $$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$| $$      | $$| $$$$   /$$__  $$ 
# | $$  $$$$| $$  \ $$| $$  | $$| $$$$$$$$| $$      | $$| $$_/  | $$$$$$$$ 
# | $$\  $$$| $$  | $$| $$  | $$| $$_____/| $$      | $$| $$    | $$_____/ 
# | $$ \  $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$$| $$| $$    |  $$$$$$$ 
# |__/  \__/ \______/  \_______/ \_______/|________/|__/|__/     \_______/ 
#
# @author Jackthehack21 <gangnam253@gmail.com | Jackthehaxk21##860>
#
# This project and all its content is distributed under the GPL-V3 license

def exec():
    from system.utils import logger
    import time, platform, system.ver, os, sys

    from system.utils.initialise import init
    from system.network import autoUpdate
    init() #ENABLES COLOUR (WRAPS STDOUT & ERR) for win.

    def pr(msg, lvl):
        logger.log(msg, lvl)

    pr('Booted on '+time.asctime(), 0)
    import ctypes
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("NodeLife: Will you survive ?")
        pr('Updated screen title',0)
    except AttributeError:
        pr('Unable to set title',0) #Linux & MacOS
    pr('Checking deployment type...',0)
    if(not system.ver.release()):
        pr('Your running a development build, instead of a release please be aware this build has issues and if you dont know why your seeing this get a release from\nhttps://github.com/Jackthehack21/NodeLife/releases\n', 2)
    else:
        pr('running released version',0)
    pr('Checking System...', 1)
    time.sleep(0.5)
    system = platform.uname()
    if(system.system.lower() != 'windows' and system.system.lower() != 'linux'):
        pr('Your system \''+system.system+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehack21/NodeLife)', 2)
    if(system.machine.lower() != 'amd64' and system.machine.lower() != 'x64'):
        pr('Your CPU running \''+system.machine+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehack21/NodeLife)', 2)
    pr('System Check Complete.',0)
    pr('Checking for updates...', 1)
    autoUpdate.check(True)
    pr('Update Check Complete.',0)
    pr('Starting Game...', 1)
    time.sleep(3)
    print('\x1b[2J')

    from system import boot
    boot.run(True)
    pr('Game ended.',0)
