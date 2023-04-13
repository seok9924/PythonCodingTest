class ListNode(object):
    def __init__(self,val=0,next=None,prev=None):
        self.val= val
        self.next=next
        self.prev=prev


class BroweserHistory(object):
    def __init__(self,homepage):
        self.head= self.current= ListNode(val=homepage)


    def visit(self,url):
        self.current.next=ListNode(val=url,prev=self.current)
        self.current=self.current.next
        return None


    def back(self,steps):
        while steps>0 and self.current.prev !=None:
            steps-=1
            self.current=self.current.prev
        return self.current.val


    # return String


    def forward(self,steps):

        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val

    # return String

bs=BroweserHistory('leetcode.com')
bs.visit("google.com")
bs.visit("facebook.com")
bs.visit("youtube.com")


bs.back(1)
bs.back(1)
bs.fowrad(1)
bs.visit("linkinpark")
bs.fowrad(2)
bs.back(2)
bs.back(7)

## visit 했을 때 앞에 다 날려야하는데  흠
