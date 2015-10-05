class DListNode(object):
    def __init__(self,value=None,link=None,rev=None):
        """creates a DListNode with the specified date value,link and reversed link
        post: creates a ListNode with the specified data value, link and rev"""
        self.value=value
        self.link=link
        self.rev=rev
