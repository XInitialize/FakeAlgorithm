class SingleNode:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        while self.head != None:
            print(self.head.data, "->")
            self.head = self.head.next
        print(self.head)


class SingleCircularList:
    def __init__(self, raw_list: list) -> None:
        self.length = len(raw_list)
        self.raw_list = raw_list
        self.head = self.gen_nodes_from_raw()

    def gen_nodes_from_raw(self):
        nodes = []
        for item in self.raw_list:
            nodes.append(SingleNode(data=item))
        for i in range(self.length - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = nodes[0]
        return nodes[0]

    def add_next_node(self, node: SingleNode):
        node.next = self.head.next
        self.length += 1
        self.head.next = node

    def print_list(self):
        i = 0
        while self.head != None and i < self.length:
            print(self.head.data, "->")
            self.head = self.head.next
            i += 1
        print(self.head.data)

    def forward(self):
        self.head = self.head.next

    def provide_data(self):
        data = self.head.data
        self.forward()
        return data
