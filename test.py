
def print_dictionary(current_ratings):
	current_ratings = sorted(current_ratings.items())
	for restaurant, rating in current_ratings:
		print(restaurant + " is rated at a " + rating + ".")


def clean_ratings(filename):
	my_file = open(filename)
	ratings = {}
	for line in my_file:
		line = line.strip()
		restaurant, rating = line.split(":")
		ratings[restaurant] = rating

	return dict(ratings)



def write_to_file(original_ratings):
	with open("scores.txt", "w") as data:
		for k, v in original_ratings.items():
			data.write(str(k) + ':' +str(v) +'\n')
	data.close()


def get_new_rating(original_ratings):
	new_restaurant = (input("What would you like to enter? ")).capitalize()
	new_score = (input("What would you score it as? "))

	valid_scores = ["1", "2", "3", "4", "5"]

	if new_score in valid_scores:

		original_ratings[new_restaurant] = new_score
		write_to_file(original_ratings)
		
	else:
		print("Please enter a valid rating. ")
		get_new_rating(ratings)



def restaurant_ratings(filename):
	ratings = clean_ratings(filename)
	while True:

		user_input = input("What would you like to do? (S)ee all ratings, (A)dd new restaurant, or (Q)uit. ")

		if user_input.upper() == "S":
			print_dictionary(ratings)
		elif user_input.upper() == "A":
			get_new_rating(ratings)
		elif user_input.upper()== "Q":
			print("Goodbye!")
			break
		else:
			print("Please enter a valid command")


restaurant_ratings("scores.txt")