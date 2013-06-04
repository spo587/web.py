import web
import random
import math
import set_any_dimension


render2 = web.template.render('templates/')

render = web.template.render('testdirectory/')
urls = (
    '/boom', 'boom',
    '/town', 'town',
    '/new','new'
)



firstboard = set_any_dimension.board(4)

firstboard.dealboard(12)


numsetsonfirstboard = firstboard.numsetsonboard()


print shouldbe12, 'should be 12'

print numsetsonfirstboard
    
    
def printcards(board):
    testlist=[]
    for i in range(12):
        testlist.append(set_any_dimension.cardmapping(board.cardsonboard[i]))
    for i in range(len(testlist)):
        testlist[i] = 'static/setcards/' + str(testlist[i]) + '.JPG'
    return testlist
    
        

class town:
    def GET(self):
        newboard = board(4)
        newboard.dealboard(12)
        printboard = printcards(newboard)
        numsetsonboard = newboard.numsetsonboard()
        
        
    
        
        s = '\<img src=\'static/setcards/{0}.JPG\' /\>'
        
        
        return render.setweb(printboard, numsetsonboard)
        
                

    

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()