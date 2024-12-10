# HanoiGame.py
from StackHanoi import Stack
import logging

# 2. Crear las pilas
print("\n¡Vamos a jugar a las torres de Hanoi!")

stacks = []  # Lista para almacenar las pilas
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# 3. Añadir pilas a la lista
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# 4. Configuración del juego
num_disks = int(input("¿Con cuántos discos quieres jugar?: "))
while num_disks < 3:
    num_disks = int(input("Ingresa un número mayor o igual a 3: "))

# 7. Agregar discos a la pila izquierda
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# 9. Calcular movimientos óptimos
num_optimal_moves = 2 ** num_disks - 1
print(f"\nLo más rápido que puedes resolver este juego es en {num_optimal_moves} movimientos.")

# 13. Obtener entrada del usuario
def get_input():
    choices = ['L', 'M', 'R']  # Opciones para las pilas
    while True:
        # 16. Imprimir opciones
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Escribe {letter} para {name}")

        # 21. Obtener entrada del usuario
        user_input = input("Tu elección: ").upper()

        # 23. Verificar entrada válida
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# 28. Jugando el juego
num_user_moves = 0

# 30. Bucle principal del juego
while right_stack.get_size() != num_disks:
    print("\n\n...Pilas actuales...")
    for stack in stacks:
        stack.print_items()

    # 32. Solicitar movimiento
    while True:
        print("\n¿Desde qué pila quieres mover un disco?\n")
        from_stack = get_input()
        print("\n¿A qué pila quieres mover el disco?\n")
        to_stack = get_input()

        # 34. Comprobar movimiento válido
        if from_stack.is_empty():
            print("\n\nMovimiento no válido. Inténtalo de nuevo.")
        elif (to_stack.is_empty() or from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break  # Movimiento válido, salir del bucle
        else:
            print("\n\nMovimiento no válido. Inténtalo de nuevo.")

# 37. Fin del juego
print(f"\n\nCompletaste el juego en {num_user_moves} movimientos y el número óptimo de movimientos es {num_optimal_moves}.")