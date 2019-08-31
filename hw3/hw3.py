import requests
import re

def analyse():
    cmd = input("")

    cmd_list = cmd.split()
    
    input_path = cmd_list[0]
    output_path = cmd_list[1]

    try:
        with open(input_path, "r") as fi:
           pass

    except IOError:
        print("Error: Input file not exist!")
        return

    try:
        with open(output_path, "w") as fo:
            pass

    except IOError:
        print("Error: Output file creat failed!")
        return

analyse()