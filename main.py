# Saper game in Python3 using tkinter
# by Konrad Ungeheuer

# Copyright (c) 2017-2023 Konrad Ungeheuer

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import profile


from tkinter import *
from tkinter import ttk
import random

class GameWindow(object):
    '''
    Prepare FileForm and HelpForm, create GameFrame
    '''
    #game state (Player can be alive or he had found the mine already :P he may won eventualy too ;]) and other strings in one place
        #those are intended to be Constant#
    WIN     = ':]'
    LOST    = 'X['
    PLAY    = ':)'
    START   = ''
    TKSAPER = 'tksaper'
    RIGHTS = '''
tksaper
Demo project in python3
Author: Konrad Ungeheuer
Mail: konrad.ungeheuer@gmail.com
'''

    def gameState(self, state, posX = None, posY = None):
        '''seting statusOfGame to given state, changing description, stopping game'''
        assert state in (GameWindow.WIN, GameWindow.LOST, GameWindow.PLAY, GameWindow.START)
        self.statusOfGame = state

        if self.statusOfGame == GameWindow.START:
            pass

        if self.statusOfGame == GameWindow.WIN :
            self.newGame.flipAll()

        if self.statusOfGame == GameWindow.LOST:
            self.newGame.flipAll()

        if self.statusOfGame == GameWindow.PLAY:
            self.newGame.flipSome(posX, posY)

        self.master.title(GameWindow.TKSAPER + ' ' + state)

    def startGame(self, sizeX=10, sizeY=10, mineNumber=40):
        '''Starting the game and changing any statusOfGame to PLAY, destroy widgets in GameWindow and proceed with new one's'''
        
        assert min(sizeX, sizeY, mineNumber) > 1
        self.gameFrame.destroy()#first gameFrame will be destroyed and then we create it again and inside we put GameFrame internal ttk.Frame
        
        self.gameFrame = ttk.Frame(self.master)#re-initialize
        self.gameFrame.grid(row = 0, column = 0, sticky = (N, S, W, E))

        self.newGame = GameFrame(self.gameFrame, self, sizeX, sizeY, mineNumber)
        #player is alive again
        self.gameState(GameWindow.START)
        
    def helpGameDestroy(self):
        self.isHelpOpen = False
        self.helpWin.destroy()

    def helpGame(self):
        if self.isHelpOpen == True:#prewent poping up more than one window
            return
        self.helpWin = Toplevel(self.master)
        self.frame = ttk.Frame(self.helpWin)
        self.helpString = StringVar()
        self.helpString = GameWindow.RIGHTS
        self.label = ttk.Label(self.frame, text = self.helpString)
        self.okButton = ttk.Button(self.frame, text = 'OK', command=self.helpGameDestroy) 
        self.frame.pack()
        self.label.pack()
        self.okButton.pack()
        self.okButton.focus()
        self.isHelpOpen = True

    def exitGame(self):
        self.master.quit()
    
    def __init__(self, master):
        
        #self.path = os.path.dirname(__file__)

        #now we load all needed pictures, they are listed one by one to prevent doubt when the script is 
        self.pictureList = []#will hold references to pictures, order is important
        
        try:
            self.pictureList.append(PhotoImage(file='g0.gif'))
            self.pictureList.append(PhotoImage(file='g1.gif'))
            self.pictureList.append(PhotoImage(file='g2.gif'))
            self.pictureList.append(PhotoImage(file='g3.gif'))
            self.pictureList.append(PhotoImage(file='g4.gif'))
            self.pictureList.append(PhotoImage(file='g5.gif'))
            self.pictureList.append(PhotoImage(file='g6.gif'))
            self.pictureList.append(PhotoImage(file='g7.gif'))
            self.pictureList.append(PhotoImage(file='g8.gif'))
            self.pictureList.append(PhotoImage(file='gmine.gif'))
            self.pictureList.append(PhotoImage(file='gwrong.gif'))
            self.pictureList.append(PhotoImage(file='gboom.gif'))
            self.pictureList.append(PhotoImage(file='gmark.gif'))
        except:
            quit('Can\'t load image(s)')

            #root
        self.master=master
        
        self.isHelpOpen = False
        
        #game state initialization, player start alive
        #self.gameState(GameWindow.PLAY)
        
        #game menu's

        #create a main menu for game, takes root as a master
        self.master.option_add('*tearOff', False)#trick preventing menu tearing off
        self.Bar = Menu(self.master)    #main menu bar of root window

        self.File = Menu(self.Bar)  #start menu
        self.Help = Menu(self.Bar)  #help menu

        self.Bar.add_cascade(menu = self.File, label='File')
        self.Bar.add_cascade(menu = self.Help, label='Help')

        self.File.add_command(label='Exit', command=self.exitGame)    #help menu item "Exit"
        self.File.add_command(label='Start 8x8 - 5'   , command=lambda:self.startGame(8,  8,  5))#start game 8x8 with 5 mines
        self.File.add_command(label='Start 10x10 - 20', command=lambda:self.startGame(10, 10, 20))
        self.File.add_command(label='Start 15x15 - 30', command=lambda:self.startGame(15, 15, 30))

        self.Help.add_command(label='Help', command=self.helpGame)    #help menu item "Help"

        #set up a menu for root
        self.master.config(menu=self.Bar)

        #typical frame setup
        self.gameFrame = Frame(self.master)
        self.gameFrame.grid(row = 0, column = 0)#, sticky = (N, S, W, E))


        self.Title = ttk.Label(self.gameFrame, text = 'Choose the board size')
        self.Title.grid(column=0, row=0, columnspan=2)

        #starting buttons
        self.Button = ttk.Button(self.gameFrame, text = 'Start 8x8 - 5',   command=lambda:self.startGame(8,  8,  5))#start game 8x8 with 5 mines
        self.Button.grid(column=0, row=1, sticky=(N, S, W, E))

        self.Button = ttk.Button(self.gameFrame, text = 'Start 10x10 - 20', command=lambda:self.startGame(10, 10, 20))#--||--
        self.Button.grid(column=1, row=1, sticky=(N, S, W, E))

        self.Button = ttk.Button(self.gameFrame, text = 'Start 15x15 - 30', command=lambda:self.startGame(15, 15, 30))#--||--
        self.Button.grid(column=0, row=2, sticky=(N, S, W, E))

        #self.Button = ttk.Button(self.gameFrame, text = 'Custom size',      command=self.startGame)#Custom size and mine number-not working yet
        #self.Button.grid(column=1, row=2, sticky=(N, S, W, E))
        
class GameFrame(object):
    '''
    Prepare game basing on data from FileForm and react on GameState change
    '''
    def __init__(self, master, window, sizeX, sizeY, mineNumber):
        assert 0 < mineNumber <= sizeX * sizeY and sizeX > 0 and sizeY > 0 # sanity check
        self.master = master
        self.window = window
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.mineNumber = mineNumber
        self.blankQuantity = self.sizeX*self.sizeY - self.mineNumber # using this number we going to calculate end game conditions
        self.counter = self.blankQuantity # we will distract from this one until self.mineNumber will be reached
        self.frame = Frame(self.master)
        self.frame.grid(column=0, row=0, sticky=(N, S, W, E))
        mineLocation = random.sample(range(sizeX*sizeY), k = self.mineNumber)
        #initialization of arrays needed for calcualteNeighbours and flip...

        self.mineArray = [[] for _ in range(self.sizeX)]
        iterator = 0
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                self.mineArray[i].append(iterator in mineLocation)
                iterator += 1
                
        self.gameArray = [[] for _ in range(self.sizeX)]

        for i in range(self.sizeX):
            for j in range(self.sizeY):
                self.gameArray[i].append(GameButton(self.master, self, i, j, self.mineArray[i][j], self.calculateNeighbours(i, j)))

    def neighbourIndexGen(self, posX, posY, sizeX, sizeY):
        '''
        Generate cooridinates of neighbouring cells(fields) all 8 of them.
        Yields tuple of two integers (x, y).
        '''
        #we start from '12'h and procedd clokwise, bacause of no size assumptions we going to check everything
        eightList = ((posX    ,posY - 1),(posX + 1,posY - 1),(posX + 1,posY    ),(posX + 1,posY + 1),(posX   ,posY + 1),(posX - 1,posY + 1),(posX - 1,posY    ),(posX - 1,posY - 1))

        for indexXY in eightList:
            if indexXY[0] >=0 and indexXY[0] < sizeX  and   indexXY[1] >=0 and indexXY[1] < sizeY:
                yield indexXY
           
    def calculateNeighbours(self, posX, posY):
        '''
        Will calculate number of mines in 8 positions touching posX, posY position
        '''
        if self.mineArray[posX][posY]:
            return 1
        returnVal = 0
        #we start from '12'h and procedd clokwise, bacause there is no size assumptions we are going to check everything
        for coordinates in self.neighbourIndexGen(posX, posY, self.sizeX, self.sizeY):
            if self.mineArray[coordinates[0]][coordinates[1]]:
                returnVal+=1
        return returnVal

    def zeroNeighbour(self, posX, posY):
        if self.gameArray[posX][posY].getNeighbours() == 0:
            return True
        
        if self.gameArray[posX][posY].getMine():
            return False

        for coordinates in self.neighbourIndexGen(posX, posY, self.sizeX, self.sizeY):
            if self.gameArray[coordinates[0]][coordinates[1]].getNeighbours() == 0: return True
        return False

    def flipSome(self, posX, posY):
        """Flip field -> (posX, posY) if it has empty neighbour"""
        if self.zeroNeighbour(posX, posY):
            self.gameArray[posX][posY].autoFlip()
            if self.gameArray[posX][posY].getNeighbours() == 0:
                for coordinates in self.neighbourIndexGen(posX, posY, self.sizeX, self.sizeY):
                    if self.gameArray[coordinates[0]][coordinates[1]].getActive() and self.zeroNeighbour(coordinates[0], coordinates[1]):
                        self.flipSome(coordinates[0], coordinates[1])

    def flipAll(self):
        for col in self.gameArray:
            for j in col:
                j.autoFlip()

    def endGameCheck(self):
        correctMarks = 0
        for col in self.gameArray:
            for item in col:
                if item.isOk():
                    correctMarks += 1
        if correctMarks == self.mineNumber:
            return True
        else:
            return False

class GameButton(object):
    '''
    Draw itself using data from GameArray can change GameState, it's Frame because it can display label or button.
    '''
    #labels - later to be changed to pictures
    N0    = ' '#for zero we left blank label - picture
    N1    = '1'
    N2    = '2'
    N3    = '3'
    N4    = '4'
    N5    = '5'
    N6    = '6'
    N7    = '7'
    N8    = '8'#bigest possible number
    MINE  = '*'#mine fliped ... 
    WRONG = 'X'#piece marked wrong
    FINE  = 'V'#piece marked right
    MARK  = 'P'#marked piece
    LABELLIST = (N0, N1, N2, N3, N4, N5, N6, N7, N8, MINE, WRONG, FINE, MARK)#this list will make it easier, we call labels - pictures using position in list

    def __init__(self, master, game, posX, posY, mine, neighbours):
        #remmember it's position

        self.master = master
        self.game = game
        GameButton.LABELLIST = self.game.window.pictureList
        self.posX = posX
        self.posY = posY
        self.mine = mine#if =True then posX, posY has mine =False otherwise
        self.mark = False
        self.active = True #if =True then it is not fliped yet
        self.neighbours = neighbours#number of mines surronuding posX, poxY like in oryginall saper
        if self.mine:
            self.neighbours = 9# this will simplify autoFlip method and usage of LABELLIST

        self.frame = ttk.Frame(self.master)
        self.frame.grid(column=self.posX, row=self.posY, sticky=(N, S, W, E))
        self.button = Button(self.frame, image=GameButton.LABELLIST[0], command=self.playerFlip, width=32, height=32)
        self.button.bind('<3>', lambda e :self.setMark())
        self.button.grid(column = 0, row = 0)

    def setMark(self):#here we need to check is this posible or is the game ended !
        if self.mark:
            self.mark = False
            self.button['image'] = GameButton.LABELLIST[0]
        else:
            self.mark = True
            self.button['image'] = GameButton.LABELLIST[12]
            self.isGameFinished()

    def isGameFinished(self):
        if self.game.counter == 0:
           if self.game.endGameCheck():
               self.game.window.gameState(GameWindow.WIN)

    def getActive(self):
        return self.active

    def getNeighbours(self):
        return self.neighbours

    def autoFlip(self):#the only function fliping buttons
        if not self.active:#if button is inactive (flipped already) do nothing
            return
        self.active = False
            #now we set proper label(for now)
        self.game.counter -= 1#we count fliped buttons
        self.isGameFinished()
        if self.mark:
            if self.mine:
                index = 11#this index will be used to show proper label - picture from GameButton.LABELLIST
            else:
                index = 10
        else:
            index = self.neighbours
        self.label = ttk.Label(self.frame, image=GameButton.LABELLIST[index])
        self.label.grid(column=0, row=0)
        self.isGameFinished()

    def isOk(self):#if mine is marked isOk() will return True
        return self.mark and self.mine and self.active

    def playerFlip(self):
        if self.mine and not self.mark:
            self.game.window.gameState(GameWindow.LOST)
        else:
            if  not self.mark:
                self.game.window.gameState(GameWindow.PLAY, self.posX, self.posY)
                self.autoFlip()
        self.isGameFinished()

    def getMine(self):
        return self.mine


def main():
    root=Tk()
    root.title('tksaper')
    root.resizable(False, False)
    newGame=GameWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    #profile.run("main()")