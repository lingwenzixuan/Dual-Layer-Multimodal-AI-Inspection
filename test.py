import os
import tkinter as tk
from tkinter import filedialog
import cv2
from ultralytics import YOLO

# 1. 確保儲存結果的資料夾存在（自動建立 test_picture 資料夾）
output_dir = "test_picture"
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

# 2. 隱藏 tkinter 主視窗，並跳出檔案選擇對話框讓使用者選圖
root = tk.Tk()
root.withdraw()

print("請在跳出的視窗中選擇你的圖片...")
image_path = filedialog.askopenfilename(
    title="選擇要檢測的圖片",
    filetypes=[
        ("圖片檔案", "*.jpg *.jpeg *.png *.bmp"),
        ("所有檔案", "*.*"),
    ],
)

# 檢查是否有選擇圖片
if not image_path:
  print("未選擇任何圖片，程式已取消。")
  exit()

print(f"已選擇圖片: {image_path}")

try:
  # 3. 載入 YOLOv9 模型（使用官方原始英文標籤）
  model = YOLO("yolov9c.pt")

  # 4. 執行辨識
  results = model(image_path)

  # 取得畫好偵測框的圖片（numpy 陣列格式）
  annotated_frame = results[0].plot()

  # 5. 將結果圖片存入 test_picture 資料夾中（以原檔名加上前綴命名）
  base_name = os.path.basename(image_path)
  output_image_path = os.path.join(output_dir, f"result_{base_name}")
  cv2.imwrite(output_image_path, annotated_frame)
  print(f"辨識完成！結果圖片已儲存至：{output_image_path}")

  # 6. 顯示辨識結果視窗
  cv2.imshow("YOLOv9 Detection Result", annotated_frame)
  print("請按任意鍵或關閉圖片視窗以繼續...")
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  # 7. 詢問使用者是否要刪除剛剛產生的結果圖片
  while True:
    choice = (
        input(
            f"是否要刪除剛剛產生的結果圖片 [{output_image_path}]？ (y/n): "
        )
        .strip()
        .lower()
    )
    if choice == "y":
      if os.path.exists(output_image_path):
        os.remove(output_image_path)
        print(f"已成功刪除檔案：{output_image_path}")
      break
    elif choice == "n":
      print(f"已保留結果圖片，檔案安全存放於：{output_image_path}")
      break
    else:
      print("輸入錯誤，請僅輸入 'y' (刪除) 或 'n' (保留)。")

except Exception as e:
  print(f"執行過程中發生錯誤: {e}")
