from colorama import Fore, init

init(autoreset=True)

def info(msg):
    print(Fore.GREEN + msg)

def section(title):
    print(Fore.CYAN + f"[ {title} ]\n" + f"-" * 20)

def item(msg):
    print(Fore.WHITE + f"{msg}")

def warn(msg):
    print(Fore.YELLOW + msg)