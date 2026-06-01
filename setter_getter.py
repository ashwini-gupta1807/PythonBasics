class C1:
    def __init__(self, name):
        self._name = name

    def info(self):
        print(f"Hello, {self._name}")
    
    @property
    def add_greet(self):
        return f"Hello {self._name}"

    @add_greet.setter
    def add_greet(self, name):
        self._name = name

c1 = C1("Ashwini")
c1.info()
c1.add_greet = "Asha"
c1.info()

    
