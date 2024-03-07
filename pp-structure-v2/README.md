# PP-StructureV2

https://aistudio.baidu.com/modelsdetail/18?modelId=18

python3 /root/.local/lib/python3.8/site-packages/paddleocr/paddleocr.py --image_dir=1.png --type=structure --image_orientation=true
python3 /root/.local/lib/python3.8/site-packages/paddleocr/paddleocr.py --image_dir=table.jpg --type=structure --layout=false

## 图像方向分类+版面分析+表格识别
paddleocr --image_dir=1.png --type=structure --image_orientation=true
paddleocr --image_dir=2.png --type=structure --image_orientation=true
paddleocr --image_dir=3.png --type=structure --image_orientation=true
- 带有文字、图片的混合识别
paddleocr --image_dir=4.png --type=structure --image_orientation=true
- 带有文字、图片、公式的混合识别
paddleocr --image_dir=5.png --type=structure --image_orientation=true
- 带有文字、图片、公式、表格的混合识别
paddleocr --image_dir=6.png --type=structure --image_orientation=true

paddleocr --image_dir=table2.png --type=structure --image_orientation=true

## 版面分析+表格识别
paddleocr --image_dir=1.png --type=structure

## 版面分析
paddleocr --image_dir=1.png --type=structure --table=false --ocr=false

## 表格识别
paddleocr --image_dir=table.jpg --type=structure --layout=false
paddleocr --image_dir=table2.png --type=structure --layout=false

# 部署服务
## 部署说明
conda activate paddle_env
卸载ocr_system模块
hub uninstall ocr_system

安装ocr_system模块
hub install deploy/hubserving/ocr_system/

启动ocr_system
`hub serving start -c ./deploy/hubserving/ocr_system/config.json`

hub uninstall structure_system

hub install deploy/hubserving/structure_system/

`hub serving start -c ./deploy/hubserving/structure_system/config.json`

完整命令：/root/miniconda3/envs/paddle_env/bin/python /root/miniconda3/envs/paddle_env/bin/hub serving start -c ./deploy/hubserving/structure_system/config.json

### 后台启动
nohup hub serving start -c ./deploy/hubserving/structure_system/config.json > /dev/null 2>&1 &

ps -ef|grep hub

使用/root/codes/ocr/PaddleOCR/service.sh脚本。


## 测试部署服务
python tools/test_hubserving.py --server_url=http://127.0.0.1:8868/predict/ocr_system --image_dir=/root/codes/ocr/paddle-ocr-learn/pp-structure-v2/3.png --visualize=false

python tools/test_hubserving.py --server_url=http://127.0.0.1:8870/predict/structure_system --image_dir=/root/codes/ocr/paddle-ocr-learn/pp-structure-v2/table2.png --visualize=false
python tools/test_hubserving.py --server_url=http://127.0.0.1:8870/predict/structure_system --image_dir=/root/codes/ocr/paddle-ocr-learn/pp-structure-v2/table.jpg --visualize=false

python tools/test_hubserving.py --server_url=http://ocr.structure_system.dward.cn/predict/structure_system --image_dir=/root/codes/ocr/paddle-ocr-learn/pp-structure-v2/table2.png --visualize=false

# 查看nvidia显卡使用状态
nvidia-smi

直接使用
`nvitop`

展示超完整的显卡信息，则用如下命令：
`nvitop -m full`

**安装方式**
`pip install nvitop`

