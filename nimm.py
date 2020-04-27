"""
File: nimm.py
-------------------------
Add your comments here.
"""

NUMBER_OF_STARTING_STONES = 20

def main():
    Print("Welcome to the Ancient Game of Nimm. The starting pile contains" + str(NUMBER_OF_STARTING_STONES) + " stones."
    stones_remaining = int(NUMBER_OF_STARTING_STONES)
    stones_chosen = 0
    while (stones_remaining > 0):
    	while 1 != stones_chosen != 2:
    		stones_chosen = int(input("would you like to remove 1 or 2 stones?"))
    	stones -= stones_chosen
    	if stones_remaining >0:
    		print("There are " + str(stones) + " left.")
    print("End of game")
    

if __name__ == '__main__':
    main()