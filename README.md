# ProjectSender

Simulate a Serial Port Transponder.

## Overview

> [!NOTE]
> 工程使用PyCharm开发，Python 3.12+，主要用于模拟串口回复。

## 运行条件

### 虚拟串口（Paired）

根据实际情况，你可能需要使用类似于[VSPD](https://www.eltima.com/products/vspdxp/)这样的工具创建成对的串口，来模拟收发。

<details>
  <summary>Show images</summary>

  ![](https://raw.githubusercontent.com/zhongwcool/ProjectSender/main/Assets/154402.png)
</details>

### 依赖库

使用pySerial这个库打开串口和进行串口通信。首先，你需要安装这个库，通常可以使用pip来安装：

```shell
pip3 install pyserial
```

## 打包

使用**pyinstaller**打包成exe文件，打开**PyCharm**的`Terminal`输入：

![](https://raw.githubusercontent.com/zhongwcool/ProjectSender/main/Assets/app-logo.png)

```shell
pyinstaller --onefile --name Sender --icon app.ico main.py
```

执行完成后，打开Sender.exe，如果没有报错，则说明安装成功。

如果报错并提示`ModuleNotFoundError: No module named 'serial'`,则使用下面的命令：

```shell
pyinstaller --onefile --name Sender --icon app.ico --additional-hooks-dir .venv\Lib\site-packages\serial\__init__.py main.py
```