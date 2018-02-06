import math
class question(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for i in xrange(len(path)):
            if path[i] in {'.',''}:
                continue
            if path[i]== '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[i])
        return '/'+'/'.join(stack)


if __name__ == '__main__':

    inputs = '/a/./b/../../c/'
    k = question()
    inputs.strip()
    r = k.simplifyPath(inputs)
    print  'result : ',r


