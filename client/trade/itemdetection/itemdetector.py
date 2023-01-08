from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2

class ItemDetector:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.previousImage = None
        self.cellWidth = w/12

    def detect(self, image):

        if self.previousImage is None:
            self.previousImage = image
            return []

        # convert the images to grayscale
        grayA = cv2.cvtColor(self.previousImage, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,    cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # map to grid
        cells = []
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            mapped_x = int(x/self.cellWidth)
            mapped_y = int(y/self.cellWidth)
            mapped_w = (int(w/self.cellWidth)+1)
            mapped_h = (int(h/self.cellWidth)+1)

            cells.append((mapped_x,mapped_y, mapped_w, mapped_h))
        
        self.previousImage = image
        return cells