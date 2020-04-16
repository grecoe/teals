'''
    List Races:

    This function supports searching for races. You can print out races
    for a whole year or a specific race. 

    Whole year view only shows the winner, race view shows all driver positions.


    1. -y : List races by a specific year
    2. -r : Search by a specific race id. 

    NOTE: Neither is required, but ONE must be present. 

    Order of precedence, when one is hit that is the result
        -y
        -r
'''
from readers.base import column_data
from app.utils.interface import IFunction, argument_definition
from app.f1functions.constants import F1DataConstants

class ListRaces(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-y',False, 'Races for a given year'),
            argument_definition('-r',False, 'Resuls for a specific race')
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
                results_file = self.datasets[F1DataConstants.RESULTS_DATA]

                races = []
                if ('-y' not in execute_args.keys()) and ('-r' not in execute_args.keys()):
                    raise Exception("-y or -r is required")

                if '-y' in execute_args.keys():
                    races.extend(race_data.get_by_race_year(execute_args['-y']))
                else:
                    races.extend(race_data.get_by_race_id(execute_args['-r']))

                # Get races and results bundled.
                full_results = {}
                for race in races:
                    full_results[race.raceId] = {}
                    full_results[race.raceId]['race'] = race
                    full_results[race.raceId]['result'] = results_file.get_by_race_id(race.raceId)

                # Regardless of result, we are going to have the same header
                print("%s" % ("-".ljust(85,'-') ))
                print("%s | %s | %s | %s | %s" % (
                        "Race ID".center(8), 
                        "Round".center(6), 
                        "Date".center(12), 
                        "Name".center(28), 
                        "Winner".center(25)) 
                        )
                print("%s" % ("-".ljust(85,'-') ))

                # Now what specifics do we want?
                if len(full_results) == 1:
                    # Only one race so we print out the same header followed
                    # by the individual results. 
                    for race_id in full_results:
                        race = full_results[race_id]['race']
                        results = full_results[race_id]['result']

                        winner = [x for x in results if x.position == '1']
                        winner_name = self._get_driver_name(driver_data,winner[0].driverId)
                        
                        self._output_race(race, winner_name)

                        # Now we dump all of them.
                        print("\n%s %s" % ("Position".center(10), "Driver"))
                        for result in results:
                            position = result.position if len(result.position.strip()) > 0 else "DNF"
                            driver_name = self._get_driver_name(driver_data,result.driverId)
                            print("%s %s" % (position.center(10), driver_name))

                else:
                    # Sort the races by race ids as they are in order
                    race_id_list = list(full_results.keys())
                    race_id_list.sort()

                    for race_id in race_id_list:
                        race = full_results[race_id]['race']
                        results = full_results[race_id]['result']

                        winner = [x for x in results if x.position == '1']
                        winner_name = self._get_driver_name(driver_data,winner[0].driverId)
                        
                        self._output_race(race, winner_name)

        except Exception as ex:
            print(str(ex))
            raise ex

    def _get_driver_name(self, driver_data, driver_id):
        driver = driver_data.get_by_driver_id(driver_id)
        return "{} {}".format(driver[0].forename, driver[0].surname )

    def _output_race(self, race, winners_name):
        print("%s | %s | %s | %s | %s" % (
            race.raceId.center(8), 
            race.round.center(6), 
            race.date.center(12), 
            race.name.center(28), 
            winners_name.center(25)) 
        )
