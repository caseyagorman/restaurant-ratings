def rating(filename):
	my_file = open(filename)
	ratings = {}
	for line in my_file:
		line = line.strip()
		restaurant, rating = line.split(":")
		ratings[restaurant] = rating
	ratings = sorted(ratings.items())
	for restaurant, rating in ratings:
		print(restaurant + " is rated at a " + rating + ".")

	return dict(ratings)


def get_new_rating(original_ratings):
	new_restaurant = input("What would you like to enter? ")
	new_score = input("What would you score it as? ")

	original_ratings[new_restaurant] = new_score

	original_ratings = sorted(original_ratings.items())
	for restaurant, rating in original_ratings:
		print(restaurant + " is rated at a " + rating + ".")
	

ratings = rating("scores.txt")
get_new_rating(ratings)