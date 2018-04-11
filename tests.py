import unittest

from main import calculator, calculateRestaurants, Object
from restaurant import Restaurant


class TestCalculator(unittest.TestCase):

    def test_calc(self):
        print("Testing Calculator")
        required = 5
        type = 'vegetarian'
        mealsRequired = 10
        restaurant = Restaurant("TestRestaurant", 5, 6, 0, 0, 0, 30)

        meals, outRequired, outMealsRequired = calculator(required, type, mealsRequired, restaurant)
        self.assertEqual(meals, 5)
        self.assertEqual(outRequired, 0)
        self.assertEqual(outMealsRequired, 5)

    def test_overall(self):
        print("Testing Multiple Restaurants")
        requiredMeals = 50
        requiredInfo = Object()
        requiredInfo.vegetarian = 5
        requiredInfo.glutenFree = 7
        requiredInfo.nutFree = 0
        requiredInfo.fishFree = 0

        restaurants = []
        restaurants.append(Restaurant("A", 5, 4, 0, 0, 0, 36))
        restaurants.append(Restaurant("B", 3, 20, 20, 0, 0, 60))  # sorted by rating

        order = calculateRestaurants(requiredMeals, requiredInfo, restaurants)

        self.assertEqual(order[0].vegetarian, 4)
        self.assertEqual(order[0].glutenFree, 0)
        self.assertEqual(order[0].nutFree, 0)
        self.assertEqual(order[0].fishFree, 0)
        self.assertEqual(order[0].regular, 36)

        self.assertEqual(order[1].vegetarian, 1)
        self.assertEqual(order[1].glutenFree, 7)
        self.assertEqual(order[1].nutFree, 0)
        self.assertEqual(order[1].fishFree, 0)
        self.assertEqual(order[1].regular, 2)


if __name__ == '__main__':
    unittest.main()
