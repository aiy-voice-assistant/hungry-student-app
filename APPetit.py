import supercook as sc
import retriveRecipes as pc  
import food_delivery as fd


def main():
    recipes, needs, urls = sc.getRecipeName(["milk", "parmesan"])
    steps, prep_time, calories = pc.getRecipe(recipes[0])    
    
    print(recipes[0])
    for s in steps:
        print(s)

    order = "pasta"
    name, price = fd.order_food(order)

    if price != -1:
        print("Best price is " + str(price) + "€ at " + name)
    else:
        print("I did not find anything")
    
    return


if __name__ == '__main__':
    main()
