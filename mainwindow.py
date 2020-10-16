# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

from models.ihs import Model


class MainWindow ( QQuickView ):

    def __init__( self ):
        super().__init__()

        # Attributes
        self._model = None

        # Custom view
        self.setWidth(1280)
        self.setHeight(720)
        self.setTitle("Fig")

        self.setResizeMode( QQuickView.SizeRootObjectToView )
        self.setSource( QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), "qml/MainView.qml")) )
        self.rootContext().setContextProperty( "MainWindow", self )

        # Model-View-Controller
        self.initMVC()

    def initMVC(self):
        self._model = Model( self )
        self.engine().rootContext().setContextProperty( "model", self._model )


if __name__ == "__main__":

    sys.argv += ['--style', 'material']

    app = QGuiApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


