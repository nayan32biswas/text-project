class SolutionOne:
    data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }

    def __init__(self, data=None) -> None:
        if data:
            self.data = data

    def depth_in_dict(self, obj, depth) -> None:
        if type(obj) != dict:
            return
        for key, value in obj.items():
            self.results.append(f"{key} {depth}")
            if type(value) == dict:
                self.depth_in_dict(value, depth+1)

    def get_results(self):
        self.results = []
        self.depth_in_dict(self.data, 1)
        return self.results 

    def print_depth(self, data=None):
        if data:
            self.data = data
        self.get_results()
        for value in self.results:
            print(value)

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

class SolutionTwo:
    data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": Person("two-first", "two-last", Person("one-first", "one-last", None))
            }
        }
    }

    def __init__(self, data=None) -> None:
        if data:
            self.data = data

    def depth_in_dict(self, obj, depth) -> None:
        if type(obj) != dict:
            return
        for key, value in obj.items():
            self.results.append(f"{key} {depth}")
            if type(value) == dict:
                self.depth_in_dict(value, depth+1)
            elif type(value) == Person:
                self.depth_in_dict(value.__dict__, depth+1)

    def get_results(self):
        self.results = []
        self.depth_in_dict(self.data, 1)
        return self.results 

    def print_depth(self, data=None):
        if data:
            self.data = data
        self.get_results()
        for value in self.results:
            print(value)

class Node:
    def __init__(self, value, parent) -> None:
        self.value = value
        self.parent = parent

class SolutionThree:
    def __init__(self) -> None:
        self.create_tree()

    def create_tree(self):
        self.nodes = [0, Node(1, None)]
        self.nodes = self.nodes + [Node(2, self.nodes[1]), Node(3, self.nodes[1])]
        self.nodes = self.nodes + [Node(4, self.nodes[2]), Node(5, self.nodes[2])]
        self.nodes = self.nodes + [Node(6, self.nodes[3]), Node(7, self.nodes[3])]
        self.nodes = self.nodes + [Node(8, self.nodes[4]), Node(9, self.nodes[4])]

    def mark_node(self, node):
        self.mark[node] = 1
        if(node.parent):
            self.mark_node(node.parent)

    def get_anc(self, node):
        if node in self.mark:
            return node
        if(node.parent):
            return self.get_anc(node.parent)

    def lca(self, node1, node2):
        self.mark = {}
        self.mark_node(node1)
        return self.get_anc(node2)

    def start(self):
        self.lca(self.nodes[6], self.nodes[7])


def main():
    runing = 1
    while(runing):
        user_input = input("Type 1 or 2 or 3 to execute solution and 0 to exit: ")
        if '1' in user_input:
            SolutionOne().print_depth()

        elif '2' in user_input:
            SolutionTwo().print_depth()
        elif '3' in user_input:
            SolutionThree().start()
        elif '0' in user_input:
            return 0
        else:
            runing = 0
            user_input = None
            SolutionOne().print_depth()
            SolutionTwo().print_depth()
            SolutionThree().start()

if __name__ == "__main__":
    main()