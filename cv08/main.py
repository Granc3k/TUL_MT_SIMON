# made by Martin "Granc3k" Šimon, Vojtěch "Shock" Hejsek

import cv2
import numpy as np
import matplotlib.pyplot as plt


def method_a(frame1, frame2):
    sum_frame1 = 0
    sum_frame2 = 0
    for i in range(frame1.shape[0]):
        for j in range(frame1.shape[1]):
            sum_frame1 += frame1[i, j]
            sum_frame2 += frame2[i, j]
    return np.abs(sum_frame2 - sum_frame1)


def method_b(frame1, frame2):
    result = 0
    for i in range(frame1.shape[0]):
        for j in range(frame1.shape[1]):
            result += frame2[i, j] - frame1[i, j]
    return result


def method_c(frame1, frame2):
    hist1 = cv2.calcHist([frame1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([frame2], [0], None, [256], [0, 256])
    return np.sum(np.abs(hist1 - hist2))


def method_d(frame1, frame2):
    dct1 = cv2.dct(np.float32(frame1) / 255.0).flatten()
    dct2 = cv2.dct(np.float32(frame2) / 255.0).flatten()
    top5_dct1 = np.sort(np.abs(dct1))[-5:]
    top5_dct2 = np.sort(np.abs(dct2))[-5:]
    return np.sum(np.abs(np.log(top5_dct2 + 1) - np.log(top5_dct1 + 1)))


def plot_results(results, redx, title, subplot_index, max_val):
    plt.subplot(2, 2, subplot_index)
    plt.plot(results)
    for x in redx:
        plt.axvline(x=x, color="r")
    plt.ylim(0, max_val)
    plt.title(title)


def main():
    cap = cv2.VideoCapture("./cv08/data/cv08_video.mp4")
    NFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    redx = [209, 210, 269, 270]

    # Init listů pro resulty
    results_a = []
    results_b = []
    results_c = []
    results_d = []

    # processng first framu
    ret, prev_frame = cap.read()
    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

    # processing zbytku framu
    for i in range(1, NFrames):
        print(f"{i} of {NFrames}")
        ret, frame = cap.read()
        if not ret:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

        results_a.append(method_a(prev_frame_gray, frame_gray))
        results_b.append(method_b(prev_frame_gray, frame_gray))
        results_c.append(method_c(prev_frame_gray, frame_gray))
        results_d.append(method_d(prev_frame_gray, frame_gray))

        prev_frame_gray = frame_gray

    cap.release()

    # Calc max hodnot pro osu y
    max_val_a = max(results_a)
    max_val_b = max(results_b)
    max_val_c = max(results_c)
    max_val_d = max(results_d)

    # Plot vysledku 2x2
    plt.figure(figsize=(12, 10))
    plot_results(results_a, redx, "Method A", 1, max_val_a)
    plot_results(results_b, redx, "Method B", 2, max_val_b)
    plot_results(results_c, redx, "Method C", 3, max_val_c)
    plot_results(results_d, redx, "Method D", 4, max_val_d)
    plt.tight_layout()
    plt.show()

    # Real-time vizualizace výsledků
    cap = cv2.VideoCapture("./cv08/data/cv08_video.mp4")
    figure = plt.figure()
    maxVal = max(results_a)
    redy = np.array([0, maxVal, maxVal, 0])
    for i in range(1, NFrames):
        ret, bgr = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        figure.clear()
        plt.imshow(
            rgb, aspect="auto", extent=[0, NFrames, min(results_a), max(results_a)]
        )
        for x in redx:
            plt.axvline(x=x, color="r")
        plt.plot(results_a, color="b")
        plt.axvline(x=i, color="g")
        plt.axis([0, NFrames, min(results_a), max(results_a)])
        plt.show(block=False)
        plt.pause(0.01)

    cap.release()
    plt.show()


if __name__ == "__main__":
    main()
