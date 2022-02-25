# Design an aggregator with two APIs. add(key, value) -> Return None, get_results() -> Return all key value paire.g.
# add(1, 5)
# add(2, 3)
# add(2, 1)

# get_result() -> {1:5, 2:4}

class Aggregator:
    def __init__(self, kv={}) -> None:
        self.kv = kv

    def add(self, key, value) -> None:
        if key in self.kv:
            self.kv[key] += value
        else:
            self.kv[key] = value

    def get_result(self) -> dict:
        return self.kv

a = Aggregator()
a.add(1,1)
a.add(1,2)
a.add(2,1)
a.add(1,3)
a.add(3,5)
a.add(1,4)

result = a.get_result()
print(result)
