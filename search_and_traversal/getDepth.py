

root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

def getDepth(node):
    if len(node['children']) == 0:
        return 0
    else:
        maxChildDepth = 0
        for child in node['children']:
            childDepth = getDepth(child)
            if childDepth > maxChildDepth:
                maxChildDepth = childDepth
        return maxChildDepth + 1

print('Depth of tree is ' + str(getDepth(root)))