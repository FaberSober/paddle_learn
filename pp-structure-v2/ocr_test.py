from paddleocr import PaddleOCR, PPStructure, draw_ocr

#Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
#ch',en',fr',german',korean',japan
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = '/root/codes/ocr/pp-structure-v2/2.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

# 表格识别
# paddleocr --image_dir=table.jpg --type=structure --layout=false
ocrStru = PaddleOCR(type="structure", use_angle_cls=True, lang="ch")
img_table_path = '/root/codes/ocr/pp-structure-v2/table.jpg'
result2 = ocrStru.ocr(img_table_path, cls=True)
for line in result2:
    print(line)
