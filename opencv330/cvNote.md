Opencv Version:
    print "Opencv Version:", cv2.__version__
    print __file__

Get Image
    img = cv2.imread(imgPath)
    img = np.zeros((height, width, 3), np.uint8)

Show Image and WaitKey:
    cv2.imshow('ImageWindow', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

Open Camera:

    cap = cv2.VideoCapture(0)
    print "cap.isOpened() : ", cap.isOpened()

    while cap.isOpened():
        _ret, frame = cap.read()
        frameResized = cv2.resize(frame, (320, 240))
        cv2.imshow('frame', frameResized)
        if 27 == cv2.waitKey(33) & 0xff:
            break

    cap.release()
    cv2.destroyAllWindows()

ROI - Rect of Image
    img = cv2.imread("files/f35/f35-night.jpg", cv2.IMREAD_UNCHANGED)
    img[20:200, 20:30] = (255, 5, 5)
    img[50,50] = (255,255,255)

2D Drawings:

    # get Image
    img = cv2.imread("files/f35/f35_1014_487.jpg")

    # Draw a line
    cv2.line(img, (10,30), (900,30), (255,0,0), 1)

    # a rectangle
    cv2.rectangle(img, (50,50), (150, 100), (0,0,255), 2)

    # a circle
    cv2.circle(img, (150,100), 55, (0,255,0), 1)

    # put text on Image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "F22 Fighter", (250, 50), font, 0.6, (200,0,100), 1, cv2.LINE_AA)

    # an ellipse
    cv2.ellipse(img, (500, 300), (120, 60), 0, 0, 360, (255,0,0), 6)

Put Logo On an Image:
    image = cv2.imread("files/f35/f35-night.jpg")
    logo = cv2.imread("files/logos/logo.png")

    rows, cols, channels = logo.shape
    roi = image[0:rows, 0:cols]

    grayLogo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    _ret, mask = cv2.threshold(grayLogo, 200, 255, cv2.THRESH_BINARY_INV)
    maskInv = cv2.bitwise_not(mask)

    cv2.imshow('logo', logo)
    cv2.imshow('mask', mask)
    cv2.imshow('maskInv', maskInv)

    logo_foreground = cv2.bitwise_and(logo, logo, mask=mask)
    roi_background  = cv2.bitwise_and(roi,  roi,  mask=maskInv)

    cv2.imshow('logo_foreground', logo_foreground)
    cv2.imshow('roi_background', roi_background)

    dst = cv2.add(roi_background, logo_foreground)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()

