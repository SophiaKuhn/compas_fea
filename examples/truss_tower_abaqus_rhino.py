"""A compas_fea package example for truss elements."""

from compas_fea.cad import rhino

from compas_fea.structure import ElementProperties as Properties
from compas_fea.structure import GeneralStep
from compas_fea.structure import PinnedDisplacement
from compas_fea.structure import PointLoad
from compas_fea.structure import Steel
from compas_fea.structure import Structure
from compas_fea.structure import TrussSection


__author__     = ['Andrew Liew <liew@arch.ethz.ch>']
__copyright__  = 'Copyright 2017, BLOCK Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'liew@arch.ethz.ch'


# Create empty Structure object

mdl = Structure(name='truss_tower', path='C:/Temp/')

# Add truss elements

rhino.add_nodes_elements_from_layers(mdl, line_type='TrussElement', layers=['elset_struts'])

# Add node and element sets

rhino.add_sets_from_layers(mdl, layers=['nset_pins', 'nset_top', 'elset_struts'])

# Add materials

mdl.add_material(Steel(name='mat_steel', fy=355))

# Add sections

mdl.add_section(TrussSection(name='sec_truss', A=0.0050))

# Add element properties

ep = Properties(material='mat_steel', section='sec_truss', elsets='elset_struts')
mdl.add_element_properties(ep, name='ep_strut')

# Add loads

mdl.add_load(PointLoad(name='load_top', nodes='nset_top', z=-1000000))

# Add displacements

mdl.add_displacement(PinnedDisplacement(name='disp_pinned', nodes='nset_pins'))

# Add steps

mdl.add_step(GeneralStep(name='step_bc', displacements=['disp_pinned']))
mdl.add_step(GeneralStep(name='step_load', loads=['load_top']))
mdl.steps_order = ['step_bc', 'step_load']

# Structure summary`

mdl.summary()

# Run and extract data

mdl.analyse_and_extract(software='abaqus', fields=['u', 's'])

# Plot displacements

rhino.plot_data(mdl, step='step_load', field='um')

# Plot stress

rhino.plot_data(mdl, step='step_load', field='smises', iptype='max', nodal='max')
