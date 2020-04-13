'''
    Same functionality as starter.py but using the abstraction 
    classes in custom/*

    However this code is approximatey 40% smaller than starter.py 
    and the objects are easier to use.  
'''

from custom.Driver import *
from custom.Races import *
from custom.Results import *
from custom.Status import *
from custom.Constructor import *

driver_file = DriverDataFile() 
races_file = RacesDataFile()
results_file = ResultsDataFile()
status_file = StatusDataFile()
constructor_file = ConstructorsDataFile()

def get_driver_results(first_name, last_name):
    global driver_file
    global races_file
    global results_file
    global status_file
    global constructor_file

    # Find the driver
    driver = driver_file.get_by_name(first_name, last_name)
    assert(len(driver) == 1)
    driver = driver[0]

    # Get driver race results    
    driver_results = results_file.get_by_driver_id(driver.driverId)

    # Some total statistics
    total_grands_prixs = len(driver_results)
    pole_positions = 0
    front_row_starts = 0
    podium_finishes = 0
    dnf_total = 0
    race_results_by_year = {}

    for result in driver_results:

        dnf_total += 1 if result.is_dnf() else 0
        podium_finishes += 1 if result.is_podium() else 0
        front_row_starts += 1 if result.is_front_row_start() else 0
        pole_positions += 1 if result.is_pole_position() else 0

        # Get constructor
        constructor = constructor_file.get_by_id(result.constructorId)
        assert(len(constructor) == 1)
        constructor = constructor[0]

        # Find the status
        current_status = status_file.get_by_status_id(result.statusId)
        assert(len(current_status) == 1)
        current_status = current_status[0]

        # Now find the race 
        current_race = races_file.get_by_race_id(result.raceId)
        assert(len(current_race) == 1)
        current_race = current_race[0]

        # Put it in the collection 
        if current_race.year not in race_results_by_year.keys():
            race_results_by_year[current_race.year] = {}

        race_results_by_year[current_race.year][current_race.round] = "%10s %4s %6s %20s %s" % (
            constructor.name,
            result.grid,
            result.position if not result.is_dnf() else "DNF",
            current_status.status,
            current_race.name
        )

    # Now dump out all the information we have collected
    print("{} {} Results:".format(driver.forename, driver.surname))
    print("   Years In F1 :", len(race_results_by_year.keys()))
    print("   Grands Prix :", total_grands_prixs)
    print("   Front Rows  : {} of which {} are pole position".format(front_row_starts,pole_positions))    
    print("   Podiums     :", podium_finishes)
    print("   DNF Total   :", dnf_total)
    print("\n   RESULTS:")
    print("     YEAR ROUND GRID FINISH %20s NAME" %('STATUS'))
    years = list(race_results_by_year.keys())
    years.sort()
    for year in years:
        for race_round in race_results_by_year[year]:
            print("     %s %5s %s" % (year, race_round, race_results_by_year[year][race_round]))

def get_most_popular_last_name():
    global driver_file
    
    drivers = driver_file.get_by_name(None,None)
    names = {}
    for d in drivers:
        if d.surname not in names:
            names[d.surname] = 0
        names[d.surname] += 1

    names = sorted((value, key) for (key,value) in names.items())
    most_popular = names[-1]
    print("{} is most popular with {} occurances".format(most_popular[1], most_popular[0]))
    # Now get them and print the names
    drivers = driver_file.get_by_name(None,most_popular[1])
    for d in drivers:
        print("  {} {}".format(d.forename, d.surname))


#get_most_popular_last_name()
#quit()

'''
    Test out functionality
'''
get_driver_results('Pastor', None)
#get_driver_results('Alberto','Ascari')
#get_driver_results("Max", "Verstappen")    
#get_driver_results("Ayrton", "Senna")    