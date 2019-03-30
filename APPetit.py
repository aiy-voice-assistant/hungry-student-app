import supercook as sc
import retriveRecipes as pc  
import food_delivery as fd
import habits as h


WANT_TO_ORDER = True


def main():
    if h.check_habits() is True:
        print("You should eat something healthy")
    else:
        print("Tell me what you want to eat")

    if WANT_TO_ORDER is True:
        ingredients = ["milk", "parmesan"]
        recipes, needs, urls = sc.getRecipeName(ingredients)
        steps, prep_time, calories = pc.getRecipe(recipes[0])

        print(recipes[0])
        for s in steps:
            print(s)
    else:
        order = "pasta"
        name, price = fd.order_food(order)

        if price != -1:
            print("Best price is " + str(price) + "€ at " + name)
        else:
            print("I did not find anything")

    return


if __name__ == '__main__':
    main()
