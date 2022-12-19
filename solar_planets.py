import cv2

img = cv2.imread("solar-system.jpg")

#text for sun
cv2.putText(img,
            "Sun",
            (60,60),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=2,
            color=(255,255,255)
            )

#text for mercury
cv2.putText(img,
            "Mercury",
            (120,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for venus
cv2.putText(img,
            "Venus",
            (180,260),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for earth
cv2.putText(img,
            "Earth",
            (300,160),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for mars
cv2.putText(img,
            "Mars",
            (390,260),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for jupiter
cv2.putText(img,
            "Jupiter",
            (550,50),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for saturn
cv2.putText(img,
            "Saturn",
            (800,320),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )
    
#text for uranus
cv2.putText(img,
            "Uranus",
            (960,130),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

#text for neptune
cv2.putText(img,
            "Neptune",
            (1120,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

cv2.imshow("Solar System" ,img)

cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)