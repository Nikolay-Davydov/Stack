
final = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_balance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in final:
            stack.push(item_)
        elif item_ == final.get(stack.peek()):
            stack.pop()
        else:
            return "Несбалансировано"
    return "Сбалансировано"








