class Solution(object):
    def simplifyPath(self, path):
        stack = []
        
        for portion in path.split('/'):
            if portion == '' or portion == '.':
                continue
            elif portion == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(portion)
                
        return '/' + '/'.join(stack)