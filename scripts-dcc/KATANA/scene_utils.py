from __future__ import print_function
import sys, os, json

from Katana import NodegraphAPI
from Katana import Nodes3DAPI

def GetProducer(node=None, location=None):
    NodegraphAPI.SetNodeViewed(node, True, exclusive=True)
    producer = Nodes3DAPI.GetGeometryProducer(node=node)
    if location:
        producer = producer.getProducerByPath(location)
    return producer


def GetChildren(producer):
    children = []
    for child in producer.iterChildren():
        children.append(child)
    return children


def travel(producer):
    stack = [producer]
    locations = []
    while stack:
        child = stack.pop()
        children = child.iterChildren()
        locations.append(child)
        stack.extend(children)
    return locations


def GetProducerSpecific(producer, specific_type):
    locations = travel(producer)
    specific_locations = []
    for location in locations:
        if specific_type != location.getType():
            continue
        specific_locations.append(location)
    return specific_locations

def showLocation(producers):
    for producer in producers:
        print (producer.getFullName())




