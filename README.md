# H.D.D-BounceProxy
 绝区零自动弹反系统
 
![img](./Docs/title.png)
## 特性
* 支持视觉检测/音频检测
* 自定义弹反招式
* 支持键盘/手柄
* 增加 GUI

## 使用

#### 下载：[Python 3.11.6](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe)
> [!IMPORTANT]
> 请务必使用 Python 3.11.6，其他版本安装模块可能会有问题

### 安装 Python 3.11.6 
> [!IMPORTANT]
> 安装 Python 时请勾选 Add to PATH

#### 打开 Windows 终端输入以下指令: 

* 克隆项目
```
git clone https://github.com/Moxiner/H.D.D-BounceProxy.git
```

* 切换到项目目录
```
cd H.D.D-BounceProxy 
```   

* 环境安装
```
// 使用脚本安装
./install.bat

// 手动安装
// 1. 更新 pip
python -m pip install --upgrade pip
// 2. 使用 pip 清华源安装模块
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple some-package
// 3. 安装字体
copy ".\Font\black.ttf" "%windir%\Fonts" > nul
// 4. 刷新字体缓存
rundll32.exe /s %windir%\System32\spool\DRIVERS\Color\fontcache.dll
```

* 启动
```
./run.bat    
```

# 致谢

## 引用开源仓库

本项目引用以下开源项目，感谢他们对开源项目做出的贡献。

视觉提供: [《绝区零》自动招架，以及闪避实现方法，基于python](https://www.bilibili.com/video/BV1QUb6eYEA5/?share_source=copy_web&vd_source=cb6401bb53217ef7b31c26ec63b95347) - By: [西瓜加糖精](https://space.bilibili.com/321123985)

音频提供: [ZZZSoundTrigger](https://github.com/ImLaoBJie/ZZZSoundTrigger) - By: [ImLaoBJie](https://github.com/ImLaoBJie)

GUI 提供: [H.D.D-System](https://github.com/PPicku/H.D.D-System) - By: [PPicku](https://github.com/PPicku)

## 赞助者名单

本项目的发展离不开您的支持，谢谢你们的支持！
| 赞助者 | 赞助留言 | 
| :------------: | :------------- |
| 烦烦 |   |
| 波奇的摇滚吉他 | 做大做强 |