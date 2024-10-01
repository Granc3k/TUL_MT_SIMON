# Mady by: Hejsek, Šimon
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def load_bitmap(filename):
    with open(filename, "rb") as f:
        # load hlavičky
        header = f.read(54)

        # getnutí výšky a šířky
        width = int.from_bytes(header[18:22], byteorder="little")
        height = int.from_bytes(header[22:26], byteorder="little")

        # load zbytku dat
        img_data = np.fromfile(f, dtype=np.uint8)

    row_padded = (width * 3 + 3) & ~3

    # pole na obrazová data
    img = np.zeros((height, width, 3), dtype=np.uint8)

    for row in range(height):
        start = row * row_padded
        end = start + width * 3
        img[height - 1 - row, :] = img_data[start:end].reshape(
            (width, 3)
        )  # Otočíme obrázek vzhůru nohama

    return img


def get_image_size(image):
    height = image.shape[0]
    width = image.shape[1]

    return width, height


def red_ball(path):
    plt.figure(path)
    ball_original = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    ball_tresholded = ball_original.copy()
    plt.subplot(1, 2, 1)
    plt.imshow(ball_original)

    width, height = get_image_size(ball_original)

    for i in range(height):
        for j in range(width):
            r, g, b = ball_original[i, j].tolist()

            try:
                threshold = r / (r + g + b)
                if threshold < 0.5:
                    ball_tresholded[i, j] = [255, 255, 255]
            except:
                continue

    plt.subplot(1, 2, 1)
    plt.imshow(ball_original)

    plt.subplot(1, 2, 2)
    plt.imshow(ball_tresholded)

    plt.show()


def main():

    image = load_bitmap("cv03_objekty1.bmp")
    RGBimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.rcParams["image.cmap"] = "jet"
    plt.imshow(image)
    plt.colorbar()
    plt.show()
    plt.imshow(RGBimage)
    plt.colorbar()
    plt.show()

    image = cv2.imread("cv03_objekty1.bmp")

    # Převod na prostory
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    h, s, v = cv2.split(hsv_image)
    y, cr, cb = cv2.split(ycrcb_image)

    fig, axs = plt.subplots(1, 2, figsize=(5, 5))

    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title("RGB")

    axs[1].imshow(gray_image, cmap="gray")
    axs[1].set_title("Gray")
    plt.tight_layout()
    plt.show()

    # HSV
    fig, axs = plt.subplots(2, 2, figsize=(5, 5))

    axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title("RGB")

    h_plot = axs[0, 1].imshow(h, cmap="jet")
    axs[0, 1].set_title("HSV - H")
    fig.colorbar(h_plot, ax=axs[0, 1])

    s_plot = axs[1, 0].imshow(s, cmap="jet")
    axs[1, 0].set_title("HSV - S")
    fig.colorbar(s_plot, ax=axs[1, 0])

    v_plot = axs[1, 1].imshow(v, cmap="jet")
    axs[1, 1].set_title("HSV - V")
    fig.colorbar(v_plot, ax=axs[1, 1])

    plt.tight_layout()
    plt.show()

    # YCrCb
    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title("RGB")

    y_plot = axs[0, 1].imshow(y, cmap="gray")
    axs[0, 1].set_title("YCrCb - Y")
    fig.colorbar(y_plot, ax=axs[0, 1])

    cr_plot = axs[1, 0].imshow(cr, cmap="jet")
    axs[1, 0].set_title("YCrCb - Cr")
    fig.colorbar(cr_plot, ax=axs[1, 0])

    cb_plot = axs[1, 1].imshow(cb, cmap="jet")
    axs[1, 1].set_title("YCrCb - Cb")
    fig.colorbar(cb_plot, ax=axs[1, 1])

    # Zobrazení grafu
    plt.tight_layout()
    plt.show()

    red_ball("cv03_red_object.jpg")


if __name__ == "__main__":
    main()
