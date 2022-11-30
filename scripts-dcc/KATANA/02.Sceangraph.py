from __future__ import print_function

from Katana import NodegraphAPI
from Katana import Nodes3DAPI

# pack
def get_producer(knode, location=None):
    NodegraphAPI.SetNodeViewed(Knode, True, exclusive=True)

    producer = Nodes3DAPI.GetGeometryProducer(knode)
    if location:
        producer = producer.getProducerByPath(location)
    return producer

knode = NodegraphAPI.GetNode('UsdIn')
location = '/root/world/geo/houseB'
producer = get_producer(knode, location=location)

print (producer.getAttributeNames())

for child in producer.iterChildren():
    print (child.getFullName())


# unpack 1
knode = NodegraphAPI.GetNode('UsdIn') 
NodegraphAPI.SetNodeViewed(knode, True, exclusive=True)

producer = Nodes3DAPI.GetGeometryProducer(knode)

print (producer.getProducerByPath('/root/world/geo/houseB').getAttributeNames()) # 지정한 location의 attr 정보

for child in producer.getProducerByPath('/root/world/geo/houseB').iterChildren(): # 지정한 location 하위에 속한 자식 location 정보
    print (child.getFullName())

# unpack 2
knode = NodegraphAPI.GetNode('UsdIn')
NodegraphAPI.SetNodeViewed(knode, True, exclusive=True)

producer = Nodes3DAPI.GetGeometryProducer(knode)

children = []
for child in producer.getProducerByPath('/root/world/geo/houseB/Looks').iterChildren():
    children.append(child.getFullName())

for i in children:
    print (i)

# iteration
knode = NodegraphAPI.GetNode('UsdIn')
producer = Nodes3DAPI.GetGeometryProducer(knode)
producer_location = producer.getProducerByPath('/root/world/geo/houseB/Looks')


children = []
for child in producer.getProducerByPath('/root/world/geo/houseB').iterChildren():
    children.append(child.getFullName())


stack = [producer_location]

while stack:
    CHILD = stack.pop()
    CHILDREN = CHILD.iterChildren()
    print (CHILD.getFullName())
    if not CHILDREN:
        continue
    stack.extend(CHILDREN)







