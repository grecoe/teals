import json
from multi_command_utils.data_file import column_data
from multi_command_utils.interface import IFunction, argument_definition
from Formula1.f1_functions.constants import F1DataConstants
from Formula1.f1_functions.banner import print_banner, print_row

class ConstructorStandings(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-y',True, 'Formula 1 season (year)')
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
                race_data = self.datasets[F1DataConstants.RACE_DATA]
                constructor_data = self.datasets[F1DataConstants.CONSTRUCTOR_DATA]
                constructor_standing_data = self.datasets[F1DataConstants.CONSTRUCTOR_STANDINGS_DATA]

                # -y is required and the only way to run this
                # Races come back in order
                races = race_data.get_by_race_year(execute_args['-y'])
                standings = constructor_standing_data.get_by_race_id(races[-1].raceId)

                if standings and len(standings):
                    for standing in standings:
                        standing.points = int(float(standing.points))

                    headers = ["Position", "Points", "Name","Nationality"]
                    columns = [10,8,20,13]
                    print_banner(columns, headers)

                    standings = sorted(standings, reverse=True, key=lambda standing : standing.points)
                    for standing in standings:
                        name, nationality = self._get_constructor_info(constructor_data, standing.constructorId)

                        print_row(
                            columns,
                            [
                                standing.position,
                                standing.points,
                                name,
                                nationality
                            ],
                            False
                        )    

        except Exception as ex:
            print(str(ex))
            raise ex

    def _get_constructor_info(self, constructor_data, constructor_id):
        constructor = constructor_data.get_by_id(constructor_id)
        return constructor[0].name, constructor[0].nationality