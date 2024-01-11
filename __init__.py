# GUI for Numerical Predictions on Graviton3 
# Copyright (c) Odycloud.

import sys
import subprocess
from qgis.core import QgsCoordinateReferenceSystem, QgsProject
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolBar, QPushButton
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre')
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre/GUI')

def classFactory(iface):
    """Load QGISPlugin class.
    """
    from mainPlugin import QGISPlugin  
    QgsProject.instance().title = 'MODELING'
#    titulus = QgsProject.instance().title() 
    title = iface.mainWindow().windowTitle()
    new_title = title.replace('QGIS', 'Gv3 Graphical Interface')
    iface.mainWindow().setWindowTitle(new_title)

    odyicon = QIcon("/opt/.Odycloud/Ody_NumPre/GUI/mixed_logo5plb63.png")
    iface.mainWindow().setWindowIcon(odyicon)
    
# menus    
    vector_menu = iface.vectorMenu()
    raster_menu = iface.rasterMenu()
    database_menu = iface.databaseMenu()
    web_menu = iface.webMenu()
    menubar = vector_menu.parentWidget()
    menubar.removeAction(vector_menu.menuAction())
    menubar.removeAction(raster_menu.menuAction())
    menubar.removeAction(database_menu.menuAction())
    menubar.removeAction(web_menu.menuAction())
    for w in iface.statusBarIface().children():
        if w.__class__.__name__ == 'QWidget':
            for c in w.children():
                if c.__class__.__name__ == 'QgsFilterLineEdit':
                    w.hide()
                    break
    return QGISPlugin(iface)


