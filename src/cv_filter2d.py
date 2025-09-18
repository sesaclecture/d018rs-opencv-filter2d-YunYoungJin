import cv2
import sys
import numpy as np

def identity_kernel() -> np.array:

    arr = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def ones_kernel() -> np.array:
    # 모든 값이 1 → 입력 이미지 주변의 모든 픽셀을 합산하는 커널
    arr = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def original_kernel() -> np.array:
    arr = [[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def doubling_kernel() -> np.array:
    # 중심 값이 2인 커널 → 원본 값을 두 배로 출력
    arr = [[0, 0, 0],
           [0, 2, 0],
           [0, 0, 0]]
    kernel = np.array(arr, dtype=np.float32)
    return kernel
