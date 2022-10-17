# NuPrGvtres 
# Copyright (c) Odycloud.

#!python
#cython: language_level=3
import sys
sys.path.append('/opt/Odycloud/NumPre_Gv3')

def classFactory(iface):
    """Load QGISPlugin class.
    """
###    from NumPre_Gv3.plugin.constants import PLUGIN_NAME
###    from NumPre_Gv3.plugin.ui.helpers import WaitDialog
    import bibliotheca
  
    title = iface.mainWindow().windowTitle()
    new_title = title.replace('QGIS', 'Gv3 Graphical Interface')
    iface.mainWindow().setWindowTitle(new_title)
    vector_menu = iface.vectorMenu()
    raster_menu = iface.rasterMenu()
#    mesh_menu = iface.meshMenu()
    database_menu = iface.databaseMenu()
    web_menu = iface.webMenu()
#    processing_menu = iface.processingMenu()
    menubar = vector_menu.parentWidget()
    menubar.removeAction(vector_menu.menuAction())
    menubar.removeAction(raster_menu.menuAction())
    menubar.removeAction(database_menu.menuAction())
#    menubar.removeAction(mesh_menu.menuAction())
    menubar.removeAction(web_menu.menuAction())
#    menubar.removeAction(processing_menu.menuAction())
#    menubar.addAction(dummy_menu)
    return QGISPlugin(iface)

def dummy_menu():
    pass


