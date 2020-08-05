import importlib
from iface import Distractor

mod = 'impl'



def get_interface(mod_name, iface):
    iface_return = None

    # Get information on the type of interface we are getting
    iface_impl = iface()
    iface_name = iface_impl.__class__

    loaded_mod = importlib.import_module(mod)

    for i in dir(loaded_mod):
        mod_attr = getattr(loaded_mod, i)

        if callable(mod_attr):
            try:
                t_created = mod_attr()
                if isinstance(t_created, Distractor) and t_created.__class__ != iface_name:
                    iface_return = t_created
            except:
                pass
    return iface_return

thing = get_interface(mod, Distractor)
thing.func("Dan")
quit()


