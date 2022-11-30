import UI4
from Katana import QtCore, QtGui, QtWidgets


main_window = UI4.App.Layouts._PrimaryWindow
main_menu = main_window.findChild(UI4.App.MainMenu.MainMenu)
main_layout = main_window.findChild(QtWidgets.QVBoxLayout)
# studio_menu.deleteLater()


studio_menu = QtWidgets.QMenu(parent=main_menu)
studio_menu.setTitle('LOCUS')
main_menu.addMenu(studio_menu)
tools = ['Update PrmanShaders', 'UsdVariantSet', 'Variant Viewer', 'Macro Update']

studio_toolbar = QtWidgets.QToolBar(parent=main_menu)
studio_toolbar.setWindowTitle('LOCUS')
# print (main_layout.addWidget(studio_toolbar))


for tool in tools:
    action = QtWidgets.QAction(studio_menu)
    action.setText(tool)
    studio_menu.addAction(action)

    studio_toolbar.addAction(action)

# import UI4
# from PyQt5 import QtWidgets

# def get_main_window():
#     return UI4.App.Layouts._PrimaryWindow

# main_window = get_main_window()
# main_menu = main_window.findChild(UI4.App.MainMenu.MainMenu)

# for each in main_window.children():
#     print (each.objectName())