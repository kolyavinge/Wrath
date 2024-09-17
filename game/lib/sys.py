from termcolor import colored


def warn(message):
    print(colored("Warning: " + message, "yellow"))
