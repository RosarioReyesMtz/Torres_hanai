# hanoi_gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from StackHanoi import Stack
from Node import Node

class HanoiGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi")

        self.stacks = [Stack("Left"), Stack("Middle"), Stack("Right")]
        self.num_disks = 3
        self.num_user_moves = 0
        self.disk_labels = []  # Para almacenar las etiquetas de los discos

        self.create_widgets()
        self.setup_game()

    def create_widgets(self):
        self.left_frame = tk.Frame(self.master)
        self.middle_frame = tk.Frame(self.master)
        self.right_frame = tk.Frame(self.master)

        self.left_frame.pack(side=tk.LEFT)
        self.middle_frame.pack(side=tk.LEFT)
        self.right_frame.pack(side=tk.LEFT)

        self.left_label = tk.Label(self.left_frame, text="Izquierda")
        self.middle_label = tk.Label(self.middle_frame, text="Medio")
        self.right_label = tk.Label(self.right_frame, text="Derecha")

        self.left_label.pack()
        self.middle_label.pack()
        self.right_label.pack()

        self.left_stack_display = tk.Canvas(self.left_frame, width=100, height=300, bg="white")
        self.middle_stack_display = tk.Canvas(self.middle_frame, width=100, height=300, bg="white")
        self.right_stack_display = tk.Canvas(self.right_frame, width=100, height=300, bg="white")

        self.left_stack_display.pack()
        self.middle_stack_display.pack()
        self.right_stack_display.pack()

        self.move_button = tk.Button(self.master, text="Mover Disco", command=self.move_disk)
        self.move_button.pack()

        self.from_stack_var = tk.StringVar(value="Left")
        self.to_stack_var = tk.StringVar(value="Middle")

        self.from_stack_menu = tk.OptionMenu(self.master, self.from_stack_var, "Left", "Middle", "Right")
        self.to_stack_menu = tk.OptionMenu(self.master, self.to_stack_var, "Left", "Middle", "Right")

        self.from_stack_menu.pack()
        self.to_stack_menu.pack()

    def setup_game(self):
        self.num_disks = simpledialog.askinteger("Número de Discos", "¿Con cuántos discos quieres jugar?", minvalue=3)
        for disk in range(self.num_disks, 0, -1):
            self.stacks[0].push(disk)

        self.update_displays()

    def update_displays(self):
        for canvas in [self.left_stack_display, self.middle_stack_display, self.right_stack_display]:
            canvas.delete("all")  # Limpia el canvas antes de dibujar

        for stack in self.stacks:
            for index, disk in enumerate(stack.show()):
                width = disk * 20  # Ancho del disco
                x0 = 50 - width // 2  # Posición x inicial
                y0 = 300 - (index + 1) * 20  # Posición y inicial
                x1 = 50 + width // 2  # Posición x final
                y1 = 300 - index * 20  # Posición y final
                canvas = {
                    "Left": self.left_stack_display,
                    "Middle": self.middle_stack_display,
                    "Right": self.right_stack_display
                }[stack.get_name()]
                canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black")

    def move_disk(self):
        from_stack_name = self.from_stack_var.get()
        to_stack_name = self.to_stack_var.get()

        from_stack = next(stack for stack in self.stacks if stack.get_name() == from_stack_name)
        to_stack = next(stack for stack in self.stacks if stack.get_name() == to_stack_name)

        if from_stack.is_empty():
            messagebox.showwarning("Movimiento no válido", "No hay discos en la pila de origen.")
            return

        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            self.num_user_moves += 1
            self.update_displays()

            if self.stacks[2].get_size() == self.num_disks:
                messagebox.showinfo("Juego Terminado", f"Completaste el juego en {self.num_user_moves} movimientos.")
        else:
            messagebox.showwarning("Movimiento no válido", "No puedes mover un disco más grande sobre uno más pequeño.")

if __name__ == "__main__":
    root = tk.Tk()
    game = HanoiGame(root)
    root.mainloop()