# Made by Vojtěch "Shock" Hejsek, Martin "Granc3k" Šimon
import cv2
import matplotlib.pyplot as plt
import numpy as np


def pca(image):
    depth = image.shape[2]
    vectors = [image[:, :, channel].flatten() for channel in range(depth)]
    effective_vector = np.add.reduce(vectors) / depth
    std_deviation = np.array([np.subtract(x, effective_vector) for x in vectors])
    covariance = np.cov(std_deviation)
    eigenvalues, eigenvectors = np.linalg.eig(covariance)
    eigvecs = eigenvectors[:, np.argsort(eigenvalues)]
    eigenspace = np.matmul(eigvecs, std_deviation)
    return np.array([np.add(v, effective_vector) for v in eigenspace])


def main():
    image = cv2.imread("./cv09/data/Cv09_obr.bmp")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    width, height = image.shape[:2]
    result = pca(image)

    plt.figure("Komponenty PCA")
    plt.subplot(2, 2, 1)
    plt.title("Původní obrázek")
    plt.imshow(image)
    plt.subplot(2, 2, 2)
    plt.title("K1")
    plt.imshow(np.reshape(result[0], (width, height)), cmap="gray")
    plt.subplot(2, 2, 3)
    plt.title("K2")
    plt.imshow(np.reshape(result[1], (width, height)), cmap="gray")
    plt.subplot(2, 2, 4)
    plt.title("K3")
    plt.imshow(np.reshape(result[2], (width, height)), cmap="gray")
    plt.show(block=False)

    plt.figure("Porovnání")
    plt.subplot(1, 2, 1),
    plt.title("PCA"),
    plt.imshow(np.reshape(result[0], (width, height)), cmap="gray")

    plt.subplot(1, 2, 2),
    plt.title("RGB2GRAY"),
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
