import qrcode
import cv2

img = qrcode.make("www.google.com")
img.save("google.jpg")

d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("google.jpg"))