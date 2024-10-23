import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import core.elements
from core.elements import Signal_information,Node

# Exercise Lab3: Network

ROOT = Path(__file__).parent.parent
INPUT_FOLDER = ROOT / 'resources'
file_input = INPUT_FOLDER / 'nodes.json'


# Load the Network from the JSON file, connect nodes and lines in Network.
# Then propagate a Signal Information object of 1mW in the network and save the results in a dataframe.
# Convert this dataframe in a csv file called 'weighted_path' and finally plot the network.
# Follow all the instructions in README.md file
# USE THE ROOT TO OPEN THE JSON FILE
with open('/home/andrea/Desktop/OOn/lab3-network-andrea22-rgb/resources/nodes.json','r') as file:
    network_data = json.load(file)

nodes = {}
for label, data in network_data.items():
    node_info = {
        'label': label,
        'position': data['position'],
        'connected_nodes': data['connected_nodes']
    }
    nodes[label] = Node(node_info)

# Step 2: Set up successive links based on connected_nodes
for label, node in nodes.items():
    successive_links = {}
    for connected_node_label in node.connected_nodes:
        if connected_node_label in nodes:
            successive_links[connected_node_label] = nodes[connected_node_label]
    node.successive = successive_links

# Step 3: Create a signal information object with a specific path
signal_info = Signal_information(10.0, ["A", "D", "E", "F"])

# Step 4: Start the propagation from node A
nodes["B"].propagate(signal_info)

print(nodes["B"].successive)
