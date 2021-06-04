import requests
# The getpass module allows your password not to be echoed in the terminal.
# Just like after you have run sudo apt install. It does not work with most
# IDE's terminals. You need to use the linux terminal for this to work.
import getpass


r = requests.get('https://api.github.com/user', auth=(input("username:"), getpass.getpass("Password:")))

print(r.status_code)