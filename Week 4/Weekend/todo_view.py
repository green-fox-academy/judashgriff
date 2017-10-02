from todo import Controller

class View(object):
    def __init__(self):
        self.lets_print()

    def lets_print(self):
            print(str("\n\
            Command Line Todo application\n\
            =============================\n\n\
            Command line arguments:\n\
            -l   Lists all the tasks\n\
            -a   Adds a new task in following method: -a \"your text\"\n\
            -r   Removes a task in following method: -r \"task to remove\"\n\
            -c   Completes an task in following method: -c \"task to comply\""))