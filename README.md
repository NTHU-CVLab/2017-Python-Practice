# 2017 Python-Practice

Apply deep-style-transfer model onto video!

## Requirements:
- Tensorflow (CPU version)
```bash
pip install tensorflow
```
- OpenCV
    - Windows: with Python 3.5 (x64)
        - `pip install opencv-python`
    - Mac:
        - Install through `brew`
    - Linux:
        - Build by your own or use other pre-build

## Homeworks
1. Import `Video` and `save_video` from the correct module of package `styler`
2. Find and set the input video `path` in `Line#44`
3. Write a list comprehension to iterate through all frames, and make it be processed by Tensorflow.
4. Pass the results as a argument into function
5. Modify the class method `read_frames()` in `styler/video.py`
    - Read video frames from `self.cap` and collect frames into list
    - Apply `resize()` on each frame before add it to list
    - Also assign frames to "self" object
    - Return your results

## Note:
If you can not save the output, you may try to change the codec used by changing the codec index in `styler/utils.py` Line#36.


## Reference:
We use the trained model and code in [deep-style-transfer](https://github.com/albertlai/deep-style-transfer).
