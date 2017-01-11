from data import Todo


class TodoDB:
    __todos = []
    __last = 0

    def getTodo(self, tid):
        for todo in self.__todos:
            if todo.tid is tid:
                return todo
        return None

    def getTodos(self):
        return self.__todos

    def addTodo(self, name, description):
        todo = Todo(self.__last + 1, name, description)
        self.__todos.append(todo)
        self.__last += 1
        return todo

    def deleteTodo(self, tid):
        self.__todos.remove(self.getTodo(tid))

    def editTodo(self, tid, name, description):
        self.deleteTodo(tid)
        self.__todos.append(Todo(tid, name, description))
        return self.getTodo(tid)
