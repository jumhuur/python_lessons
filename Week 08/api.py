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
# ShowData()



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
# GetRandomMeal()


def Api_Test():
    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
    querystring = {"name":"landon","locale":"en-gb"}
    headers = {
        "x-rapidapi-key": "5de993e486mshc54b203ad97c00bp162403jsnbdcf2950d435",
        "x-rapidapi-host": "booking-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    if response.status_code ==  200:
        Hotels = response.json()
        for Hotel in Hotels:
            print(Hotel.get("name"))
            print(Hotel.get("image_url"))
    print(response.status_code)
# Api_Test()

ll = [{"name":"bob"},{"name": "poot"}]
print(ll.index({"name":"bob"}))
print(ll)
# print(dir(list))




