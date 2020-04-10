'''
    Example using data files to collect and coordinate data. 

    Data used for this example is from the Formula One World Championship
    from the years 1950-2017 and was collected from kaggle.com
        https://www.kaggle.com/cjgdev/formula-1-race-data-19502017

    In this example we use 4 of the data files
        drivers.csv
        results.csv
        status.csv
        races.csv

    We use a drivers name to look up the driver. From there we get the 
    driver ID in which we can look up their results. 

    With the results, we collect information about the race and the final
    status for the driver. 

    Finally we print this information out as a table. 

    All of this work occurs in the funciton get_driver_results with the 
    help of the DataFile class defined in readers/base.py.

    Line 170 is where we exercise the function itself. 
'''
from readers.base import *

'''
    Create readers for drivers, races and results
'''
race_file = DataFile('data', 'races.csv')
driver_file = DataFile('data', 'drivers.csv')
result_file = DataFile('data', 'results.csv')
status_file = DataFile('data', 'status.csv')

def get_driver_results(first_name, last_name):
    '''
        This funciton will get a specific drivers results using 
        three of the data files. More data, of course, is available
        but this is a simple example on how to collect data across files.

        Fields of interest from the files are: 
        Driver
            driverId
            forename
            surname
        Race
            raceId
            year
            name    
        Result
            raceId
            driverId
            grid
            position
            statusId
        Status
            statusId
            status
    '''
    global race_file
    global driver_file
    global result_file
    global status_file

    '''
        Get all indexes that will be needed from the data rows retrieved.
    '''
    #Driver Indexes
    driver_id_index = driver_file.get_field_index('driverId')
    driver_forename_idx = driver_file.get_field_index('forename')
    driver_surname_idx = driver_file.get_field_index('surname')

    # Race indexes
    race_round_idx = race_file.get_field_index('round')        
    race_year_idx = race_file.get_field_index('year')        
    race_name_idx = race_file.get_field_index('name')

    # Result Indexes
    result_race_id_index = result_file.get_field_index('raceId')
    result_grid_index = result_file.get_field_index('grid')
    result_position_index = result_file.get_field_index('position')
    result_status_index = result_file.get_field_index('statusId')

    # Status Indexes
    status_idx = status_file.get_field_index("status")

    # Find the driver
    driver = driver_file.find([column_data('surname',last_name), column_data('forename', first_name)])
    assert(len(driver) == 1)
    driver = driver[0]

    # Get driver race results    
    driver_id = driver[driver_id_index]
    driver_results = result_file.find([column_data('driverId',driver_id)])

    # Some total statistics
    total_grands_prixs = len(driver_results)
    pole_positions = 0
    front_row_starts = 0
    podium_finishes = 0
    dnf_total = 0

    race_results_by_year = {}

    for result in driver_results:
        # Get the specific results
        starting_grid_position = result[result_grid_index]
        finishing_position = result[result_position_index]
        status_id = result[result_status_index]

        if not finishing_position.strip():
            finishing_position = "DNF"
            dnf_total += 1
        elif finishing_position in ['1','2','3']:
            podium_finishes += 1

        if starting_grid_position in ['1','2']:
            front_row_starts += 1
            if starting_grid_position == '1':
                pole_positions += 1

        # Find the status
        current_status = status_file.find([column_data('statusId',status_id)])
        current_status = current_status[0][status_idx]

        # Now find the race 
        current_race = race_file.find([column_data('raceId',result[result_race_id_index])])

        race_round = current_race[0][race_round_idx]
        year = current_race[0][race_year_idx]
        name = current_race[0][race_name_idx]

        # Put it in the collection 
        if year not in race_results_by_year.keys():
            race_results_by_year[year] = {}
        race_results_by_year[year][race_round] = "%4s %6s %20s %s" % (
            starting_grid_position,
            finishing_position,
            current_status,
            name
        )

    # Now dump out all the information we have collected
    print("{} {} Results:".format(driver[driver_forename_idx], driver[driver_surname_idx]))
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

'''
    Test out functionality
'''
get_driver_results('Alberto','Ascari')
#get_driver_results("Max", "Verstappen")    
#get_driver_results("Ayrton", "Senna")    