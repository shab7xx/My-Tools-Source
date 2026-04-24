import os
import sys
from colorama import init, Fore

init(autoreset=True)

class Toolkit:
    def __init__(self):
        self.clear_screen()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_banner(self):
        banner = f"""{Fore.RED}
  _________.__          _______________________  ___        
 /   _____/|  |__ _____ \______   \______  \   \/  /___  ___
 \_____  \ |  |  \\__  \ |    |  _/   /    /\     / \  \/  /
 /        \|   Y  \/ __ \|    |   \  /    / /     \  >    < 
/_______  /|___|  (____  /______  / /____/ /___/\  \/__/\_ \\
        \/      \/     \/       \/               \_/      \/    
                    {Fore.MAGENTA}Developed by: ShaB7Xx{Fore.RESET}
"""
        print(banner)
    
    def display_main_menu(self):
        print(f"{Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] > Option 1")
        print(f"{Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] > Option 2")
        print(f"{Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] > Option 3")
        print(f"{Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] > Exit")
        print(f"\n{Fore.RED}[>]{Fore.WHITE} Choose : ", end="")
    
    def option1(self):
        print(f"\n{Fore.GREEN}[+] Option 1 Selected")
        print(f"{Fore.YELLOW}[!] This is a placeholder for your functionality")
    
    def option2(self):
        print(f"\n{Fore.GREEN}[+] Option 2 Selected")
        print(f"{Fore.YELLOW}[!] This is a placeholder for your functionality")
    
    def option3(self):
        print(f"\n{Fore.GREEN}[+] Option 3 Selected")
        print(f"{Fore.YELLOW}[!] This is a placeholder for your functionality")
    
    def run(self):
        try:
            while True:
                self.clear_screen()
                self.display_banner()
                self.display_main_menu()
                
                choice = input().strip()
                
                if choice == "1":
                    self.option1()
                    input(f"\n{Fore.YELLOW}Press Enter to continue...")
                
                elif choice == "2":
                    self.option2()
                    input(f"\n{Fore.YELLOW}Press Enter to continue...")
                
                elif choice == "3":
                    self.option3()
                    input(f"\n{Fore.YELLOW}Press Enter to continue...")
                
                elif choice == "4":
                    print(f"\n{Fore.RED}[!] Exiting...")
                    sys.exit(0)
                
                else:
                    print(f"{Fore.RED}[!] Invalid choice")
                    input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Program terminated by user")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    toolkit = Toolkit()
    toolkit.run()
