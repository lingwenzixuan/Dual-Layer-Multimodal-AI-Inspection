# 🔍 Dual-Layer-Multimodal-AI-Inspection（建設中）
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg)](https://pytorch.org/)
[![YOLOv9](https://img.shields.io/badge/Model-YOLOv9c-orange.svg)](https://github.com/WongKinYiu/yolov9)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

本專案旨在建構一套結合 **Ultralytics YOLOv9** 與 **OpenCV / Tkinter** 的智慧化工業光學檢測（AOI）系統驗證原型（PoC）。專案聚焦於透明或複雜材質物件內外部缺陷（如內部氣泡、微小裂紋與結構異狀）的自動辨識，並具備圖形化介面選取、自動檔案歸檔與互動式清理機制。

---

## ✨ 核心功能特點 (Key Features)

- **直覺化圖形介面**：內建 `tkinter` 檔案對話框，點選即可自由載入待檢測目標影像。
- **YOLOv9 高效辨識核心**：載入 `yolov9c.pt` 預訓練與微調權重，精準對焦並標註物件瑕疵位置。
- **自動化測試歸檔**：檢測完成後自動於根目錄建立 `test_picture` 資料夾，並將結果以規範化命名（`result_<原檔名>`）安全存檔。
- **互動式記憶體與儲存管理**：預覽檢測結果後，終端機將即時互動詢問是否保留或清理暫存結果，優化磁碟空間。

---

## 💻 系統需求 (Prerequisites)

請確保運行環境已安裝以下核心相依套件：
- Python 3.10 或以上版本
- PyTorch & Torchvision
- Ultralytics (`pip install ultralytics`)
- OpenCV-Python (`pip install opencv-python`)
- Pillow (`pip install Pillow`)

---

## 🚀 快速開始 (Quick Start)

1. **複製專案到本地端**：
   ```bash
   git clone [https://github.com/lingwenzixuan/Dual-Layer-Multimodal-AI-Inspection.git](https://github.com/lingwenzixuan/Dual-Layer-Multimodal-AI-Inspection.git)
   cd Dual-Layer-Multimodal-AI-Inspection
