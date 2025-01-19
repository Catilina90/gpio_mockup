import importlib.resources as resources
import json

BOARD = "board"
LOW = 0
HIGH = 1
OUT = "output"
IN = "input"

"""
Current states of all GPIO channels is written in the board_config.json file and may 
be retrieved from there if required (e.g. to check if an output is high or low)
"""


def setmode(*args, **kwargs):
    # initiate with creating a json file for tracking states
    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "w") as board_config:
            print(f"Config Path: {board_config}")
            config = []
            json.dump(config, board_config)


def setup(channel, setting, state=LOW):
    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "r") as board_config:
            config = json.load(board_config)
            print(f"before append: {config}")
            # TODO: Check if channel is already configured

    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "w") as board_config:
            config.append({"channel": channel, "setting": setting, "state": state})
            print(f"after append: {config}")
            json.dump(config, board_config)


def output(channel, state):
    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "r") as board_config:
            config = json.load(board_config)

            _ = [i.update({"state": state}) for i in config if i["channel"] == channel]
            print(f"output config: {config}")

    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "w") as board_config:
            json.dump(config, board_config)


def input(channel):

    with resources.path("RPi.data", "board_config.json") as path:
        with open(path, "r") as board_config:
            config = json.load(board_config)

            print(f"input config: {config}")

            pin_config = [i for i in config if i["channel"] == channel][0]

            if pin_config["setting"] == OUT:
                return pin_config["state"]

            else:
                print("TODO")
