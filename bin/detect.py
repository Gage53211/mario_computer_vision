import cv2 as cv
import numpy as np

THREASHOLD = 0.8

# finds first instance of item
def find_single_item (image, name): 
    """Finds single item using name provided."""

    template = cv.cvtColor(cv.imread(f'templates/{name}.png'), cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(image, template,cv.TM_CCOEFF_NORMED)
    threshold = THREASHOLD
    coords = None 
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):
        coords = pt
        return coords, template.shape
    return coords, template.shape

# finds all instances of item
def find_multiple_items (image, name):
    """Finds multiple items using name provided."""

    template = cv.cvtColor(cv.imread(f'templates/{name}.png'), cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(image, template,cv.TM_CCOEFF_NORMED)
    threshold = THREASHOLD
    loc = np.where( res >= threshold)
    coords = []

    for pt in zip(*loc[::-1]):
        coords.append(pt)
    return coords, template.shape

