

root = {'name': 'Alice', 'children': [{'name': 'Bob', 'children':
[{'name': 'Darya', 'children': []}]}, {'name': 'Caroline',
'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo',
'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred',
'children': []}]}]}

def find8LetterName(node):
    print(' Visiting node ' + node['name'] + '...')
    print('Checking if ' + node['name'] + ' is 8 letters...')
    if len(node['name']) == 8:
        return node['name']
    if len(node['children']) > 0:
        for child in node['children']:
            returnValue = find8LetterName(child)
            if returnValue != None:
                return returnValue

    print('Checking if ' + node['name'] + ' is 8 letters...')
    if len(node['name']) == 8: return node['name'] # БАЗОВЫЙ СЛУЧАЙ
    return None # БАЗОВЫЙ СЛУЧАЙ


print('Found an 8-letter name: ' + str(find8LetterName(root)))