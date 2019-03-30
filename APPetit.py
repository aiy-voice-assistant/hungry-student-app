import supercook as sc
import translate as ts


IT_TO_EN = "it-en"
EN_TO_IT = "en-it"


def main():
    ingredients = ["uova", "burro"]

    ingredients = ts.translator(ingredients, IT_TO_EN)
    recipes = sc.get_recipes(ingredients)

    return


if __name__ == '__main__':
    main()
