import numpy as np
from traits.api import (HasTraits, List, Float, Tuple, Instance, Bool, Str, 
    Int, Either)

class Electrode(HasTraits):
#    ct_coords = List(Float)
#    surf_coords = List(Float)
#    snap_coords = List(Float)
    ct_coords = Tuple
    surf_coords = Tuple
    #snap_coords = Tuple
    snap_coords = Instance(np.ndarray)

    is_interpolation = Bool(False)
    grid_name = Str('unsorted')
    grid_transition_to = Str('')
    
    hemi = Str
    vertno = Int(-1)
    pial_coords = Instance(np.ndarray)

    geom_coords = Either(None, Tuple)

    #def __eq__(self, other):
    #    return np.all(self.snap_coords == other)

    def astuple(self):
        return nparrayastuple(self.snap_coords)

def nparrayastuple(nparray):
    nparray = np.array(nparray)
    return (nparray[0], nparray[1], nparray[2])
