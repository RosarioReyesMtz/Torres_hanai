# StackHanoi.py
from Node import Node
import logging

class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name
  
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            logging.warning('La pila está llena ¡No queda espacio!')

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        logging.warning('La pila está totalmente vacía!')

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        logging.warning('La pila está totalmente vacía!')

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
  
    def get_size(self):
        return self.size
  
    def get_name(self):
        return self.name
  
    def show(self):
        """Devuelve una representación de los discos en la pila."""
        items = []
        pointer = self.top_item
        while pointer:
            items.append(pointer.get_value())
            pointer = pointer.get_next_node()
        items.reverse()  # Mostrar desde el disco más bajo al más alto
        return items
  
    def print_items(self):
        items = self.show()  # Llama a show para obtener la lista de elementos
        print("{0} Stack: {1}".format(self.get_name(), items))