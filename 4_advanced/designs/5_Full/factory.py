import typing
import inspect

class DIFactory:

    def __init__(self):
        self.register = {}
        self.generation_props = {}


    def register_object(self, obj) :
        self.register[type(obj)] = obj       

    def register_construction_props(self, object_type, optional_args : typing.Dict[str, object]):
        self.generation_props[object_type] = optional_args

    def generate(self, object_type , optional_args : typing.Dict[str, object]):
        return self._internal_generate(object_type, None, optional_args)


    def generate_with_targets(self, object_type , injection_targets: typing.List[object] , optional_args : typing.Dict[str, object] ) -> object:

        targets = []
        # Make sure we have all the injection targets built
        for injection_target in injection_targets:
            if injection_target not in self.register:
                inject_obj = self.generate(injection_target, None)
                if not inject_obj:
                    raise Exception("Cannot generate injection target {}".format(str(injection_target)))
                self.register_object(inject_obj)
                targets.append(inject_obj)

        if len(targets) == 0:
            targets = None                    

        return self._internal_generate(object_type, targets, optional_args)   

    def _internal_generate(self, object_type , inject_targets : typing.List[object], optional_args : typing.Dict[str, object] ):
        args = []
        arg_count = 0

        for member in inspect.getmembers(object_type):
            # When we hit init, find the args                
            if member[0] == '__init__':
                for arg in inspect.getfullargspec(member[1]):
                    # For things using type, there is definitely a dictionary
                    if isinstance(arg, dict):
                        # This is teh total number of args
                        arg_count = len(arg)

                        # Now is it in the register or the optional arguments passed in
                        for arg_name in arg.keys():
                            arg_found = False                                    
                            if optional_args and arg_name in optional_args:
                                # Optional args were passed in
                                args.append(optional_args[arg_name])
                                arg_found = True
                            elif object_type in self.generation_props:
                                # Have some pre-registered settings
                                if arg_name in self.generation_props[object_type]:
                                    # Optional args were passed in
                                    args.append(self.generation_props[object_type][arg_name])
                                    arg_found = True

                            # Do we have targets or are we using the inject_targets param?
                            #if not arg_found and len(self.register):
                            if not arg_found and len(self.register):
                                
                                # Is it in the inject targets?
                                if inject_targets:
                                    for inject_target in inject_targets:
                                        if isinstance(inject_target, arg[arg_name]):
                                            args.append(inject_target)
                                            arg_found = True                                
                                            break

                                # Or already registered?
                                if not arg_found and len(self.register):
                                    for class_type in self.register:
                                        # Make sure it's an instance based on the type setting in 
                                        # the parameters list....derivations work with this as well.
                                        if isinstance(self.register[class_type], arg[arg_name]):
                                            args.append(self.register[class_type])                                
                                            break
                break
        
        if len(args) != arg_count:
            raise Exception("Issue with arg count")

        return object_type(*args)
