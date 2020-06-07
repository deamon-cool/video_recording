import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.flip(frame, 1)

        out.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
