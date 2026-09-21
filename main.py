import sys
import torch
import ultralytics
from ultralytics import YOLO

print("Python 版本:", sys.version)                    # 列印 Python 版本資訊
print("PyTorch 版本:", torch.__version__)             # 列印 PyTorch 版本
print("是否支援 CUDA:", torch.cuda.is_available())     # 查詢是否支援 CUDA
print("CUDA 版本:", torch.version.cuda)              # 列印 CUDA 版本
print("cuDNN 版本:", torch.backends.cudnn.version())  # 列印 cuDNN 版本

if torch.cuda.is_available():
    print("GPU 名稱:", torch.cuda.get_device_name(0))          # 列印第一張 GPU 的名稱
    print("GPU 詳細屬性:", torch.cuda.get_device_properties(0)) # 列印 GPU 詳細屬性

print("Ultralytics 版本:", ultralytics.__version__)  # 列印 ultralytics 版本
model = YOLO('yolov9c.pt')                           # 載入預訓練 YOLOv9c 模型
model.info()                                         # 列印 YOLOv9 模型參數
