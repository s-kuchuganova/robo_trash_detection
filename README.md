# robo_trash_detection
ITMO.DataProductHack,  OpenDataTools track

For running on Jetson run:

```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install

#detection
#for webcam set source 0
python detect.py --weights path/to/best.pt --img 416 --conf 0.1 --source test_images/zoom_cigaret.jpg
```
