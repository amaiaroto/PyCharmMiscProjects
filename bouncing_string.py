import time

userinput = input("Bouncer,Delay: ")
string: str = userinput.split(",")[0]
row: int = 0
padding: int = 9
rows: int = len(string) + padding
delay: float = 0.500

while True:
    for _ in range(rows):
        print((" " * row) + string + (" " * abs(rows - row)), end="\r")

        time.sleep(delay)

        row += 1

    for _ in range(rows):
        print((" " * row) + string + (" " * abs(rows - row)), end="\r")

        time.sleep(delay)

        row -= 1
