from time import sleep
# from colorama import Fore, Back, Style
import os

def line_generator(size=os.get_terminal_size().columns):
    for count in range(0, size // 5 ):
       print('-', end='-', flush=True) 
       sleep(0.01)
    
    print('-')
    return ''

def format_account_dict(dict):
    first_name = dict['first_name']
    last_name = dict['last_name']
    email = dict['email']
    balance = dict['balance']
    print(f'Name: {first_name} {last_name}\nEmail: {email}\nBalance: ${balance}', end='\n\n')