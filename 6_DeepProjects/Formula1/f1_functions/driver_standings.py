'''
    Driver Search:

    This function supports searching for drivers by:

    1. -l : Last name of a driver
            Lists all drivers with the same last name
    2. -y : A year of F1. Lists all the drivers that were involved
            in the championship that year. 
    3. -q : A query. Valid query fields are those found in the drivers.csv
            data file headers.
    4.    : No arguments returns all drivers who ever drove. 

    Order of precedence, when one is hit that is the result
        -q
        -l
        -y
'''
import json
from multi_command_utils.data_file import column_data
from multi_command_utils.interface import IFunction, argument_definition
from Formula1.f1_functions.constants import F1DataConstants
from Formula1.f1_functions.banner import print_banner, print_row

class DriverStandings(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-y',False, 'Formula 1 season (year)')
            ])

    def execute(self, args):
        try:
            # This call validates inputs. If a required arg isn't there 
            # or an additional, unexpected, arg is present it will except.
            execute_args = super()._parse_execute_arguments(args)

            if IFunction.GLOBAL_HELP in execute_args.keys():
                # Regardless of anything else, if help is there, show it and quit
                self.get_help(1)
            else:
                # At this point, you're clear and ready to go. 
                # This is where all your logic goes. 
                driver_data = self.datasets[F1DataConstants.DRIVER_DATA]
                race_data = self.datasets[F1DataConstants.RACE_DATA]
                driver_standing_data = self.datasets[F1DataConstants.DRIVER_STANDING_DATA]

                search_header = "Search All Years:"
                if '-y' in execute_args.keys():
                    search_header = "Search Standings By Year {}:".format(execute_args['-y'])
                    print(search_header)
                    headers = ["Position" ,"Points", "Driver"] 
                    columns = [10,8,20]
                    print_banner(columns,headers)

                    # Get all races for the year
                    races = race_data.get_by_race_year(execute_args['-y'])

                    # Only interested in the last one
                    race = races[-1]
                    standings = driver_standing_data.find([column_data('raceId', race.raceId)])
                    for standing in standings:
                        standing.points = int(float(standing.points))

                    # Sort on points
                    position = 1
                    standings = sorted(standings, reverse=True, key=lambda standing : standing.points)

                    # Now print them out.
                    for standing in standings:
                        print_row(
                            columns,
                            [
                                position, 
                                standing.points,
                                self._get_driver_info(driver_data,standing.driverId)
                            ],
                            False
                        )
                        position += 1

                else:
                    # Slightly different, we want to get the winner by each year
                    print(search_header)

                    headers = ["Year" ,"Driver Name"] 
                    columns = [8,30]
                    print_banner(columns,headers)
                    
                    # Get all the years 
                    years = race_data.get_column_by_name('year')
                    years = list(set(years))
                    years.sort(reverse = True)

                    # For each year, get the races and take the last one
                    for year in years:
                        # Get all races for the year
                        races = race_data.get_by_race_year(year)

                        # Only interested in the last one
                        race = races[-1]
                        standings = driver_standing_data.find([column_data('position', '1'),column_data('raceId', race.raceId)])
                        # Seems to have some, but not all, 2018 data so we will get no standings 
                        # for that year, so ignore it. 
                        if len(standings):
                            print_row(
                                columns,
                                [
                                    year,
                                    self._get_driver_info(driver_data, standings[0].driverId)
                                ],
                                False
                            )


        except Exception as ex:
            print(str(ex))
            raise ex

    def _get_driver_info(self, driver_data, driver_id):
        driver = driver_data.get_by_driver_id(driver_id)
        return "%s, %s" % (driver[0].surname, driver[0].forename)