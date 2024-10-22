import json

class Signal_information(object):
    def __init__(self,s_p:float,paths:list):
        self._signal_power = s_p
        self._noise_power = 0.0
        self._latency = 0.0
        self._path = paths

    @property
    def signal_power(self):
        return self._signal_power

    def update_signal_power(self,inc):
        self._signal_power += inc

    @property
    def noise_power(self):
        return self._noise_power

    @noise_power.setter
    def noise_power(self,val):
        self._noise_power = val

    def update_noise_power(self,inc):
        self._noise_power += inc

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def latency(self,val):
        self._latency = val

    def update_latency(self,inc):
        self._latency += inc

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self,value):
        self._path = value

    def update_path(self):
        if self._path:
            self._path.pop(0)


class Node(object):
    def __init__(self,node_data:dict):
        self._label = node_data['label']
        self._position = tuple(node_data['position'])
        self._connected_nodes = node_data['connected_nodes']
        self._successive = {}

    @property
    def label(self):
        return  self._label

    @property
    def position(self):
        return self._position

    @property
    def connected_nodes(self):
        return self._connected_nodes

    @property
    def successive(self):
        return self._successive

    @successive.setter
    def successive(self,val):
        self._successive = val

    def propagate(self,sig_info : Signal_information):
        if sig_info.path:
            first_node = sig_info.path[0]

            # Check if the current node is the first in the signal's path
            if first_node == self.label:
                sig_info.update_path()
                if sig_info.path:
                    next_node_label = sig_info.path[0]

                    # If the next node exists in successive, propagate to it
                    if next_node_label in self._successive:
                        next_node = self._successive[next_node_label]
                        next_node.propagate(sig_info)


class Line(object):
    def __init__(self):
        pass

    @property
    def label(self):
        pass

    @property
    def length(self):
        pass

    @property
    def successive(self):
        pass

    @successive.setter
    def successive(self):
        pass

    def latency_generation(self):
        pass

    def noise_generation(self):
        pass

    def propagate(self):
        pass


class Network(object):
    def __init__(self):
        pass

    @property
    def nodes(self):
        pass

    @property
    def lines(self):
        pass

    def draw(self):
        pass

    # find_paths: given two node labels, returns all paths that connect the 2 nodes
    # as a list of node labels. Admissible path only if cross any node at most once
    def find_paths(self, label1, label2):
        pass

    # connect function set the successive attributes of all NEs as dicts
    # each node must have dict of lines and viceversa
    def connect(self):
        pass

    # propagate signal_information through path specified in it
    # and returns the modified spectral information
    def propagate(self, signal_information):
        pass