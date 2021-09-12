import os
import re
from pathlib import Path
from paddleocr import PaddleOCR


def recognize(upload_folder):
    ocr = PaddleOCR(lang='en', use_gpu=False)
    result = ""
    for idx, file_path in enumerate(Path(upload_folder).glob('*.jpg')):
        tmp = ocr.ocr(str(file_path), det=False, cls=False)
        os.remove(file_path)
        result += f"<p>{idx + 1}. Номер: "
        lic_plate = re.sub(r'[^\w\s]', '', tmp[0][0])
        result += lic_plate if len(lic_plate) > 0 else "Найден, но не распознан"
        result += "</p>"
    result = result if len(result) > 0 else "Не найдены номера на изображении"
    return result

