from termcolor import colored


def warn(message):
    print(colored(f"Warning: {message}", "yellow"))
