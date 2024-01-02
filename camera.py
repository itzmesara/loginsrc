import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('Original Frame', frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Processed Frame', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
