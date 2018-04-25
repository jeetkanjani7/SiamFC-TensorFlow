# import the necessary packages
import argparse
import cv2

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that           # the cropping operation is finished
        refPt.append((x, y))
        cropping = False

        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
       
        file.write('{},{},{},{}\n'.format(refPt[0][0],refPt[0][1], refPt[1][0]- refPt[0][0], refPt[1][1] - refPt[0][1] ))
        
        print('{},{}'.format(refPt[0],refPt[1])) #refPt[1][0]- refPt[0][0], refPt[1][1] - refPt[0][1]))
        
        cv2.imshow("image", image)

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#args = vars(ap.parse_args())

file = open('./groundtruth.txt', 'w+')

# load the image, clone it, and setup the mouse callback function
for i in range(1,20):
    cv2.namedWindow("image")
    image = cv2.imread('./%04d.jpg'%i)
    print('./%04d.jpg'%i)
  #  clone = image.copy()
    
    cv2.setMouseCallback("image", click_and_crop)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

       
    # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()

    # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
    next_key = cv2.waitKey(1) & 0xFF
    if next_key == ord('q'):
        break
    else:
        cv2.destroyAllWindows()
        continue
    
      #  if len(refPt) == 2:
        #    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        #    cv2.imshow("ROI", roi)
        #    cv2.waitKey(0)
    
file.close()