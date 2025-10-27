## 一种基于强化学习的XSS自动化攻击工具
1. 请根据系统选择合适的chorme-driver
 - https://www.chromium.org/getting-involved/download-chromium/
 - 解压到文件夹Chrome-win下
2. 根据系统安装合适的crawlergo
  - 下载安装与使用参考：https://github.com/Qianlitp/crawlergo/blob/master/README_zh-cn.md
  - 下载到文件夹 crawlergo下
3. 安装靶场（docker 方法）
```
docker search xss-labs
docker pull xss-labs
docker run -d --name xss-lab -p 8080:80 xss-labs
```
3. 使用方法
```
python -r requirements.txt
python spider.py
```
