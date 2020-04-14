'''
    Simple implementation of the IFunction as an example.
'''
from app.functions.interface import IFunction, argument_definition

class DriverSearch(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-l',False, 'Last name of driver'),
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
                driver_data = self.datasets[IFunction.DRIVER_DATA]
                race_data = self.datasets[IFunction.RACE_DATA]
                results_data = self.datasets[IFunction.RESULTS_DATA]
                driver_info = None

                search_header = "Search All Drivers:"
                if '-l' in execute_args.keys():
                    search_header = "Search Drivers By Last Name {}:".format(execute_args['-l'])
                    driver_info = driver_data.get_by_name(None,execute_args['-l'])
                elif '-y' in execute_args.keys():
                    search_header = "Search Drivers By Year {}:".format(execute_args['-y'])
                    races = race_data.get_by_race_year(execute_args['-y'])
                    driver_id_list = []
                    driver_info = []
                    print("Races", len(races))
                    for race in races:
                        race_results = results_data.get_by_race_id(race.raceId)
                        for race_result in race_results:
                            if race_result.driverId not in driver_id_list:
                                driver_id_list.append(race_result.driverId)
                                current_driver = driver_data.get_by_driver_id(race_result.driverId)
                                driver_info.extend(current_driver)
                else:
                    driver_info = driver_data.get_by_name(None,None)

                # Now dump out what we found
                print("{}: {} drivers".format(search_header, len(driver_info)))
                print("%s" % ("-".ljust(85,'-') ))
                print("%s | %s | %s | %s | %s" % (
                    "Driver ID".center(10), 
                    "First Name".center(18), 
                    "Last Name".center(18), 
                    "DOB".center(15),
                    "Nationality".center(17)) )
                print("%s" % ("-".ljust(85,'-') ))

                for driver in driver_info:
                    print("%s | %s | %s | %s | %s" % (
                        driver.driverId.center(10), 
                        driver.forename.center(18), 
                        driver.surname.center(18), 
                        driver.dob.center(15),
                        driver.nationality.center(17)) )

        except Exception as ex:
            print(str(ex))
            raise ex
