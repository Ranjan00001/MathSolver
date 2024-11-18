from ocr import OCR

ocr=OCR(image_folder=r"C:\Users\Deependra\Desktop\DeepLearning\Cnn\cv project\MathSolver\compare_model\test")


if __name__ == "__main__":
    print("hello world")
    # ocr.keras_ocr_works()
    ocr.easyocr_model_works()
    # ocr.pytesseract_model_works()