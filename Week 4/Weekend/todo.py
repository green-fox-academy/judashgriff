from sys import argv
# from todo_view import View

class Controller(object):
    def __init__(self):
        self.view = View()
        if len(argv) == 1:
            self.print_options()
        else:
            d = Dictionary()
            todo_list = d.make_dictionary()
            self.select_operation(todo_list)
    
            
    def print_options(self):
        self.view.lets_print()
            
    def select_operation(self, todo_list):
        self.modify = Add_and_Remove()
        self.complete = Checker()
        if len(argv) == 2:
            if argv[1] == "-l":
                self.view.list_todo(todo_list)
            else:
                self.print_options()
        elif len(argv) == 3:
            if argv[1] == "-a" or "-r":
                self.modify.operation_selector(argv[1], todo_list)
            elif argv[1] == "-c":
                self.complete.change_check(todo_list) 
            else:
                self.print_options()


class Dictionary(object):
    todo_list = []

    def make_dictionary(self):
        with open('todo.txt', 'r') as text:
            for line in text:
                d = {}
                check = self.get_checks(line)
                d['check'] = check
                d['text'] = line[2:]
                print(d)
                self.todo_list.append(d)
        return self.todo_list

    def get_checks(self, line):
        if line[0] == "1":
            return True
        else:
            return False


class View(object):
    def __init__(self):
        self.d = Dictionary()
    
    command_lines = [
        {'command': "-l", 'text': "Lists all the tasks"},
        {'command': "-a", 'text': "Adds a new task in following method: -a \"your text\""},
        {'command': "-r", 'text': "Removes a task in following method: -r \"task to remove\""},
        {'command': "-c", 'text': "Completes an task in following method: -c \"task to comply\""}]

    def lets_print(self):
        print(str(
        "\nCommand Line Todo application\
        \n=============================\
        \n\nCommand line arguments:\n"))
        for line in self.command_lines:
            print(line['command'], line['text'])

    def list_todo(self, todo_list):
        if todo_list == []:
            print("Nothing to do for today! :)")
        else:
            for i, line in enumerate(todo_list):
                if line['check'] == True:
                    print(str(i + 1) + '- [X]' + line['text'])
                elif line['check'] == False:
                    print(str(i + 1) + '- [ ]' + line['text'])
                

class Add_and_Remove(object):
    view = View()
    d = Dictionary()
        
    def operation_selector(self, operation, todo_list):
        if operation == '-a':
            self.add(todo_list)
        elif operation == '-r':
            self.remove(todo_list)

    def add(self, todo_list):
        d = {}
        d['check'] = False
        d['text'] = argv[2]
        todo_list.append(d)
        self.update(todo_list)

    def remove(self, todo_list):
        new_todo = { k:v for k,v in todo_list.items() if k != argv[2]}
        # for i, line in enumerate(todo_list):
        #     if argv[2] == todo_list[i]['text']:
        #         todo_list -= todo_list[i]
        self.update(new_todo)
        
    def update(self, todo_list):
        with open('todo.txt', 'w') as text:
            for num, line in enumerate(todo_list):
                if line['check'] == False:
                    text.write("0 " + line['text'] + "\n")
                elif line['check'] == True:
                    text.write("1 " + line['text'] + "\n")
        # self.new = self.d.make_dictionary()
        self.view.list_todo(todo_list)


class Checker(object):
    def change_check(self, todo_list):
        d = Dictionary()
        v = View()
        with open('todo.txt', 'w') as text:
            for line in text:
                if argv[2] in line:
                    if line[0] == 0:
                        text[0].write('1')
                    elif line[0] == 1:
                        text[0].write('0')
        todo = self.d.make_dictionary()
        self.v.list_todo(todo)


user = Controller()

