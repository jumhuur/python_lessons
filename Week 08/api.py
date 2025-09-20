import requests,pyfiglet, termcolor
# url = "https://fakestoreapi.com/products"
# def ShowData():
#     AllPrice = []
#     Response = requests.get(url)
#     if Response.status_code == 200:
#         print("Loading ... please Wait")
#         data = Response.json()
#         for Product in data:
#             print(f'------ {Product["title"]}')
#             print(f'--- {Product["price"]}$')
#             AllPrice.append(Product["price"])
#         print(termcolor.colored(pyfiglet.figlet_format(f"{sum(AllPrice)}$"), "blue"))
# ShowData()
import requests, termcolor
api = "https://www.themealdb.com/api/json/v1/1/random.php"
colors = []
def get_Colors():
    for c_key, c_val in termcolor.COLORS.items():
        colors.append(c_key)
    return colors
def GetRandomMeal():
    response = requests.get(api)
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
            # for m_key, m_val  in meal.items():
            #     Ingredient.append(m_key)
            # all_ing = filter(lambda m_key : m_key.startswith("strIngredient") and meal[m_key],Ingredient)
            ingredients = [meal[k] for k in meal if k.startswith("strIngredient") and meal[k]]
            print("Ingredient")
            for index , value in enumerate(ingredients):
                print(f"{index + 1} - {termcolor.colored(value, get_Colors()[index])}")
    else :
        print(response.json())
GetRandomMeal()


