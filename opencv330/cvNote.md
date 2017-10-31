## Get Image:
    img = cv2.imread(imgPath[, flag])
    img = np.zeros((height, width, 3), np.uint8)

## Show Image and WaitKey:
    cv2.imshow('ImageWindow', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
