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

    def start(self):
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

    def start(self):
         self.get_results()
         for value in self.results:
             print(value)


class SolutionThree:
    def results(self):
        return []
    def start(self):
        pass


def main():
    runing = 1
    while(runing):
        user_input = input("Type 1 or 2 or 3 to execute solution and 0 to exit: ")
        if '1' in user_input:
            SolutionOne().start()

        elif '2' in user_input:
            SolutionTwo().start()
        elif '3' in user_input:
            SolutionThree().start()
        elif '0' in user_input:
            return 0
        else:
            runing = 0
            user_input = None
            SolutionOne().start()
            SolutionTwo().start()
            SolutionThree().start()

if __name__ == "__main__":
    main()