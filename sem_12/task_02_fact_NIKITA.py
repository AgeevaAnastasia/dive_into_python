import json


class Factorial:
    def __init__(self, k):
        self.k = k
        self.list_dict = []

    def __call__(self, *args, **kwargs):
        num = args[0]
        fac = 1
        for i in range(2, num + 1):
            fac *= i
            self.list_dict.append({num: fac})
        if len(self.list_dict) >= self.k:
            self.list_dict = self.list_dict[-self.k:]
        return fac

    def show(self):
        return self.list_dict

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = 'factorials.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.list_dict, f)


if __name__ == '__main__':
    factorial = Factorial(5)
    with factorial as f:
        for i in range(1, 8):
            factorial(i)
    print(factorial.show())
