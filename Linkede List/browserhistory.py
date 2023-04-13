class Url:
    def __init__(self,url,next=None,prev=None,):
        self.url= url
        self.next=next
        self.prev=prev
        self.stack=None

class BroweserHistory:
    def __init__(self,url):
        self.head=Url(url)
        self.head.stack=1
        self.tail=self.head
        self.count=1

    def visit(self,url):
        new_url=Url(url)
        self.count += 1
        new_url.stack=self.count

        current=self.tail
        new_url.prev=current
        current.next=new_url
        self.tail=new_url
        self.current=self.tail

    def back(self,steps):

        if steps>self.current.stack:
            self.current=self.head
            return self.current.url

        else :
            for i in range(steps):
                self.current=self.current.prev
            return self.current.url

    # return String


    def forward(self,steps):

        if steps>(self.count-self.current.stack):
            self.current=self.tail
            return self.current.url
        else:
            for i in range(steps):
                self.current = self.current.next
            return self.current.url

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
