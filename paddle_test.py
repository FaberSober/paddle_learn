import paddle

# 输出cudnn版本，如：8901，则正确
print(paddle.device.get_cudnn_version())
# 检查paddle是否安装成功
paddle.utils.run_check()