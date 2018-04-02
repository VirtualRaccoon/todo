import json


class Todo:

    def __init__(self, path):
        self.path = path
        self.tasks = []

        try:
            with open(path, 'r') as data_file:
                self.tasks = json.load(data_file)
        except FileNotFoundError:
            pass

    def list(self):
        return self.tasks

    def create(self, task):
        self.tasks.append(task)

    def delete(self, id):
        try:
            del self.tasks[id]
        except IndexError:
            raise

    def save(self):
        with open(self.path, 'w') as data_file:
            json.dump(self.tasks, data_file)
