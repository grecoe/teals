# Menu Shopping Cart

This project is based on a class project with the Sophomores when getting into multiple for loops and arrays. 

Internally, data is kept in dictionaries and arrays, but this program is a good way to work on your skills with:

- Classes and class derivations
- Working within an existing program to extend functionality. 

The following files are provided for you:

|File|Contents|
|-----------|------------|
|example.py|The main program to run. It includes a definition of the application menu you need to flush out with implementations of the different required IFunction derivations.|
|cartconstants.py|Classes and constants you will need in your IFunction definitions. An instances of the ShoppingCart class (as in the example implementation) is used to be passed to each IFunction to be worked on by the larger program.|
|categories.py|An implementation of IFunction(CategoriesFunction) for dealing with one of the several program commands.|

There are several commands you will need to implement to make this program complete. You will find them stubbed out in the program menu with the stub() function. 

What you need to write (use categories.py as your example to build these out).

In examples.py by the menu declaration you will find a definition of the parameters the following functions must accept. 

|File|Contents|
|-----------|------------|
|show.py|IFunction implementation to show the contents of the cart or a specfic category of information in the cart.|
|add.py|IFunction implementation to add items to your shopping cart.|
|remove.py|IFunction implementation to remove items from your shopping cart.|
