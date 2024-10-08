#Mady by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_images_with_error(original, corrected, error, title):
    plt.figure(figsize=(15,5))
    
    # Původní obrázek
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title(f'Original - {title}')
    plt.axis('off')
    
    # Etalon
    plt.subplot(1, 3, 2)
    plt.imshow(error, cmap='gray')
    plt.title(f'Etalon - {title}')
    plt.axis('off')

    # Opravený obrázek
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB))
    plt.title(f'Corrected - {title}')
    plt.axis('off')
    
    plt.show()

def custom_histogram_equalization(image):
    N, M = image.shape
    H, _ = np.histogram(image, bins=256, range=[0, 256])
    
    # Kumulativní suma histogramu
    H_cumsum = np.cumsum(H)
    
    # Aplikace zadané rovnice
    q0, p0, qk = 0, 0, 255
    T = (qk - q0) / (N * M) * H_cumsum + q0
    T = np.clip(T, 0, 255).astype(np.uint8)
    
    #Transformace obrazu
    equalized_image = T[image]
    
    return equalized_image

def display_rentgen(equalized_image, hist, equalized_hist):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Původní obrázek
    rentgen = cv2.imread('Cv04_rentgen.bmp')
    axs[0, 0].imshow(rentgen)
    axs[0, 0].set_title('Original Rentgen Image')
    axs[0, 0].axis('off')

    # Histogram původního obrázku
    axs[0, 1].plot(hist)
    axs[0, 1].set_title('Original Rentgen Histogram')

    # Upravený obrázek
    axs[1, 0].imshow(equalized_image, cmap='gray')
    axs[1, 0].set_title('Equalized Rentgen Image')
    axs[1, 0].axis('off')

    # Histogram upraveného obrázku
    axs[1, 1].plot(equalized_hist)
    axs[1, 1].set_title('Equalized Rentgen Histogram')

    plt.tight_layout()
    plt.show()

def main():
    #----- ELATONY -----
    porucha1 = cv2.imread('Cv04_porucha1.bmp')
    porucha2 = cv2.imread('Cv04_porucha2.bmp')

    etalon1 = cv2.imread('Cv04_porucha1_etalon.bmp', cv2.IMREAD_GRAYSCALE)
    etalon2 = cv2.imread('Cv04_porucha2_etalon.bmp', cv2.IMREAD_GRAYSCALE)

    c = 255

    # Korekce jasového obrazu pomocí etalonu, aplikováno na každý kanál zvlášť
    corrected1 = np.zeros_like(porucha1)
    corrected2 = np.zeros_like(porucha2)

    for i in range(3):
        corrected1[:, :, i] = porucha1[:, :, i] * (c / (etalon1 + 1e-5))
        corrected2[:, :, i] = porucha2[:, :, i] * (c / (etalon2 + 1e-5))

    # Zajistit, že hodnoty pixelů nepřesáhnou rozsah [0, 255]
    corrected1 = np.clip(corrected1, 0, 255).astype(np.uint8)
    corrected2 = np.clip(corrected2, 0, 255).astype(np.uint8)

    # Zobrazení výsledků s chybou
    display_images_with_error(porucha1, corrected1, etalon1, 'Porucha 1')
    display_images_with_error(porucha2, corrected2, etalon2, 'Porucha 2')
    
    #----- RENTGEN -----

    rentgen = cv2.imread('Cv04_rentgen.bmp', cv2.IMREAD_GRAYSCALE)

    hist, bins = np.histogram(rentgen.flatten(), 256, [0, 256])

    equalized_rentgen = custom_histogram_equalization(rentgen)

    equalized_hist, _ = np.histogram(equalized_rentgen.flatten(), 256, [0, 256])

    display_rentgen(equalized_rentgen, hist, equalized_hist)

if __name__ == '__main__':
    main()
