'''
    LINK: https://www.interviewcake.com/question/python/mesh-message?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23270:%20MeshMessage&utm_medium=email&utm_medium=email

    QUESTION:
    You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.

    Instead of routing texts through cell towers, your app sends messages via the phones of nearby users, 
    passing each message along from one phone to the next until it reaches the intended recipient. 
    (Don't worry—the messages are encrypted while they're in transit.)

    Some friends have been using your service, and they're complaining that it takes a long time for messages 
    to get delivered. After some preliminary debugging, you suspect messages might not be taking the most direct 
    route from the sender to the recipient.

    Given information about active users on the network, find the shortest route for a message from one user 
    (the sender) to another (the recipient). 
    
    Return a list of users that make up this route.    
'''

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}

# ['Jayden', 'Amelia', 'Adam']
start = "Jayden"
destination = "Adam"

# PATH: ['Amelia', 'Jayden', 'Min', 'Omar']
#start = "Amelia"
#estination = "Omar"

# PATH: ['William', 'Min', 'Omar']
#start = "William"
#destination = "Omar"

# PATH: ['Omar'] (Test send to self)
#start = "Omar"
#destination = "Omar"

# PATH: ROUTE NOT POSSIBLE (Tests starter not present, initial expansion test)
#start = "Scott"
#destination = "Amelia"

# PATH: ROUTE NOT POSSIBLE (Test destination not present, loop limitations)
#start = "Omar"
#destination = "Abhinav"


'''
    It's possible that someone left the network but is still in a cache
    somewhere. So, make sure that user is still in network. 

    Return True if in the network False otherwise. 
'''
def validateNetworkUser(user):
    global network
    returnValue = False
    if user in network.keys():
        returnValue = True
    return returnValue

'''
    Expand a route from the start user. If the end (destination user) is found, leave immediately. 

    Returns a list of lists. First element is always start (where we came from) and the second is 
    someone they are connected to in the mesh network. 
'''
def expandRoutes(start, end):
    global network

    routes = []
    if validateNetworkUser(start):
        starter = []
        starter.append(start)
        for subUser in network[start]:
            routes.append(starter.copy())
            routes[-1].append(subUser)
            if subUser == end:
                break
    return routes

'''
    Takes a list of routes and expands it by finding the next person from the 
    next persons network. 

    For example

    INPUT: 
    
    [user1,user2] # User 2 is in user1's network

    OUTPUT: where user A-C are in user2's network
    [user1,user2,userA] 
    [user1,user2,userB] 
    [user1,user2,userC] 
'''
def continueExpansion(routes, destination):
    newRoutes = []

    for route in routes:
        subRoute = expandRoutes(route[-1], destination)
        for rt in subRoute:
            if rt[-1] not in route:
                cpy = route.copy()
                cpy.append(rt[-1])
                newRoutes.append(cpy)

        # Did the last route expansion find it? Did it even expand?
        if len(newRoutes) > 0 and destination in newRoutes[-1]:
            break

    return newRoutes


'''
    Program Code:

    This is where the work happens using the above information
'''

print(start, "wants to send a message to", destination)

# Competed routes collected here....
completeRoute = []

# Get the first set of routes which will have a list of lists [[start, next], [start, ....]]
if start == destination:
    completeRoute.append([start])
else:
    routes = expandRoutes(start, destination )
    # If start person is not in the network, we get no routes back.
    if len(routes) > 0:
        # Some common sense, don't loop forever
        attempt = 0
        maxAttempt = len(network) * 2
        while attempt < maxAttempt:

            # Check the current routes to see if destination is there
            for route in routes:
                if destination in route:
                    completeRoute.append(route)

            # If we found one or more, then get out....
            if len(completeRoute) > 0:
                break

            # If we are here, continue expanding in the mesh 
            routes = continueExpansion(routes,destination)
            attempt += 1
    else:
        print("It appears that", start, "is not currently in network.")

# Print out the results
if len(completeRoute) > 0:
    print("Shortest Route(s):")
    for route in completeRoute:
        print("    ", route)
else:
    print("Route not possible at this time")

