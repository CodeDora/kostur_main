import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard

detector = HandDetector(detectionCon=0.5, maxHands=1)
cap = cv2.VideoCapture(0)
cap.set(3, 700)
cap.set(4, 500)

# Karelerin genel boyutlarını ayarlamak için kullandığım kısım
box_size = 120

# Kırmızı karenin koordinatlarını belirttiğimiz kısım
red_box_x, red_box_y = 50, 150

# Yeşil karenin koordinatları belirttiğimiz kısım
green_box_x, green_box_y = 200, 150

# Mavi karenin koordinatları belirttiğimiz kısım
blue_box_x, blue_box_y = 350, 150

# Sarı karenin koordinatları belirttiğimiz kısım
yellow_box_x, yellow_box_y = 500, 150

# İşaret parmağının üzerindeki dairenin boyutu ve rengi için gerekli 
circle_radius = 20
circle_color = (0, 255, 0)  # Yeşil

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Kırmızı kareyi çiz
    cv2.rectangle(img, (red_box_x, red_box_y), (red_box_x + box_size, red_box_y + box_size), (0, 0, 255), cv2.FILLED)

    # Yeşil kareyi çiz
    cv2.rectangle(img, (green_box_x, green_box_y), (green_box_x + box_size, green_box_y + box_size), (0, 255, 0), cv2.FILLED)

    # Mavi kareyi çiz
    cv2.rectangle(img, (blue_box_x, blue_box_y), (blue_box_x + box_size, blue_box_y + box_size), (255, 0, 0), cv2.FILLED)

    # Sarı kareyi çiz
    cv2.rectangle(img, (yellow_box_x, yellow_box_y), (yellow_box_x + box_size, yellow_box_y + box_size), (0, 255, 255), cv2.FILLED)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # İşaret parmağının konumunu al 
        index_finger_tip = hand['lmList'][8]  # İşaret parmağı ucu genellikle 8. noktadadır
        index_finger_x, index_finger_y = index_finger_tip[0], index_finger_tip[1]

        # İşaret parmağının üzerinde bir daire çiz
        cv2.circle(img, (index_finger_x, index_finger_y), circle_radius, circle_color, cv2.FILLED)

        # Kırmızı kareye girildiyse
        if red_box_x < index_finger_x < red_box_x + box_size and red_box_y < index_finger_y < red_box_y + box_size:
            keyboard.press_and_release('right')  # Sağa hareket

        # Yeşil kareye girildiyse bunu yap------
        elif green_box_x < index_finger_x < green_box_x + box_size and green_box_y < index_finger_y < green_box_y + box_size:
            keyboard.press_and_release('left')  # Sola hareket

        # Mavi kareye girildiyse
        elif blue_box_x < index_finger_x < blue_box_x + box_size and blue_box_y < index_finger_y < blue_box_y + box_size:
            keyboard.press_and_release('up')  # Yukarı hareket

        # Sarı kareye girildiyse
        elif yellow_box_x < index_finger_x < yellow_box_x + box_size and yellow_box_y < index_finger_y < yellow_box_y + box_size:
            keyboard.press_and_release('down')  # Aşağı hareket

    cv2.imshow("Kamera", img) 
    cv2.waitKey(1)
