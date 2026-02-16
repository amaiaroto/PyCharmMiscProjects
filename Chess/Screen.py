# import random, time, sys, runpy
import runpy


class Screen:
    def __init__(self, pygame_object, screen_width: int, screen_height: int, options: list = None):
        self.width = screen_width
        self.height = screen_height
        self.options = options
        self.pg = pygame_object

    def screen(self):
        return self.pg.display.set_mode((self.width, self.height), *self.options if self.options else [self.pg.SCALED])


# if __name__ == '__main__':
#     print('> Enter password for access.\n')
#     entered_password = input('>>')
#     if entered_password != '//run':
#         print('Incorrect Password: punishing failure...')
#         time.sleep(1)
#         while True:
#             print(random.uniform(-1000**10, 10000**10))
#
#     elif not entered_password:
#         text_pos = open('Screen.py', 'r').read()
#         print(text_pos)
#         time.sleep(1e-2)
#         exit('Success: Access granted')
#         exit('Failure: Access illegal') # If first exit failed then try again.
#         sys.exit() # If all goes wrong...
#
#     else:
#         print('Running main...')
#         time.sleep(random.uniform(0.1, 3))
#         runpy.run_path('.\\main.py')
if __name__ == '__main__':
    runpy.run_path('.\\main.py')
