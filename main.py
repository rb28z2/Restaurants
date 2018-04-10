from restaurant import Restaurant


# Empty object class to hold temporary values
class Object(object):
    pass


def main():
    restaurants = []
    requiredMeals = 50

    requiredInfo = Object()
    requiredInfo.vegetarian = 5
    requiredInfo.glutenFree = 7
    requiredInfo.nutFree = 0
    requiredInfo.fishFree = 0

    restaurants.append(Restaurant("A", 0.6, 20, 20, 0, 0, 60))
    restaurants.append(Restaurant("B", 1, 4, 0, 0, 0, 36))

    # sort the restaurants array by highest rated first. makes processing much faster/easier
    restaurants = sorted(restaurants, key=lambda restaurant: restaurant.rating, reverse=True)

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

    print(order)


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
            mealsRequired -= out  # if we dont order more than the restaurant can provide, update total meals required
    else:
        out = 0  # no meals of this type required
    return out, required, mealsRequired


if __name__ == '__main__':
    main()
