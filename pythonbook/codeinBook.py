class stackcal:
    stack=[]
    def push(self,stack):

        stack.appened(raw_input("plz enter your content "))

    def pop(self,stack):
        if len(stack)==0:
            print "can not remove!!!"
        else:
           stack.pop()
           print "removed  yeah"
    def showstack(self,stack):
        print stack
    def showmenu(self):
        entercontent="""
        plz enter number of below choice:
        1:push
        2:pop
        3.show
        4:quit"""

        while True:
             while True:
                 choice=raw_input(entercontent).strip()[0].lower()
                 if choice not in "123":
                     print "wrong input"
                 else:
                     break
                 if choice=='4':
                     break
    if __name__=="__main__":
        showmenu()
