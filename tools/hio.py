from huepy import *
import os, time, sys

def banner():

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

def kit_one():

    try:

        os.system('cls') if os.name == 'nt' else os.sytem('clear')
        banner()

        print(green("""
            ╔──────────────────────────────────────────────────────────╗
            |                     H4CK-IN-ONE                          |
            |──────────────────────────────────────────────────────────|
            |   [1] EMAIL SPOOFING     |     [2] CARDING TOOLKIT       |
            |                          |                               |
            |   [3] SPAMMER            |     [4] DOXING TOOLS          |
            |                          |                               |
            ┖──────────────────────────────────────────────────────────┙\n"""))

        case = input(yellow("$ "))

        if case == '1':
            os.system('bash tools/FAQUE/faque.sh')

        elif case == '2':
            os.system('python tools/azathot/azathot1.py')

        elif case == '3':
            os.system('python tools/autospamer.py')

        elif case == '4':
            os.system('bash tools/gvngs.sh')
        
        else:
            print(bad("An Error Occurred..."))
    
    except:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(good("Finish."))
        exit()
    
kit_one()
