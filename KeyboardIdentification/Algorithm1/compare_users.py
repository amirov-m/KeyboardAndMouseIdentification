from read_users import read_user
from core import users_likelihood
import sys



def main():
	first_user = read_user(sys.argv[1])
	second_user = read_user(sys.argv[2])

	likelihood = users_likelihood(first_user, second_user)
	print("users likelihood: " + str(likelihood))

	print()
	print(" INFO : MAX: 0.0. More likelihood - bigger result.")



if __name__ == "__main__":
	main()