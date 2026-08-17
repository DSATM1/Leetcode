class Solution(object):
    def defangIPaddr(self, address):
        ans = ""
        for i in address:
            if i != ".":
                ans+=i
            else:
                ans+="[.]"
        return ans 
        """
        :type address: str
        :rtype: str
        """
        