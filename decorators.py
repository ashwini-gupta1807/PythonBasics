# decorators - takes the function as a argument and modify the existing function acc to the needs and return the modify function

def greet(func):
    def modified():
        print("Hello")
        func()
        print("Modified function runs")
    return modified

@greet
def demo():
    print("Hi")

demo()