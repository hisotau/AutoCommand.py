import time
from itertools import cycle
import keyboard
import mouse

nachalo = int(input("Введите слот 1 супа: "))
digit_generator = cycle(map(str, range(nachalo, 10)))


def on_key_event(e, command_key):
    global digit_generator
    if e.event_type == keyboard.KEY_DOWN and e.name == command_key:
        current_digit = next(digit_generator, None)
        if current_digit is not None:
            keyboard.press(current_digit)
            mouse.click('right')
            time.sleep(0.05)
            keyboard.release(current_digit)
            keyboard.press_and_release("1")


def main():
    command_key = input("Введите клавишу для начала работы: ")
    exit_key = input("Введите клавишу для выхода с программы: ")
    keyboard.hook(lambda e: on_key_event(e, command_key))
    print(f"Нажмите {exit_key} чтобы выйти.")
    keyboard.wait(exit_key)


main()

# def on_key_event(e, command_key, digit_generator, nachalo):
# global digit_generator

#   if e.event_type == keyboard.KEY_DOWN and e.name == command_key:
#      current_digit = next(digit_generator, None)
#     if current_digit is not None:
#        keyboard.press(current_digit)
#       mouse.click('right')
#      time.sleep(0.1)
#     keyboard.release(current_digit)
# else:
#     # Если цифры закончились, создаем новый генератор
#   digit_generator = (str(i) for i in range(nachalo, 10))


# def on_key_event(e, command_key):
#   if e.name == command_key:
#  keyboard.press_and_release(chat_key)
#      click = 1
#     keyboard.press_and_release('2')
#    mouse.click('right')
#   time.sleep(0.1)
#  keyboard.press_and_release('1')


# def change_key():
#   command_key = input("Введите клавишу для ввода команды: ")
# chat_key = input("Введите клавишу на которой у вас стоит чат: ")
#  exit_key = input("Введите клавишу для выхода с программы: ")
# keyboard.hook(lambda e: on_key_event(e, command_key))
# print(f"Нажмите {exit_key} чтобы выйти.")
# keyboard.wait(exit_key)


# def main():
#   command_key = input("Введите клавишу для ввода команды: ")
#  # chat_key = input("Введите клавишу на которой у вас стоит чат: ")
# nachalo = int(input("Введите слот 1 супа: "))
# exit_key = input("Введите клавишу для выхода с программы: ")
# digit_generator = (str(i) for i in range(nachalo, 10))
# keyboard.hook(lambda e: on_key_event(e, command_key, digit_generator, nachalo))
# print(f"Нажмите {exit_key} чтобы выйти.")
# keyboard.wait(exit_key)


# main()
