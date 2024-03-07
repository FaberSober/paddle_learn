# paddle-learn

## jupyter
### version `GLIBCXX_3.4.30‘ not found

创建conda环境后出现此问题。
解决办法：
```
# 进入新创建的conda环境
cd /root/miniconda3/envs/paddle_xxx/lib/python3.8/site-packages/zmq/backend/cython/../../../../.././

# 查看libstdc++.so
ll libstd*

# 备份
mv libstdc++.so.6 libstdc++.so.6.old

# 关联新的libstdc++.so
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 libstdc++.so.6
```
