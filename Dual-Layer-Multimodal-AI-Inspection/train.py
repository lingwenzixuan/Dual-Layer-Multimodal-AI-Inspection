from ultralytics import YOLO
import os

if __name__ == '__main__':
    # 1. 載入 YOLOv9 預訓練模型 (yolov9c.pt 會自動下載)
    model = YOLO("yolov9c.pt")

    # 2. 指定 custom_data.yaml 的真實絕對路徑 (路徑前加 r 避免轉義字元)
    yaml_path = r"D:\YOLOV9\Glass_Inspection\custom_data.yaml"

    # 3. 開始訓練 (針對玻璃瑕疵優化的參數)
    results = model.train(
        data=yaml_path,
        epochs=150,           # 訓練輪數，瑕疵較難學習，建議 150 輪以上
        imgsz=1024,           # 瑕疵微小，使用 1024 高解析度，保留細節
        batch=4,              # 若 GPU 記憶體不足 (OOM)，請調小至 2 或 4
        device=0,             # 使用第 1 張顯卡 (GPU 0)
        workers=2,            # Windows 建議設為 2 或 4
        name="glass_defects_exp1"
    )