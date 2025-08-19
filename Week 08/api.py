import requests,pyfiglet, termcolor
url = "https://fakestoreapi.com/products"
def ShowData():
    AllPrice = []
    Response = requests.get(url)
    if Response.status_code == 200:
        print("Loading ... please Wait")
        data = Response.json()
        for Product in data:
            print(f'------ {Product["title"]}')
            print(f'--- {Product["price"]}$')
            AllPrice.append(Product["price"])
        print(termcolor.colored(pyfiglet.figlet_format(f"{sum(AllPrice)}$"), "blue"))
ShowData()