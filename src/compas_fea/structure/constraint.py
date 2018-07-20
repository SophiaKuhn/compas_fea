
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


__author__    = ['Andrew Liew <liew@arch.ethz.ch>']
__copyright__ = 'Copyright 2018, BLOCK Research Group - ETH Zurich'
__license__   = 'MIT License'
__email__     = 'liew@arch.ethz.ch'


__all__ = [
    'Constraint',
    'TieConstraint',
]


class Constraint(object):

    """ Initialises base Constraint object.

    Parameters
    ----------
    name : str
        Name of the Constraint object.

    Returns
    -------
    None

    """

    def __init__(self, name):

        self.__name__ = 'ConstraintObject'
        self.name = name
        self.attr_list = ['name']

    def __str__(self):

        print('compas_fea {0} object'.format(self.__name__))
        print('-' * (len(self.__name__) + 10))

        for attr in self.attr_list:
            print('{0:<10} : {1}'.format(attr, getattr(self, attr)))

        return ''


class TieConstraint(Constraint):

    """ Tie constraint between two sets of nodes, elements or surfaces.

    Parameters
    ----------
    name : str
        TieConstraint name.
    master : str
        Master set name.
    slave : str
        Slave set name.
    tol : float
        Constraint tolerance, distance limit between master and slave.

    Returns
    -------
    None

    """

    def __init__(self, name, master, slave, tol):
        Constraint.__init__(self, name=name)

        self.__name__ = 'TieConstraint'
        self.master = master
        self.slave = slave
        self.tol = tol
        self.attr_list.extend(['master', 'slave', 'tol'])
