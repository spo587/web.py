import math
import random


## this is set up to play setgames of different types corresponding to different numbers of card attributes or different 'dimensions'

## the function toward the bottom, "deadboards", is the one that doesn't seem to quite be working, but it's a problem with a function in
## board class (detectsetandremoveadvanced). what the d???? it works really well for a while, but then a random game
## always derails it. lil help??

class card(object):
    def __init__(self,attributes):
        '''attributes is a tuple of length=card dimension'''
        self.attributes=attributes
    def getdimension(self):
        return len(self.attributes)
    def printcard(self):
        return self.attributes

def isset(card1,card2,card3):
    ans=0
    for i in range(len(card1.printcard())):
        if (card1.printcard()[i]+card2.printcard()[i]+card3.printcard()[i])%3==0:
            ans+=1
    return ans==len(card1.printcard())
    
def issuperset(card1,card2,card3,card4):
    assert len(card1.printcard()) == 4
    for i in range(4):
        num1 = card1.printcard()[i]
        num2 = card2.printcard()[i]
        num3 = card3.printcard()[i]
        num4 = card4.printcard()[i]
        if num2 == num1 and num3 == num1:
            if num4 != num1:
                return False
        elif num2 == num1 and num3 != num1:
            if num4 == num1 or num4 == num3:
                return False
        elif num2 != num1 and num3 == num1:
            if num4 != num2:
                return False
        elif num2 != num1 and num3 == num2:
            if num4 != num1:
                return False
        elif num2 != num1 and num3 != num2 and num3 != num1:
            if num4 != num3:
                return False
    return True
    

    
    

def settype((card1,card2,card3)):
    '''a function to determine the number of differences in a given a set'''
    assert isset(card1,card2,card3) is True
    numdiffs=0
    for i in range(3):
        if card1.attributes[i]!=card2.attributes[i]:
            numdiffs+=1
    return numdiffs
    
##card1=card((1,3,2))
##card2=card((0,2,2))
##card3=card((2,1,2))
##
##print settype((card1,card2,card3))

def twodmastercardlist():
    '''creates a list of all nine 9 two dimensional cards'''
    mastercardlist=[]
    for i in range(3):
        for j in range(3):
            mastercardlist.append(card((i,j)))
    return mastercardlist

##print twodmastercardlist()   
    
def threedmastercardlist():
    '''list of all 27 three d cards'''
    threedmastercardtuple=[]
    for i in range(3):
        for j in range(3):
            for t in range(3):
            
                threedmastercardtuple+=[card((i,j,t)),]
    return threedmastercardtuple

def fourdmastercardlist():
    '''list of all 81 4-d cards'''
    fourdmastercardtuple=[]
    for i in range(3):
            for j in range(3):
                for t in range(3):
                    for n in range(3):
                        fourdmastercardtuple+=[card((n,t,j,i)),]
    #random.shuffle(fourdmastercardtuple)
    return fourdmastercardtuple


def cardmapping(card):
    '''converts each card to a number 0-80'''
    return card.attributes[0] + 3*card.attributes[1] + 9*card.attributes[2] + 27*card.attributes[3]

## build the image list mapping
def print_src_list():
    src_list=[]
    for card in fourdmastercardlist():
            src_list.append(cardmapping(card))
            
    return src_list

##print print_src_list()

## global list 'dimensionlist' is just a list with all the mastercardlists in it. there's certainly
## a better way to do this, but it's what i came up with
dimensionlistdefault = [twodmastercardlist(),threedmastercardlist(),fourdmastercardlist()]

def threecardcombos(numcardsonboard):
    '''returns list of tuples for all possible threecard combinations given a number of cards, where each tuple is a possible combination of three cards
    numcardsonboard=int
    returns: list of tuples'''
    listofthreecardcombos=[]
    for i in range(numcardsonboard-2):
        for j in range(i+1,numcardsonboard-1):
            for k in range(j+1,numcardsonboard):
                listofthreecardcombos.append((i,j,k))
    return listofthreecardcombos


def fourcardcombos(numcards):
    '''samesies for four cards. we'll want this for superset'''
    listoffourcardcombos=[]
    for i in range(numcards-3):
        for j in range(i+1,numcards-2):
            for k in range(j+1,numcards-1):
                for t in range(k+1,numcards):
                    listoffourcardcombos.append((i,j,k,t))
    return listoffourcardcombos






class board(object):
    def __init__(self,dimension,dimensionlist=dimensionlistdefault,cardsonboard=None,cardsremoved=None):
        ## each of the inputs is a list, but except for the dimension
        ## each game board will start with empty lists
        ## dimensionlist will be a global list that we'll input
        if cardsonboard == None:
            self.cardsonboard = []
        
        if cardsremoved == None:
            self.cardsremoved = []
        self.dimension=dimension
        self.dimensionlist=dimensionlist
        self.mastercardlist=dimensionlist[self.dimension-2]
        self.cardlist=[]
        ## shuffle the cardlist at the beginning of each game
        for i in range(len(self.mastercardlist)):
            self.cardlist.append(self.mastercardlist[i])
        random.shuffle(self.cardlist)
              
        
        self.cardsremoved=cardsremoved
    def dealboard(self,numcards):
        '''a random deal that adds numcards cards to the existing board'''
        for i in range(numcards):
            selectedcard=random.choice(self.cardlist)
            self.cardsonboard.append(selectedcard)
            self.cardlist.remove(selectedcard)
   
    def clearboard(self):
        self.cardsonboard=[]

    def dealboardnonrandom(self,cards):
        '''adds the cards in the list to the existing board
        cards=list of cards'''
        self.cardsonboard+=cards
        

    def dealnextcards(self,numcards):
        '''deals the next cards in the cardlist to the existing board'''
        for i in range(numcards):
            newcard=self.cardlist[0]
            
            self.cardsonboard.append(newcard)
            self.cardlist.remove(newcard)
       
    def isthereaset(self):
        for t in threecardcombos(len(self.cardsonboard)):
            if isset(self.cardsonboard[t[0]],self.cardsonboard[t[1]],self.cardsonboard[t[2]]) is True:
                return True
        return False
        
    ## take away the first set found
    def detectsetandremove(self):
        for t in threecardcombos(len(self.cardsonboard)):

            card1=self.cardsonboard[t[0]]
            card2=self.cardsonboard[t[1]]
            card3=self.cardsonboard[t[2]]
            
            if isset(card1,card2,card3) is True:
                
                
                
                ## uncomment print statements to see the game as it progresses in
                ## the playgame() function below
##                print 'set!'
##                print card1.printcard()
##                print card2.printcard()
##                print card3.printcard()
                self.cardsonboard.remove(card1)
                self.cardsonboard.remove(card2)
                self.cardsonboard.remove(card3)
                self.cardsremoved+=[card1,card2,card3,]
                
                break

    def detectsetandremoveadvanced(self):
        '''removes the set of lowest number of differences instead of the first set detected'''
        i=1
        while i<=self.dimension:
            for t in threecardcombos(len(self.cardsonboard)):
                card1=self.cardsonboard[t[0]]
                card2=self.cardsonboard[t[1]]
                card3=self.cardsonboard[t[2]]
               
                
                if isset(card1,card2,card3) is True and settype((card1,card2,card3))==i:
                    #print 'set!'
##                    print card1.printcard()
##                    print card2.printcard()
##                    print card3.printcard()
                    self.cardsonboard.remove(card1)
                    self.cardsonboard.remove(card2)
                    self.cardsonboard.remove(card3)
                    self.cardsremoved+=[card1,card2,card3,]
                    return 'not deadboard'
                
            i+=1
                
    ## find the number of sets on the board (without removal)
    def numsetsonboard(self):
        ans=0
        for t in threecardcombos(len(self.cardsonboard)):
            if isset(self.cardsonboard[t[0]],self.cardsonboard[t[1]],self.cardsonboard[t[2]]) is True:
                ans+=1
        return ans
    ## this might be unnecessary

    def printsetsonboard(self):
        listofsets = []
        for t in threecardcombos(len(self.cardsonboard)):
            if isset(self.cardsonboard[t[0]],self.cardsonboard[t[1]],self.cardsonboard[t[2]]) is True:
                # print 'set!'
                #                                                 print self.cardsonboard[t[0]].printcard()
                #                                                 print self.cardsonboard[t[1]].printcard()
                #                                                 print self.cardsonboard[t[2]].printcard()
                listofsets += [cardmapping(self.cardsonboard[t[0]]),cardmapping(self.cardsonboard[t[1]]),cardmapping(self.cardsonboard[t[2]]),]
        return listofsets
    
    def printsupersetsonboard(self):
        listofsupersets = []
        for t in fourcardcombos(len(self.cardsonboard)):
            
            if issuperset(self.cardsonboard[t[0]],self.cardsonboard[t[1]],self.cardsonboard[t[2]],self.cardsonboard[t[3]]) is True:
                
                listofsupersets += [cardmapping(self.cardsonboard[t[0]]),cardmapping(self.cardsonboard[t[1]]),cardmapping(self.cardsonboard[t[2]]),cardmapping(self.cardsonboard[t[3]]),]
        return listofsupersets
    ## what cards are on the current board
    def printboard(self):
        for i in range(len(self.cardsonboard)):
            print self.cardsonboard[i].printcard()

    
    def allpossfourcarddealstwod(self):
        '''a function to test all the possible deals for a two d board'''
        l=fourcardcombos(3**2)
        ans=0
        tries=0
        
        for t in l:
             
            tries+=1
            self.clearboard()
            
            self.dealboardnonrandom([self.cardlist[t[0]],self.cardlist[t[1]],self.cardlist[t[2]],self.cardlist[t[3]]])
            
            if self.isthereaset() is True:
                 ans+=1

        return (ans,tries)

    
testboard = board(4)
testboard.dealboard(12)
print testboard.printsupersetsonboard()  
         
def randomdealdeadboards(numcards,numtrials,dimension,dimensionlist=dimensionlistdefault):
    
    numdeadboards=0
    for i in range(numtrials):
        #print 'new board'
        board2=board([],[],dimension,dimensionlist)
        #print board2.cardlist
        board2.dealboard(numcards)
        #board2.printboard()
        
        if board2.isthereaset() is False:
            #print 'deadboard!!'
            numdeadboards+=1
            print board2.printboard()
    return numdeadboards

##board1=board([],[],2,dimensionlist)
##for i in range(len(board1.cardlist)):
##    print board1.cardlist[i].printcard()
##board1.dealnextcards(4)
##print board1.cardsonboard
##print board1.printboard()
##
##
##print board1.allpossfourcarddealstwod()
##
##
##print randomdealdeadboards(9,10000,3,dimensionlist)

def playgame(dimension,detectiontype):
    '''function to play a game with cards of specified dimension and detection type
    dimension=int
 
    detectiontype=str: 'simple' or 'complex
    uncomment print statements to see the game as it goes. leave them in to return only the number
    of deadboards'''
    numsets=0
    deadboards=0
    board1=board(dimension)
    board1.dealnextcards(dimension*3)
    board1.printboard()
    print 'board=',board1.printboard()
    while len(board1.cardlist)>=0:
        
        if board1.isthereaset() is True:
            
            if detectiontype=='simple':
                board1.detectsetandremove()
            elif detectiontype=='complex':
                board1.detectsetandremoveadvanced()
            numsets+=1
            print numsets
            if len(board1.cardlist)>=3:
                board1.dealnextcards(3)
            print 'board=', board1.printboard()
            
            
        elif len(board1.cardlist)>=3:
            deadboards+=1
            print 'deadboard'
            board1.dealboard(3)
            print 'new board=', board1.printboard()
            
            
        else:
            print 'game over!'
            print 'total number of sets in game=',numsets
            break
##    
    print 'game over!'
    print 'final board=',board1.printboard()
    if len(board1.cardsonboard)>=12:
        deadboards+=1
    print len(board1.cardsonboard)
    print len(board1.cardsremoved)
    print len(board1.cardlist)
    print 'number of sets=',numsets
    print 'number of deadboards=',deadboards
    return deadboards

#print playgame(4,dimensionlist,'complex')

def deadboards(numgames,detectiontype):
    '''returns a list with the number of deadboards in a number of games of a certain type'''
    listofdeadboards=[]
    for i in range(numgames):
        listofdeadboards.append(playgame(4,detectiontype))
        ## i've left the print statement in below at an attempt to debug...you'll see what happens
        ## the program works for a while, then it just stops all of a sudden
        print listofdeadboards
    return listofdeadboards

def average(x):
    return sum(x)/float(len(x))

#print average(deadboards(100,'simple'))

## the function below is the one that doens't work. i can't figure out why. 
##print average(deadboards(100,'complex'))


































#def playsimultaneousgames(dimension,dimensionlist,gametypes=['simple','complex']):
    
    





##for card in mastercardlist:
##    print card.printcard()
##
##print mastercardlist[0].printcard()
##print mastercardlist[2].printcard()

##list1=[]
##j=0
###for j in range(0,79):
##for i in range(j+1,26):
##    for t in range(i+1,27):
##        if isset(mastercardlist[j],mastercardlist[i],mastercardlist[t]) is True:
##            listtemp=[j,i,t]
##            listtemp2=[mastercardlist[j].printcard(),mastercardlist[i].printcard(),mastercardlist[t].printcard()]
##            listtemp.sort()
##            listtemp2.sort()
##            print listtemp
##            print listtemp2
##            
##                
##            list1.append(listtemp)
##print len(list1)








# the old isset function
##for i in range(3):
##        if card1.attributes()[i]==card2.attributes()[i]:
##            if card1.attributes()[i]!=card3.attributes()[i]:
##                return False
##        else:
##            if card2.attributes()[i]==card3.attributes()[i] or card3.attributes()[i]==card1.attributes()[i]:
##                return False
