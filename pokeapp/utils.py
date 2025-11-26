import os

def limpar_console() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')