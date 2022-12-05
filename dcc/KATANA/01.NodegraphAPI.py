from __future__ import print_function

from Katana import NodegraphAPI

nodes_name = NodegraphAPI.GetAllNodes(includeDeleted=False, sortByName=True)
nodes_type = NodegraphAPI.GetAllNodesByType('Alembic_In', includeDeleted=False, sortByName=True)
node_type = NodegraphAPI.GetNodeTypes() # 내장 된 모든 노드 Node 출력

NodegraphAPI.GetAllSelectedNodes()
NodegraphAPI.GetViewNodes() # 현재 뷰모드 혹은 에디팅 되어져 있는 노드 get
NodegraphAPI.getChildren() # 하위 노드 get 

nodes = NodegraphAPI.GetNode('NetworkMaterialCreate')

def get_scene_nodes():
    nodes = []
    knodes = NodegraphAPI.GetAllNodes(includeDeleted=False, sortByName=True)
    for knode in knodes:
        nodes.append(knode.getName())
    return nodes

scene_nodes = get_scene_nodes()
print (scene_nodes)

surface_node = NodegraphAPI.GetNode('PxrSurface')

node_attr = surface_node.getAttributes()
node_param = surface_node.get



for key, value in node_type.items():
    print(key, value)

surface_node.getParameter('name').getValue(0)
surface_node.getParameter('nodeType').getValue(0)
surface_node.getParameter('parameters').getChildren()
surface_node.getParameter('publicInterface').getChildren()

NodegraphAPI.GetNode('PrmanShadingNode').getParameters().getChildren()



from Katana import NodegraphAPI
from Katana import Nodes3DAPI


node = NodegraphAPI.GetNode('UsdIn')
root_prod = Nodes3DAPI.GetGeometryProducer(node)

root_prod.getFullName()
root_prod.getProducerByPath(LOCATION)



Nodes3DAPI.GetGeometryProducer
Nodes3DAPI.GetRenderProducer




# root_producer = producer.getRootProducer()


node = NodegraphAPI.GetNode('UsdIn')
root_prod = Nodes3DAPI.GetGeometryProducer(node)




grpAttr = root_prod.getAttribute('info') # GROUP ATTRIBUTE ## 어트리뷰트 쪽 쿼리 말고 다른 쪽도 갖고오자
strAttr = root_prod.getAttribute('info.usdLoader') # STRING ATTRIBUTE




