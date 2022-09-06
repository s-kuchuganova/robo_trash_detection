import numpy as np
import torch
import cv2
# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s-cls.pt')  # load from PyTorch Hub

batch = 1
# Images
imgs = 'test_images/zoom_cigaret.jpg'  # batch of images
data = cv2.imread(imgs)
data = cv2.resize(data, (224,224))
# print((data.T).shape)
# Inference
data = torch.from_numpy(np.expand_dims(data.T,axis=0))

print(data.shape)
results = model(data)

# Results
results.print()
results.save()  # or .show()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]  # img1 predictions (pandas)
