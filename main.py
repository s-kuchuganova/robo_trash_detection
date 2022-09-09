import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow("Trash deteection", frame)
    k = cv2.waitKey(1)
    #чтобы закрыть открывшееся окно с вебкой нажми q
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
