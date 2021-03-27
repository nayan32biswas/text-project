print("One")


class SolutionOne:
    data = {
        "key1": 1,
        "”key2": {
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
    def results(self):
        return []

class SolutionTwo:
    def results(self):
        return []

class SolutionThree:
    def results(self):
        return []
