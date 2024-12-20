import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from core.elements import Signal_information,Node,Line,Network

# Exercise Lab3: Network

ROOT = Path(__file__).parent.parent
INPUT_FOLDER = ROOT / 'resources'
file_input = INPUT_FOLDER / 'nodes.json'


# Load the Network from the JSON file, connect nodes and lines in Network.
# Then propagate a Signal Information object of 1mW in the network and save the results in a dataframe.
# Convert this dataframe in a csv file called 'weighted_path' and finally plot the network.
# Follow all the instructions in README.md file

network = Network(file_input)
network.connect()
Path_A_F = network.find_paths("A","C")

Sig_info = Signal_information(1e-3,Path_A_F[0])
print(Sig_info.path)
Info_path = {'Paths': ['->'.join(path) for path in Path_A_F]}

A_B = network.propagate(Sig_info)



