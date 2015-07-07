def restaurant_ratings(filename):
    the_file = open(filename)
    ratings = {}
    for line in the_file:
        restaurant_info = line.rstrip().split(":")
        key = restaurant_info[0]
        value = restaurant_info[1]
        ratings[key] = value
    for key, value in sorted(ratings.items()):
        print "%s is rated at %s." % (key, value)

restaurant_ratings("scores.txt")