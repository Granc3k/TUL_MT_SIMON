# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek
import cv2
import numpy as np

# Load imagů
image_path = "./cv10/data/input/cv11_merkers.bmp"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Normalizace image
binary_image = image / 255.0

# Split imagů na horní a dolní polovinu
height, width = binary_image.shape
upper_half = binary_image[: height // 2, :]
lower_half = binary_image[height // 2 :, :]

# Definice strukturního elementu
kernel = np.ones((3, 3), np.uint8)

# Eroze pro získání marků
eroded_upper = cv2.erode(upper_half, kernel, iterations=1)
eroded_lower = cv2.erode(lower_half, kernel, iterations=1)


# Find souřadnic marků
def find_coordinates(eroded_image):
    coordinates = np.column_stack(np.where(eroded_image > 0))
    return coordinates


upper_coordinates = find_coordinates(eroded_upper)
lower_coordinates = find_coordinates(eroded_lower)

# Create matice 3x3 pro souřadnice
upper_matrix = np.zeros((3, 3), dtype=int)
lower_matrix = np.zeros((3, 3), dtype=int)

# Fill in matice souřadnicemi
for coord in upper_coordinates:
    x, y = coord
    upper_matrix[x % 3, y % 3] += 1

for coord in lower_coordinates:
    x, y = coord
    lower_matrix[x % 3, y % 3] += 1

# Print souřadnic do konzole
print("Upper half coordinates matrix:")
print(upper_matrix)

print("Lower half coordinates matrix:")
print(lower_matrix)

# Dilatace pro dekódování obrázku
dilated_upper = cv2.dilate(eroded_upper, kernel, iterations=1)
dilated_lower = cv2.dilate(eroded_lower, kernel, iterations=1)

# Union horní a dolní poloviny
decoded_image = np.vstack((dilated_upper, dilated_lower))

# Save dekódovaného obrázku
cv2.imwrite("./cv10/data/output/decoded_image.bmp", decoded_image * 255)
