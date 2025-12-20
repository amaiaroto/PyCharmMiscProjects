# # import sys
# #
# # from pynput import keyboard
# #
# # # def on_press(key):
# # #     print(type(key))
# # #
# # # def on_release(key):
# # #     print(key)
# # #
# # #
# # # # Collect events until released
# # # with keyboard.Listener(
# # #         on_press=on_press,
# # #         on_release=on_release) as listener:
# # #     listener.join()
# # #
# # # # ...or, in a non-blocking fashion:
# # # listener = keyboard.Listener(
# # #     on_press=on_press,
# # #     on_release=on_release)
# # # listener.start()
# # from enum import Enum
# #
# # # class syntax
# # class Color(Enum):
# #     RED = 1
# #     GREEN = 2
# #     BLUE = 3
# #
# #
# # print(Color(1))
# #
# # print(keyboard.Key.up.value.vk)
# #
# # print(keyboard.Key(keyboard.KeyCode.from_vk(keyboard.Key.up.value.vk)))
# #
# # l = list()
# #
# # for _ in range(100):
# #     def test_function(v: str | int | float = 'jolt'):
# #         print(v, end='eon\n')
# #     l.append(lambda: test_function('Spik'))
# #
# # for i in l:
# #     i()
# #print(0b110, end=str(0b111))
# import sys
#
# import pygame as pg
# pg.init()
# screen = pg.display.set_mode((800, 600))
# img = pg.image.load('BeeBee.png')
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             sys.exit()
#             pg.quit()
#
#     screen.blit(img)
#     pg.display.update()

price = 67
formatted_price = "{:.2n}".format(price)
print(f"The price is ${formatted_price}") # Output: The price is $6700
