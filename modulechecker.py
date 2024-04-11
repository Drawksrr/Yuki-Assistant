from colorama import Fore, Back, Style, init
import timermod
import soundmod
import lessons

def checker():
    if timermod.checker and lessons.checker and soundmod.checker:
        print("\n+----------------------------------+\n|          timermod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|          soundmod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|           lessons ",  f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}","        |\n+----------------------------------+\n|             Стан: ", f"{Style.BRIGHT + Fore.GREEN}True{Style.RESET_ALL}", "         |\n+----------------------------------+\n")
    
    elif timermod.checker == False:
        print("\n+----------------------------------+\n|          timermod ", f"{Style.BRIGHT + Fore.RED}Check{Style.RESET_ALL}         |\n|          soundmod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|           lessons ",  f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}","        |\n+----------------------------------+\n|             Стан: ", f"{Style.BRIGHT + Fore.RED}False{Style.RESET_ALL}", "        |\n+----------------------------------+\n")

    elif soundmod.checker == False:
        print("\n+----------------------------------+\n|          timermod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|          soundmod ", f"{Style.BRIGHT + Fore.RED}Check{Style.RESET_ALL}         |\n|           lessons ",  f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}","        |\n+----------------------------------+\n|             Стан: ", f"{Style.BRIGHT + Fore.RED}False{Style.RESET_ALL}", "        |\n+----------------------------------+\n")
    
    elif lessons.checker == False:
        print("\n+----------------------------------+\n|          timermod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|          soundmod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|           lessons ",  f"{Style.BRIGHT + Fore.RED}Check{Style.RESET_ALL}","        |\n+----------------------------------+\n|             Стан: ", f"{Style.BRIGHT + Fore.RED}False{Style.RESET_ALL}", "        |\n+----------------------------------+\n")

    else:
        print("\n+----------------------------------+\n|          timermod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|          soundmod ", f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}         |\n|           lessons ",  f"{Style.BRIGHT + Fore.BLUE}Check{Style.RESET_ALL}","        |\n+----------------------------------+\n|             Стан: ", f"{Style.BRIGHT + Fore.RED}False{Style.RESET_ALL}", "        |\n+----------------------------------+\n")
