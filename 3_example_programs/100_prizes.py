'''
    Arrays and indexing to win a prize

    How long is an array? 
    What index does it start at?
'''
prizes = [ "Ferrari","Mclaren","Porche","VW"]

selection = int(input("\nEnter a value between 1 and " + str(len(prizes)) + " to see your prize! ")) -1

if selection >= 0 and selection < len(prizes):
    print("Awesome you won a " , prizes[selection])
else:
    print("Invalid selection")