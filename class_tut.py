class Teachers:
    def __init__(self,name,lesson):
        self.name=name
        self.lesson=lesson
    def great(self):
        print(f"hi it's your tr {self.name} and I teach {self.lesson}")


class Students(Teachers):
    pass
paul=Students("paul","Javascript")
paul.great()