'''
    Driver Stats:

    This function supports printing out a drivers history (without
    titles won). 

    1. -f : First name of a driver
    2. -l : Last name of a driver
    3. -i : Driver ID

    QUERY IS NOT SUPPORTED

    Order of precedence, when one is hit that is the result
        -i      Driver ID
        -f/-l   Any valid information

    NOTE: If nore than one driver is returned, the first in the list
    is the one presented. 
'''

from multi_command_utils.interface import IFunction, argument_definition
from Formula1.f1_functions.constants import F1DataConstants

class DriverStats(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            [
            argument_definition('-f',False, 'First Name'),
            argument_definition('-l',False, 'Last Name'),
            argument_definition('-i',False, 'Driver ID'),
            ])

    def execute(self, args):
        try:
            # This call validates inputs. If a required arg isn't there 
            # or an additional, unexpected, arg is present it will except.
            execute_args = super()._parse_execute_arguments(args)

            if IFunction.GLOBAL_HELP in execute_args.keys():
                self.get_help(1)
            else:
                driver_data = self.datasets[F1DataConstants.DRIVER_DATA]
                driver_info = None

                if '-i' in execute_args.keys():
                    driver_info = driver_data.get_by_driver_id(execute_args['-i'])
                else:
                    first = execute_args['-f'] if '-f' in execute_args.keys() else None    
                    last = execute_args['-l'] if '-l' in execute_args.keys() else None    
                    driver_info = driver_data.get_by_name(first,last)

                if len(driver_info):
                    driver_info = driver_info[0]
                    self._get_stats(driver_info)
                else:
                    print("No driver info could be found for supplied information.")

        except Exception as ex:
            print(str(ex))

    def _get_stats(self, driver):
        print("{} : {}, {}".format(driver.driverId, driver.surname, driver.forename))

        results_file = self.datasets[F1DataConstants.RESULTS_DATA]
        constructor_file = self.datasets[F1DataConstants.CONSTRUCTOR_DATA]
        status_file = self.datasets[F1DataConstants.STATUS_DATA]
        races_file = self.datasets[F1DataConstants.RACE_DATA]

        # Get driver race results    
        driver_results = results_file.get_by_driver_id(driver.driverId)

        # Some total statistics
        total_grands_prixs = len(driver_results)
        pole_positions = 0
        front_row_starts = 0
        podium_finishes = 0
        dnf_total = 0
        teams = []
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
            # Get teams raced for
            if constructor.name not in teams:
                teams.append(constructor.name)

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

            race_results_by_year[current_race.year][current_race.round] = "%15s %4s %6s %s %s" % (
                constructor.name,
                result.grid,
                result.position if not result.is_dnf() else "DNF",
                current_status.status.center(20),
                current_race.name
            )

        # Now dump out all the information we have collected
        years_keys = list(race_results_by_year.keys())
        print("   Years In F1 :", len(race_results_by_year.keys()),"({} - {})".format(years_keys[-1], years_keys[0]))
        print("   Teams       :", len(teams),"-", ','.join(teams))
        print("   Grands Prix :", total_grands_prixs)
        print("   Front Rows  : {} of which {} are pole position".format(front_row_starts,pole_positions))    
        print("   Podiums     :", podium_finishes)
        print("   DNF Total   :", dnf_total)
        input("\nPress enter to see race results\n")
        print("\n   RESULTS:")
        print("     YEAR ROUND %15s GRID FINISH %s NAME" %('CONSTRUCTOR', 'STATUS'.center(20)))
        years = list(race_results_by_year.keys())
        years.sort()
        for year in years:
            for race_round in race_results_by_year[year]:
                print("     %s %5s %s" % (year, race_round, race_results_by_year[year][race_round]))
