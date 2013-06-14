import web
import random
import math
import set_any_dimension


render2 = web.template.render('templates/')

render = web.template.render('testdirectory/')
urls = (
    '/set', 'set',
    '/town', 'town',
    '/new','new',
    '/checkcards','checkcards'
)

def printcards(board):
    testlist=[]
    for i in range(len(board.cardsonboard)):
        testlist.append(set_any_dimension.cardmapping(board.cardsonboard[i]))
    for i in range(len(testlist)):
        testlist[i] = 'static/setcards/' + str(testlist[i]) + '.JPG'
    return testlist

def printallsets(board):
    setlist = board.printsetsonboard()

    for i in range(len(setlist)):
        setlist[i] = 'static/setcards/' + str(setlist[i]) + '.JPG'
    return setlist
    

def printallsupersets(board):
    supersetlist = board.printsupersetsonboard()
    for i in range(len(supersetlist)):
        supersetlist[i] = 'static/setcards/' + str(supersetlist[i]) + '.JPG'
    return supersetlist
    
def numsupersets(board):
    return len(printallsupersets(board))/4
      
newboard = None

class set:
    def GET(self):
        global newboard
        newboard = set_any_dimension.board(4)
        newboard.dealcards(12)
        
        printboard = printcards(newboard)
        printthesets = printallsets(newboard)
        numsetsonboard = newboard.numsetsonboard()
        
        modifiedBoard = newboard
        
        
        
        return render.setweb(printboard, numsetsonboard, printthesets, newboard)
        
class checkcards:
    def GET(self):
        cardIds = web.input()
        print cardIds
        cards = []
        for i in range(3):
            cards.append(set_any_dimension.reversecardmapping(cardIds[i]))
            
            
        if set_any_dimension.isset(cards[0],cards[1],cards[2]):
            return 'YAY!!!'
        return 'NOOOO!!!'
        
class new:
    def GET(self):
        newboard.dealcards(3)
        printboard = printcards(newboard)
        printthesets = printallsets(newboard)
        numsetsonboard = newboard.numsetsonboard()
        
        
        
        return render.biggerboard(printboard, numsetsonboard, printthesets)
        
class boom:
    def GET(self):
        newboard2 = set_any_dimension.board(4)
        newboard2.dealcards(12)
        printboard = printcards(newboard2)
        printthesupersets = printallsupersets(newboard2)
        numsupersetsonboard = numsupersets(newboard2)
        
        return render.supersetweb(printboard,printthesupersets, numsupersetsonboard)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()