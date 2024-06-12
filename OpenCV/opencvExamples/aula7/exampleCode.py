import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    text += ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.putText(frame, text, (10, 50), font, 0.5, (0, 0, 255), 1)

    datet = str(datetime.datetime.now())
    cv2.putText(frame, datet, (10, 430), font, 0.5, (0, 0, 255), 1)

    if ret:
        cv2.imshow('imagem da camer hsv', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
