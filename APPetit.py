import supercook as sc
import translate as ts


IT_TO_EN = "it-en"
EN_TO_IT = "en-it"


def main():
    ingredients = ["uova", "suefhienuwehfi"]

    ingredients = ts.translator(ingredients, IT_TO_EN)
    recipes, needs = sc.get_recipes(ingredients)

    print(recipes)
    print(needs)

    return


if __name__ == '__main__':
    main()
