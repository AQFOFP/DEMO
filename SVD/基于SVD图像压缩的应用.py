import numpy as np
import cv2


def comp_2d(image_2d,rate):
    height,width = image_2d.shape[:2]

    # 执行下面这一行报错显示无法广播。我修改了dtype还是报错，不知道为何。
    # cov_mat = image_2d - np.mean(image_2d, axis=1) 。
    # print("data.type:", image_2d.astype(np.float64).dtype)
    # print("mean.type:", np.mean(image_2d, axis=1).dtype)
    #
    # print("data.shape:", image_2d.astype(np.float64).shape)
    # print("mean.shape:", np.mean(image_2d, axis=1).shape)

    # 我自己广播代码为如下三行代码
    mean_array = np.mean(image_2d, axis=1)
    mean_array = mean_array[:, np.newaxis]
    mean_array = np.tile(mean_array, width)

    cov_mat = image_2d.astype(np.float64) - mean_array
    eig_val, eig_vec = np.linalg.eigh(np.cov(cov_mat))  # 求特征值 特征向量
    p = np.size(eig_vec, axis=1)
    idx = np.argsort(eig_val)
    idx = idx[::-1]
    eig_vec = eig_vec[:, idx]
    numpc = rate
    if numpc < p or numpc > 0:
        eig_vec = eig_vec[:, range(numpc)]
    score = np.dot(eig_vec.T, cov_mat)
    recon = np.dot(eig_vec, score) + mean_array
    recon_img_mat = np.uint8(np.absolute(recon))
    return recon_img_mat

if __name__ == '__main__':
    data = cv2.imread(r'sender.png')
    height, width = data.shape[:2]
    a_g = data[:, :, 0]
    a_b = data[:, :, 1]
    a_r = data[:, :, 2]
    rates = [30,60,90]  #主成分前30，60，90个k值
    for rate in rates:
        g_recon, b_recon, r_recon = comp_2d(a_g,rate), comp_2d(a_b,rate), comp_2d(a_r,rate)
        result = cv2.merge([g_recon, b_recon, r_recon])
        cv2.imshow('result_'+str(rate),result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()