#Pick three names and store them in a list.

#Prompt the user to enter their name. 
#If their name is one of the names in the list, display a greeting message that includes their name. 
#If their name isn't in the list, display "Who goes there?"



name_list = []
name_list.append("Martha")
name_list.append("Josh")
name_list.append("Yolo")


def Password(name_list):
	print("What is Your Name?")
	name = input()
	if name in name_list:
		print('Welcome {}'.format(name))	

	else:
		print("Who goes there?")


Password(name_list)
#print(name_list)