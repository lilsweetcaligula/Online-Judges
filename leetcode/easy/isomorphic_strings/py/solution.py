class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Leetcode hasn't upgraded its Python judges to 3.x, however the function
        # still receives unicode strings as parameters. str.translate method in
        # Python 2.x will not work on a unicode translation table, thus we must
        # build a translation table ourselves based on char codes.
        #
        return (    t == s.translate({ ord(frm): ord(to) for frm, to in zip(s, t)})
                and s == t.translate({ ord(frm): ord(to) for frm, to in zip(t, s)}))
                
        # A cleaner Python 3.x solution would be:
        #
        # return t == s.translate(str.maketrans(s, t)) and s == t.translate(str.maketrans(t, s))
