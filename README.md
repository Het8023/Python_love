## 📋 环境要求

-   Python 3.8 或更高版本
-   tkinter (Python 标准库，通常已预装)

## 🚀 快速开始

### 方法一：直接运行 Python 脚本

1. **克隆仓库**

```bash
git clone https://github.com/你的用户名/仓库名.git
cd He
```

2. **运行程序**

```bash
python hello.py
```

### 方法二：使用打包好的可执行文件

如果你已经使用 PyInstaller 打包了程序：

1. 直接双击 `dist/hello.exe` 运行（Windows 系统）
2. 无需安装 Python 环境

## 📦 打包说明

本项目使用 PyInstaller 进行打包，配置文件为 `hello.spec`。

### 打包步骤

1. **安装 PyInstaller**

```bash
pip install pyinstaller
```

2. **执行打包**

```bash
pyinstaller hello.spec
```

3. **获取可执行文件**
   打包完成后，可执行文件位于 `dist/hello.exe`

### PyInstaller 配置说明

-   `console=False`：无控制台窗口模式运行
-   `upx=True`：启用 UPX 压缩，减小文件体积
-   单文件模式打包，方便分发

## 🛠️ 技术栈

-   **GUI 框架**：Tkinter
-   **多线程**：threading 模块
-   **打包工具**：PyInstaller
-   **开发语言**：Python 3.8+

## 📝 自定义配置

你可以根据需要自定义以下内容：

### 修改关心话语

编辑 `hello.py` 中的 `tips` 列表：

```python
tips = [
    '你的自定义消息 1',
    '你的自定义消息 2',
    # ... 添加更多
]
```

### 修改配色方案

编辑 `bg_colors` 列表中的颜色代码：

```python
bg_colors = [
    # ... 添加更多配色
]
```
