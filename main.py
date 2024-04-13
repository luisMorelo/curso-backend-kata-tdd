import unittest


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 4), 5)


if __name__ == '__main__':
    unittest.main()


class Greeter:
    def __init__(self):
        pass
    
    def greet(self, name):
        import datetime
        now = datetime.datetime.now()
        formatted_name = name.strip().capitalize()
        greeting = ""
        
        if 6 <= now.hour < 12:
            greeting = "Good morning"
        elif 18 <= now.hour < 22:
            greeting = "Good evening"
        else:
            greeting = "Good night"
        
        message = f"{greeting} {formatted_name}"
        print(message)
        return message



saludar = Greeter()
saludar.greet('Luis')