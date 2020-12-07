"""
Day 7 is essentially a graph problem with different questions about the quality
of the graph. Part 1 is asking the number of nodes that are parent to a given
base.
"""
import time
from typing import List
from copy import deepcopy

class BagGraph:
    def __init__(
            self,
            rules: List[str]):
        self.graph = {}
        rules = self.parse_rules(rules)
        self.build_graph(rules)

    def parse_rules(self, rules: List[str]) -> dict:
        rules_dict = {}
        for rule in rules:
            bag, rule = rule.split('contain')
            bag = ' '.join(bag.split()[0:-1]).strip()
            rule = rule[1:-1]
            children_rules = [r.strip().split() for r in rule.split(',')]

            if len(children_rules) == 1 and children_rules[0][0] == 'no':
                rules_dict[bag] = []
            else:
                rules_dict[bag] = [(int(b[0]), ' '.join(b[1:-1])) for b in children_rules]

        return rules_dict

    def build_graph(self, rules: dict) -> int:
        # Add nodes to graph
        #bags_strs = [rule.split('contain')[0].strip() for rule in rules]
        bags = [b for b in rules]

        # Add all the empty nodes to the graph
        for bag in bags:
            self.add_node(bag)

        # Connect them all
        for bag, children in rules.items():
            node = self.get_node(bag)
            node.add_children(children, self)

    def get_node(self, bag: str) -> object:
        return self.graph[bag]

    def add_node(self, node_str: str) -> None:
        self.graph[node_str] = BagNode(node_str)

class BagNode:
    def __init__(self, key: str):
        self.key = key
        self.visited = False

        # Each dict for children contain the node of their children
        # as well as the number of those bags this bag's parents nodes
        self.parents = []
        self.children = [] # List of edges

    def get_key(self) -> str:
        return self.key

    def get_parents(self) -> list:
        return self.parents

    def get_children(self) -> list:
        return self.children

    def add_children(self, children, graph) -> None:
        for quantity, child in children:
            child_node = graph.get_node(child)
            child_node.add_parent(self)
            self.children.append(Edge(child_node, quantity))

    def add_parent(self, parent: object) -> None:
        self.parents.append(parent)

class Edge:
    def __init__(self, target: object, weight: int):
        self.node = target
        self.weight = weight


def part1(bag, graph):
    node = graph.get_node(bag)

    parents = [p.key for p in node.get_parents()]
    num_bags = 0
    while parents:
        cur_node = graph.get_node(parents.pop())
        if not cur_node.visited:
            num_bags += 1
            cur_node.visited = True
            parents.extend([p.key for p in cur_node.get_parents()])

    return num_bags

def part2(bag, graph):
    node = graph.get_node(bag)

    children_edges = [(k,1) for k in node.get_children()]
    num_bags = 0
    while children_edges:
        edge, multiplier = children_edges.pop()
        cur_node = edge.node
        cur_num_bags = edge.weight
        num_bags += cur_num_bags * multiplier
        children = [(k, multiplier*cur_num_bags) for k in cur_node.get_children()]
        children_edges.extend(children)

    return num_bags

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        rules = [l.strip() for l in f.readlines()]

    bag_graph = BagGraph(rules)

    print(part1('shiny gold', bag_graph))
    print(part2('shiny gold', bag_graph))
