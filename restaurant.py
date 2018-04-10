class Restaurant:
    'Base class for all restaurants'

    # rating = 0
    # vegetarian = 0
    # glutenFree = 0
    # nutFree = 0
    # fishFree = 0

    def __init__(self, name, rating, vegetarian, glutenFree, nutFree, fishFree, regular):
        self.name = name
        self.rating = rating
        self.vegetarian = vegetarian
        self.glutenFree = glutenFree
        self.nutFree = nutFree
        self.fishFree = fishFree
        self.regular = regular

    def __repr__(self):
        return repr(
            (self.name, self.rating, self.vegetarian, self.glutenFree, self.nutFree, self.fishFree, self.regular))

    def __cmp__(self, other):
        if hasattr(other, 'rating'):
            return self.rating.__cmp__(other.rating)
