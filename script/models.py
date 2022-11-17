import time


class Process():
    name: str
    arrival_time: float
    gust: float
    start_time: float
    final_time: float
    returning_time: float
    waiting_time: float

    def __init__(self, name, arrival_time, gust):
        self.name = name
        self.arrival_time = arrival_time
        self.gust = gust
        self.start_time = 0
        self.final_time = 0
        self.returning_time = 0
        self.waiting_time = 0

    def __str__(self):
        return """
{}
- Arraival Time: {}
- Gust: {}
- Start Time: {}
- Final Time: {}
- Returning Time: {}
- Waiting Time: {}
        """.format(self.name, self.arrival_time, self.gust, self.start_time, self.final_time, self.returning_time, self.waiting_time)

    def execute(self, app_time):
        print("Execute process {}".format(self.name))
        self.start_time = round(time.time() - app_time)
        self.final_time = self.start_time + self.gust
        self.returning_time = self.final_time - self.arrival_time
        self.waiting_time = self.returning_time - self.gust
        time.sleep(self.gust)


class List:
    name: str
    app_time: float
    ls: list

    def __init__(self, app_time):
        self.ls = []
        self.app_time = app_time

    def add_process(self, process):
        self.ls.append(process)

    def process_node(self, historical_list):
        self.ls[0].execute(self.app_time)
        historical_list.add_process(self.ls[0])
        self.ls.pop(0)

    def print_list(self):
        print()
        print(f"printing a list of processes {self.__str__()}")
        for node in self.ls:
            print(node)

    def execute(self, historical_list):
        while len(self.ls) > 0:
            self.process_node(historical_list)

    def __str__(self) -> str:
        return self.name
