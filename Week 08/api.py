import requests,pyfiglet, termcolor
Products = "https://fakestoreapi.com/products"
R_Meal_Api = "https://www.themealdb.com/api/json/v1/1/random.php"
def ShowData():
    AllPrice = []
    Response = requests.get(Products)
    if Response.status_code == 200:
        print("Loading ... please Wait")
        data = Response.json()
        for Product in data:
            print(f'------ {Product["title"]}')
            print(f'--- {Product["price"]}$')
            AllPrice.append(Product["price"])
        print(termcolor.colored(pyfiglet.figlet_format(f"{sum(AllPrice)}$"), "blue"))
ShowData()



colors = [color for color in termcolor.COLORS]
def GetRandomMeal():
    response = requests.get(R_Meal_Api)
    if response.status_code == 200:
        data = response.json()
        listMeal = data["meals"]
        print("MEAL INFO :")
        for meal in listMeal:
            print(meal["idMeal"])
            print(meal["strMeal"])
            print(meal["strCategory"])
            print(meal["strArea"])
            print(meal["strMealThumb"])
            ingredients = [meal[k] for k in meal if k.startswith("strIngredient") and meal[k]]
            print("Ingredient")
            for index , value in enumerate(ingredients):
                print(f"{index + 1} - {termcolor.colored(value, colors[index])}")
    else :
        print(response.json())
GetRandomMeal()


