#coding:utf-8
from __future__ import print_function
import os, glob, re, pprint
import pprint

import NodegraphAPI
import Nodes3DAPI
import Nodes2DAPI
import UI4.Widgets as Widgets

from Katana import (
    QtCore, QtGui, QtWidgets,
    UI4, NodegraphAPI, Nodes3DAPI
)


class TextureMonitor(UI4.Tabs.BaseTab):
    def __init__(self, parent):
        UI4.Tabs.BaseTab.__init__(self, parent)

        mlayout = QtWidgets.QVBoxLayout()
        self.setLayout(mlayout)

        self.itemFont = QtGui.QFont()
        self.itemFont.setPointSize(10)
        self.itemFont.setBold(True)
        # self.colorFont = QtGui.QBrush(QtGui.QColor(9, 255, 212))
        self.itemIconUDIM = QtGui.QIcon('/opt/vfxrepo/apps/prman_toolkit/scripts/txconverter/icons/clamp_clamp.jpg')
        self.itemIconChannel = QtGui.QIcon('/usr/local/Katana5.0v1/bin/python/UI4/Resources/Icons/Messages/info12.png')
        
        #
        button = QtWidgets.QPushButton()
        button.setText('Compute')
        button.setIcon(QtGui.QIcon('/opt/vfxrepo/apps/prman_toolkit/scripts/txconverter/icons/reload_hilite16.png'))
        mlayout.addWidget(button)
        button.pressed.connect(self.buildTree)

        #
        treeWidget = QtWidgets.QTreeWidget()
        treeWidget.setAlternatingRowColors(True)
        treeWidget.header().setVisible(False)
        treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        treeWidget.customContextMenuRequested.connect(self.rightclick)
        mlayout.addWidget(treeWidget)
        self.treeWidget = treeWidget


    def buildTree(self, node=None):
        self.treeWidget.clear()
        self.node = NodegraphAPI.GetViewNode()

        celstr = '//*{hasattr("geometry.arbitrary.txPath")}'
        collector = Widgets.CollectAndSelectInScenegraph(celstr, '/root')
        self.locations = collector.collectAndSelect(select=False, node=self.node)

        result = []
        self.rootPath = '/show/pipe/publish/3d'
        producer = Nodes3DAPI.GetGeometryProducer(node=self.node)

        data = {}
        for loc in self.locations:
            producerByPath = producer.getProducerByPath(loc)
            txPathAttr = producerByPath.getAttribute('geometry.arbitrary.txPath.value')
            txVerAttr = producerByPath.getAttribute('geometry.arbitrary.txVer.value')
            txLayerAttr = producerByPath.getAttribute('geometry.arbitrary.txLayer.value')
            txChannelAttr = '_<channel>'
            txUdimAttr = producerByPath.getAttribute('geometry.arbitrary.txUdim.value')
            texPath = None
            if txPathAttr:
                txPath = txPathAttr.getValue()
                texPath = self.rootPath + '/' + txPath
            if txVerAttr:
                txVer = txVerAttr.getValue()
                texPath += '/' + txVer + '/tex'
            if txLayerAttr:
                tvLayer = txLayerAttr.getValue()
                texPath += '/' + tvLayer
            if txChannelAttr:
                texPath += txChannelAttr
            if txUdimAttr: 
                # txUdim = txUdimAttr.getValue()
                texPath += '.<UDIM>'
            texPath += '.tex'

            if not texPath in data:
                data[texPath] = {'locations': []}
            data[texPath]['locations'].append(loc)

        for i in sorted(data):
            txPath_item = QtWidgets.QTreeWidgetItem(self.treeWidget) 
            txPath_item.setText(0, i) 
            txPath_item.setFont(0, self.itemFont)
            # txPath_item.setForeground(0, self.colorFont)
            nautilus_path = i.split('/tex/')[0] + '/tex'
            print (i)
                
            for tex_file in sorted(os.listdir(nautilus_path)):
                match = re.search(r"\.\d\d\d\d\.", tex_file)
                if i.find('<UDIM>') > 0:
                    if match:
                        location_item = QtWidgets.QTreeWidgetItem(txPath_item)
                        location_item.setText(0, tex_file)
                        location_item.setIcon(0, self.itemIconUDIM)
                else:
                    if not match:
                        location_item = QtWidgets.QTreeWidgetItem(txPath_item)
                        location_item.setText(0, tex_file)
                        location_item.setIcon(0, self.itemIconChannel)
                

            self.treeWidget.expandAll()
            self.data = data

    def rightclick(self, pos):
        menu = QtWidgets.QMenu(self)
        self.print_action = menu.addAction('Select Katana Scenegraph ', self.selectLocation)
        action = menu.exec_(self.mapToGlobal(pos))

    def selectLocation(self):
        sg = Nodes3DAPI.ScenegraphManager.getActiveScenegraph()        
        sg.clearSelection()
        items = self.treeWidget.selectedItems()
        if not items:
            return
        item = items[0]
        txt = item.text(0)
        if self.rootPath in txt:
            location_list = self.data[txt]['locations']
            for location in location_list:
                sg.setLocationSelected(location)
                sg.ensureLocationVisible(location)
        else:
            print ('sibong')
            
PluginRegistry = [
    ('KatanaPanel', 2.0, 'TextureMonitor', TextureMonitor),
]

