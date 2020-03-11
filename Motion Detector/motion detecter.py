import cv2
first_frame=None
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:#this if statement is used for the saving the first frame in the varible.
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)#this will subtract the first frame to the second or upcomming frame.
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]#.If the value will be less than 30 then it will convert it to black and if the value is greater than 30 thenm it will be counted in white.
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)#threshold is declared to delete or ignore noises or shadows in the frames.
    (cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#defining the contour or defining the border around the objects.
    for contour in cnts:
        if cv2.contourArea(contour)<1000:# or it will remove the smaller objects from the frames like whose size is less than 1000 pixels.
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('frame',frame)
    #cv2.imshow('capturing',gray)
    #cv2.imshow('delta',delta_frame)
    #cv2.imshow('thresh',thresh_delta)
    key=cv2.waitKey(1)
    if key==ord('q'):
            break
video.release()
cv2.destroyAllWindows()
