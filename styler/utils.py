import cv2
import numpy as np

MEAN_VALUES = np.array([123, 117, 104]).reshape((1,1,3))


def resize(img, image_h, image_w, zoom=False):
    # crop image from center
    ratio = float(image_h) / image_w
    height, width = int(img.shape[0]), int(img.shape[1])
    yy, xx = 0, 0
    if height > width * ratio:  #too tall
        yy = int(height - width * ratio) // 2
        height = int(width * ratio)
    else:  # too wide
        xx = int(width - height / ratio) // 2
        width = int(height / ratio)
    if zoom:
        yy += int(height / 6)
        xx += int(height / 6)
        height = int(height * 2 / 3)
        width = int(width * 2 / 3)
    crop_img = img[yy:yy + height, xx:xx + width]
    # resize
    resized_img = cv2.resize(crop_img, (image_h, image_w))
    centered_img = resized_img - MEAN_VALUES

    return centered_img


def save_video(filepath, fps, w, h, frames):
    codecs = ['WMV1', 'MJPG', 'XVID', 'PIM1']
    '''
      If you cannot write video file, you may change the used codec
    '''
    used_codec = codecs[2]  # change the index from codecs
    fourcc = cv2.VideoWriter_fourcc(*used_codec)
    out = cv2.VideoWriter(filepath, fourcc, fps, (w, h))
    for frame in frames:
        f = frame[0, :, :, :]
        out.write(post_process(f))
    out.release()


def post_process(image):
    img = image + MEAN_VALUES
    img = np.clip(img, 0, 255).astype('uint8')
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
