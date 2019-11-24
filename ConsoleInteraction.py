def ask_guess(message):
    while True:
        command = input(message).upper()
        if len(command) == 1 and command in "ABCDEFGHIJKLMNOPQRSTUVWXYZ/":
            return command
        print("I'm expecting a single letter or a /... -> ", end='')
