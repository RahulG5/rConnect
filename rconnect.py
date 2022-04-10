from pyfiglet import figlet_format
from sys import exit
from getpass import getpass

vars = {
    exit : { 'SAFE':1, 'ABORT':0, },
}

def argument_missing(**kwargs):

    func_name = kwargs.get('FUNCTION')
    argument  = kwargs.get('ARGUMENT')
    display(INFO=f"{func_name} : Function called without argument {argument}, please check")
    exit(vars['EXIT']['ABORT'])

def client_display_intro():

    ascii_banner = figlet_format(f"Welcome to rConnect")
    display(INFO=ascii_banner, LOGIT=False)
    return

def client_take_input():

    host     = input(f"Please provide the remote device you wish to rConnect         : HOST : ")
    user     = input(f"Please provide the user type of the rConnected device         : USER : ")
    password = getpass(f"Please provide the password (if any) to the rConnected device : PSWD : ")
    return

def display(**kwargs):

    info  = kwargs.get('INFO')
    logit = kwargs.get('LOGIT',True)
    if (info is None): argument_missing(FUNCTION="display", ARGUMENT="info") 
    print(info)
    return