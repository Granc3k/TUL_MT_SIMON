# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek
import cv2
import numpy as np
import glob
import os

# Path ke složkám
image_path = "./cv10/data/input/"
output_path = "./cv10/data/output/"

# Load obrázků
images = glob.glob(os.path.join(image_path, "cv11_c0[1-6].bmp"))

for image_file in images:
    # Load přes cv2 obrázku
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Chyba při načítání obrázku {image_file}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Detekce kružnic pomocí Houghovy transformace
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=50,
        param2=10,
        minRadius=5,
        maxRadius=50,
    )

    # Count detekovaných kružnic
    num_circles = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        num_circles = len(circles[0])
        print(f"Detekováno {num_circles} kružnic v {image_file}")
    else:
        print(f"Nebyly detekovány žádné kružnice v {image_file}")

    # Print countu kružnic
    text = str(num_circles)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 2, 3)[0]
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = (img.shape[0] + text_size[1]) // 2
    cv2.putText(img, text, (text_x, text_y), font, 2, (0, 255, 0), 3)

    # Save result obrázku
    output_file = os.path.join(output_path, "output_" + os.path.basename(image_file))
    cv2.imwrite(output_file, img)
