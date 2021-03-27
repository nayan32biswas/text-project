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
        pass

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


class SolutionTwo:
    data = {
        "key1": 1,
        "”key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    results = []

    def __init__(self, data=None) -> None:
        if data:
            self.data = data
        pass

    def get_results(self):
        return []

    def start(self):
        self.results = []


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