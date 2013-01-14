""" pyurdme model file for reversible dimerization on a surface. """
import os
from pyurdme.urdme import *

def dimerization(model_name=""):
    """ Dimerization. The reversible reaction A+B<->C on a
        surface. """
    if model_name == "":
        model_name = "dimerization"
    model = URDMEModel(name=model_name);

    # Species
    A = Species(name="A",initial_value=0,reaction_radius=1e-9,diffusion_constant=1e-14);
    B = Species(name="B",initial_value=0,reaction_radius=1e-9,diffusion_constant=1e-14);
    C = Species(name="C",initial_value=100,reaction_radius=1e-9,diffusion_constant=1e-14);

    model.addSpecies([A,B,C])

    # Parameters
    k1 = Parameter(name="k1",expression=1.0e6)
    k2 = Parameter(name="k2",expression=1.0)

    model.addParameter([k1,k2])

    # Reactions
    R1 = Reaction(name="R1",reactants={A:1,B:1},products={C:1},massaction=True,rate=k1)
    R2 = Reaction(name="R2",reactants={C:1},products={A:1,B:1},massaction=True,rate=k2)
    model.addReaction([R1,R2])

    # Import a Gmsh mesh and physical regions (subdomains)
    # mesh = dolfin.Mesh('meshes/surface.xml')
    # sd = dolfin.MeshFunction('meshes/surface_physical_region.xml')

    # model.mesh = mesh
    
    # Create extended mesh (Will this be necessary?) for use with URDME
    # model.meshextend()
    
    # Read the Physical IDs.

    # Define the spatial distribution of the molecules
    #mesh.

    return model


if __name__ == '__main__':
    """ Create a model and assemble the URDME input file. """
    model = dimerization()
    
#model.serialize()