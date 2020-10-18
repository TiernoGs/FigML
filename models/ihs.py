# -*- coding: utf-8 -*-

from PyQt5 import QtCore

from .property_helper import PropertyMeta, Property

class Model( QtCore.QObject, metaclass=PropertyMeta):


    project_name = Property( 'Untitled.fml' )

    def __init__( self, view ):
        super().__init__()
        self._view = view
        pass
