from huepy import *
import os, time

def banner():

    os.system('cls') if os.name == 'nt' else os.system('clear')

    print(red("""
    $$\   $$\                     $$\             $$$$$$\             $$\   
    $$ |  $$ |                    $$ |            \_$$  _|          $$$$ |  
    $$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\         $$ |  $$$$$$$\  \_$$ |  
    $$$$$$$$ | \____$$\ $$  _____|$$ | $$  |$$$$$$\ $$ |  $$  __$$\   $$ |  
    $$  __$$ | $$$$$$$ |$$ /      $$$$$$  / \______|$$ |  $$ |  $$ |  $$ |  
    $$ |  $$ |$$  __$$ |$$ |      $$  _$$<          $$ |  $$ |  $$ |  $$ |  
    $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       $$$$$$\ $$ |  $$ |$$$$$$\ 
    \__|  \__| \_______| \_______|\__|  \__|      \______|\__|  \__|\______|\n""")
    + green("                                                                          V.1.0\n"))

def azathot():

    banner()

    print(green("""
            ╔──────────────────────────────────────────────────────────╗
            |                     H4CK-IN-ONE                          |
            |──────────────────────────────────────────────────────────|
            |   [1] CC - GEN           |     [2] BIN - INFO            |
            |                          |                               |
            |   [3] TEMP EMAIL         |     [4] CHECKER               |
            |                          |                               |
            ┖──────────────────────────────────────────────────────────┙\n"""))

    case = input(yellow("$ "))

    if case == '1':
        os.system('python tools/azathot/azathot.py --tool CC-GEN')

    elif case == '2':
        os.system('python tools/azathot/azathot.py --tool BIN-INFO')

    elif case == '3':
        os.system('python tools/azathot/azathot.py --tool TEMP-MAIL')

    elif case == '4':
        os.system('python tools/azathot/azathot.py --tool CHECKER')

    else:
        print(bad('Try again...'))
        time.sleep(2.5)
        azathot()

azathot()