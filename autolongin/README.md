# SWPU疫情采集系统自动提交脚本

首先确保你的电脑中已经安装了python
## **chrome.py** 使用依赖

### 1.下载chromedriver

前往 http://chromedriver.storage.googleapis.com/index.html 选择你的chrome版本并下载。

将解压出的chromedriver.exe放到你的chrome安装文件里：

` C:\Program Files (x86)\Google\Chrome\`

### 2. 将chromedriver.exe 添加到系统环境变量的PATH里

### 3. 安装selenium

cmd 中输入 ：` pip install selenium`

***

## **swpu.py** 使用依赖

### 1. 安装lxml

（1）首先升级下pip：

```
python -m pip install -U pip
```

（2）安装wheel

```
pip install wheel
```

（3）下载lxml对应python版本的wheel文件：[地址]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml比如我的是lxml‑3.7.3‑cp37‑cp37m‑win_amd64.whl
进到whl文件的目录下，进入命令窗口，输入相应*.whl文件名，我的输入如下：
```
pip install  lxml‑3.7.3‑cp37‑cp37m‑win_amd64.whl
```

### 2. 安装requests

```
pip install requests
```



