import termcolor , pyfiglet

# print(dir(termcolor))
# print(pyfiglet.figlet_format("Jumhuur"))

print(termcolor.colored(pyfiglet.figlet_format("Jumhuur"), "blue"))
# print(dir(termcolor))
# print(termcolor.COLORS)

import  requests
url = "https://fakestoreapi.com/prodzucts"

response = requests.get(url)
print(response.status_code)
print(response.json())
print(response)
# print(dir(requests))