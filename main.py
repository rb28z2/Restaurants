from restaurant import Restaurant


# Empty object class to hold temporary values
class Object(object):
    pass


def main():
    print("Welcome to Restaurant Chooser")
    numRestaurants = int(input('Enter the number of restaurants to choose from: '))

    restaurants = []

    for num in range(0, numRestaurants):
        name = input("\nPlease enter the name of the restaurant: ")
        rating = getValidInt("Please enter a rating for " + name + " between 1 and 5 inclusive: ", True)
        veg = getValidInt("# of vegetarian meals " + name + " can provide: ", False)
        gf = getValidInt("# of gluten-free meals " + name + " can provide: ", False)
        nf = getValidInt("# of nut-free meals " + name + " can provide: ", False)
        ff = getValidInt("# of fish-free meals " + name + " can provide: ", False)
        reg = getValidInt("# of total meals " + name + " can provide: ", False)

        reg = reg - veg - gf - nf - ff  # regular meals = total meals - special meals
        restaurants.append(Restaurant(name, rating, veg, gf, nf, ff, reg))

    requiredMeals = getValidInt("\nEnter number of total meals required for your team: ", False)

    requiredInfo = Object()
    requiredInfo.vegetarian = getValidInt("Enter number of vegetarian meals your team requires: ", False)
    requiredInfo.glutenFree = getValidInt("Enter number of gluten-free meals your team requires: ", False)
    requiredInfo.nutFree = getValidInt("Enter number of nut-free meals your team requires: ", False)
    requiredInfo.fishFree = getValidInt("Enter number of fish-free meals your team requires: ", False)

    # sort the restaurants array by highest rated first. makes processing much faster/easier
    restaurants = sorted(restaurants, key=lambda restaurant: restaurant.rating, reverse=True)

    order = calculateRestaurants(requiredMeals, requiredInfo, restaurants)

    printOrder(order)


def calculateRestaurants(requiredMeals, requiredInfo, restaurants):
    order = []
    for i in range(0, len(restaurants)):
        if requiredMeals > 0:  # only process until all required meals are ordered
            tempRestaurant = Object()  # empty object
            for type in ['vegetarian', 'glutenFree', 'nutFree',
                         'fishFree']:  # iterate through the types of required food
                retVal, tempRequired, requiredMeals = calculator(getattr(requiredInfo, type), type, requiredMeals,
                                                                 restaurants[i])
                setattr(tempRestaurant, type, retVal)  # set the temp restaurant's values ie: number of type of meal
                setattr(requiredInfo, type, tempRequired)  # update the required number of meals

            if requiredMeals != 0:  # once all special meals are satisfied, calculate number of regular meals required
                # follows same algorithm as in calculator function
                regular = restaurants[i].regular
                requiredMeals -= regular
                if requiredMeals < 0:
                    regular += requiredMeals
                    requiredMeals = 0
            else:
                regular = 0
        order.append(Restaurant(restaurants[i].name, 0, vegetarian=tempRestaurant.vegetarian,
                                glutenFree=tempRestaurant.glutenFree,
                                nutFree=tempRestaurant.nutFree, fishFree=tempRestaurant.fishFree, regular=regular))
    return order


def getValidInt(prompt, rating):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, please enter a valid integer")
            continue

        if rating:
            if (value < 1) or (value > 5):
                print("Sorry, please enter a rating between 1 and 5 inclusive")
                continue
            else:
                break
        else:
            if value < 0:
                print("Sorry, please enter a positive integer")
                continue
            else:
                break
    return value


# takes as input the number of a certain type of meal required, what meal it is, total meals required, and a
# restaurant object.
# Returns: number of meals of a certain type to order from that restaurant, plus some updated required meals values
def calculator(required, type, mealsRequired, restaurant):
    # check that a certain type of meal is required, otherwise return 0
    # variable 'out' is the number of a type of meal from a certain restaurant that needs to be ordered
    if required != 0:
        out = getattr(restaurant, type)  # temporarily set the number to order to the maximum the restaurant can provide
        required -= out  # decrement the required amount of that type of meal by the number added to order
        if required < 0:  # if we order more than the restaurant can provide
            out += required  # set the number to order to the maximum the restaurant can provide
            mealsRequired -= out  # correct the number of total meals required
            required = 0  # in this scenario, we have fulfilled all the meals (of a certain type) required
        else:
            mealsRequired -= out  # if we don't order more than the restaurant can provide, update total meals required
    else:
        out = 0  # no meals of this type required
    return out, required, mealsRequired


def printOrder(order):
    print("\nExpected meal orders:")
    out = ""
    for restaurant in order:
        out = (restaurant.name + ": " + str(restaurant.vegetarian) + " Vegetarian + " + str(
            restaurant.glutenFree) + " Gluten Free + "
               + str(restaurant.nutFree) + " Nut-Free + " + str(restaurant.fishFree) + " Fish-Free + " + str(
                    restaurant.regular) + " others")
        print(out)
    return out

if __name__ == '__main__':
    main()
