from itemdetection.itemdetector import ItemDetector
import cv2

class Trader:

    itemDetector = ItemDetector(0,0,890,380)
    rows = 5
    cols = 12
    cellWidth = 75 

    def __init__(self):
        return


    def trade(self, given, expectedReceived):

        # drop bot stuff


        # assert the received stuff is valid

        img1 = cv2.imread("img1.png")
        self.itemDetector.detect(img1)
        currentReceived = 0
        currentGrid = [[0]*self.cols for i in range(self.rows)]
        
        while expectedReceived != currentReceived:
            img2 = cv2.imread("img2.png")
            cells = self.itemDetector.detect(img2)
            if len(cells) == 0:
                continue

            for (x,y,w,h) in cells :
                # todo, get content of the cell
                currentGrid[y][x] = 1
                print(currentGrid)





trader = Trader()
trader.trade(10,20)
