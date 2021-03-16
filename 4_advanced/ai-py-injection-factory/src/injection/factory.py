import typing
import inspect
from injection.exceptions import (
    FactoryArgCountException,
    FactoryMissingArgException
)


class ObjectFactory:
    """
    NOTE: For injection to work your classes must include typing information 
          for the parameters to it's __init__ funciton, i.e. 

            def __init__(self, data_store : IDataStore, store_query : str):          
                ...

    Object factory can be responsible for
    - Generating objects on the fly with optional dependency injection.
    - When instructed for a singleton, storing the singleton for later retreival
      whether that be user request or using a dependency injection.

    NOTES:

    Injection of an existing type:
    generate()
        - Type MUST exist in the singleton registry
    generate_with_targets()
        - Type MAY exist in teh singleton registery
        - Type may be generated on the fly but MUST have an __init__ function that 
          requires no parameters. If it does require parameters it must be pre-registered.        

    Generation - With or without targets.

    Singleton flag
        If provided will (1) return a singleton of that type IF one exists in the registry
        OR (2) generate an instance of that type and store it in the registry.

        If a class of the given type already exists in the registry and the singleton flag is
        TRUE:
            Returns the instance in the registry and will not create another one regardless
            of any additional parameters. That is, you get the existing instance of the 
            type with however it was generated initially. 
        FALSE:
            Returns a NEW instance of the type ignoring any already registered singletons
            of that type and does NOT store the instance being returned. 

    generate_with_targets:
    This is meant to be used in a case where there are multiple types of object that 
    can be injected, mainly through inheritance. For example

    IStore -> LocalStore, SqlStore, CosmosStore -> all registered as singletons

    And an instance of IWork which in it's constructor takes an IStore. Using a simple
    generate call we would always get the same IStore returned.

    Using generate with targets we could define the target as [CosmosStore] to ensure the 
    instance of IWork gets the appropriate store injected. 
    """

    def __init__(self):
        # Singleton dictionary to regsiter and store instance objects
        self.singleton_registry = {}
        # Dictionary to cache construction props for any class. All entries
        # are key=class value=Dictionary where key maps to a __init__ parameter
        # name and value is whatever value is expected. 
        self.generation_props = {}

    def register_singleton(self, obj) -> None:
        """
        Registers an object into the singleton_registry

        Parameter:
        obj : An actual instance of the object.

        Returns:
        None
        """
        self.singleton_registry[type(obj)] = obj       

    def unregister_singleton(self, klass) -> None:
        """
        Unregisters an object from the singleton_registry

        Parameter:
        klass : The class name to unregister as an actual type : class

        Returns:
        None
        """
        if klass in self.singleton_registry:
            del self.singleton_registry[klass]

    def get_singleton(self, klass) -> object:
        """
        Gets an instance of a singleton based off of class type. 

        Parameter:
        klass : The class name to unregister as an actual type : class

        Returns:
        Instance if the klass has an entry in the registry, None otherwise.
        """
        return_value = None
        if klass in self.singleton_registry:
            return_value = self.singleton_registry[klass]
        return return_value            

    def is_singleton(self, klass) -> bool:
        """
        Returns a flag if the klass type exists in the singleton registry.

        Parameter:
        klass : The class name to unregister as an actual type : class

        Returns:
        True if a singleton of that type, False otherwise.
        """
        if klass in self.singleton_registry:
            return True
        return False            

    def register_construction_props(self, klass, optional_args : typing.Dict[str, object]) -> None:
        """
        Registers construction properties, or a subset of properties, to be used
        when instantiating an instance of klass.

        Parameter:
        klass : The class name to unregister as an actual type : class
        optional_args : Dictionary where key is the __init__ param name and value
            is whatever is expected as an input.

        NOTE: If the constructor will have somethign injected it does not need to be 
              part of this dictionary. Only include data that will (1) not be in the 
              registry or (2) cannot be generated.

        Returns:
        None
        """
        self.generation_props[klass] = optional_args

    def generate(
        self, 
        klass , 
        singleton: bool,  
        optional_args : typing.Dict[str, object]) -> object:
        """
        Generates an instance of klass 

        Parameter:
        klass : The class name to generate an instance of : class
        singleton:
            True - If an instance of klass exists, you will get that back. If one
                   doesn't exist, creates it and registers it.
            False - Will always create a new instance of klass and not register it.
        optional_args:
            For all other init parameters that can not be injected, this is a dictionary
            with a key matching a parameter name in __init__ and a value of whatever that
            field expects.

        Returns:
        Instance of klass 

        Throws:
        FactoryArgCountException        
        FactoryMissingArgException
        TypeError
        Any exception thrown by object creation not covered here.
        """
        return_instance = None

        if singleton and self.is_singleton(klass):
            return_instance = self.get_singleton(klass)

        if not return_instance:
            return_instance = self._internal_generate(klass, None, optional_args)
            if return_instance and singleton:
                self.register_singleton(return_instance)

        return return_instance

    def generate_with_targets(
        self, 
        klass , 
        singleton: bool, 
        injection_targets: typing.List[object] , 
        optional_args : typing.Dict[str, object] ) -> object:
        """
        Generates an instance of klass with specified injection targets. 

        This is useful if there is more than one class already registered with 
        the registry that matches (through inheritance).

        Parameter:
        klass : The class name to create an instance of: class
        singleton:
            True - If an instance of klass exists, you will get that back. If one
                   doesn't exist, creates it and registers it.
            False - Will always create a new instance of klass and not register it.
        injection_targets:
            List of klass to inject so as not to take anything that is in the registry.
            If an injection target is to be generated from scratch it MUST have an empty
            __init__ argument list. 

            Regardless of singleton flag, any target that is generated in this call will
            itself NOT be registered in the registry.
        optional_args:
            For all other init parameters that can not be injected, this is a dictionary
            with a key matching a parameter name in __init__ and a value of whatever that
            field expects.
            
        Returns:
        Instance of klass 

        Throws:
        FactoryArgCountException        
        FactoryMissingArgException
        TypeError
        Any exception thrown by object creation not covered here.
        """
        targets = []
        removable_targets = []
        return_instance = None

        if singleton and self.is_singleton(klass):
            return_instance = self.get_singleton(klass)
        else:
            for injection_target in injection_targets:
                inject_object = None
                if self.is_singleton(injection_target):
                    inject_object = self.get_singleton(injection_target)
                else:
                    inject_object = self.generate(injection_target,False, None)
                    self.register_singleton(inject_object)
                    removable_targets.append(inject_object)

                if not inject_object:
                    raise Exception("Cannot generate injection target {}".format(str(injection_target)))
                targets.append(inject_object)

            if len(targets) == 0:
                targets = None                    

            return_instance = self._internal_generate(klass, targets, optional_args)   

            if return_instance and singleton:
                self.register_singleton(return_instance)

            for target in removable_targets:
                # Don't keep around whatever was generated if it wasn't already a singleton
                self.unregister_singleton(type(target))

        return return_instance

    def _internal_generate(
        self, 
        klass , 
        inject_targets : typing.List[object], 
        optional_args : typing.Dict[str, object] ) -> object:
        """
        Generates an instance of klass with specified injection targets. 

        Parameter:
        klass : The class name to generate an instance of : class
        inject_targets:
            Instances of object to inject to the argument list for init.

            If klass requires an object not in this list it will then check the 
            registry.
        optional_args:
            For all other init parameters that can not be injected, this is a dictionary
            with a key matching a parameter name in __init__ and a value of whatever that
            field expects.
            
        Returns:
        Instance of klass 

        Throws:
        FactoryArgCountException        
        FactoryMissingArgException
        TypeError
        Any exception thrown by object creation not covered here.
        """
        args = []
        arg_count = 0

        for member in inspect.getmembers(klass):
            # When we hit init, find the args                
            if member[0] == '__init__':
                for arg in inspect.getfullargspec(member[1]):
                    # __init__ must be declared with type information on parameters. That
                    # shows up as a dictioanry where key=name value=type
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
                            elif klass in self.generation_props:
                                # Have some pre-registered settings
                                if arg_name in self.generation_props[klass]:
                                    # Optional args were passed in
                                    args.append(self.generation_props[klass][arg_name])
                                    arg_found = True

                            # Do we have targets? Check there next.
                            if inject_targets:
                                for inject_target in inject_targets:
                                    if isinstance(inject_target, arg[arg_name]):
                                        args.append(inject_target)
                                        arg_found = True                                
                                        break
                            
                            # Still not there? Last check is in singleton registry
                            if not arg_found and len(self.singleton_registry):
                                for class_type in self.singleton_registry:
                                    # Make sure it's an instance based on the type setting in 
                                    # the parameters list....derivations work with this as well.
                                    if isinstance(self.singleton_registry[class_type], arg[arg_name]):
                                        args.append(self.singleton_registry[class_type])
                                        arg_found = True                                
                                        break

                            if not arg_found:
                                raise FactoryMissingArgException(klass, arg_name)
                break
        
        if len(args) != arg_count:
            raise FactoryArgCountException(klass, arg_count, len(args))

        return klass(*args)
