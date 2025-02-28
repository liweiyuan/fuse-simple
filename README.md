# SimpleFS - 基于 FUSE 的简单文件系统

## 项目简介

SimpleFS 是一个使用 Python 和 FUSE (Filesystem in Userspace) 构建的简单文件系统示例。它演示了如何使用 FUSE 创建一个基本的文件系统，该文件系统在内存中存储文件和目录。

## 项目结构

```
fuse-sample/
├── fs.py          # 主程序文件，包含文件系统逻辑
├── requirements.txt # 项目依赖
└── myfs/          # 文件系统挂载点 (需要手动创建)
```

*   `fs.py`: 实现了 `SimpleFS` 类，继承自 `fuse.Operations`，并重写了必要的文件系统操作方法。
*   `requirements.txt`: 列出了项目依赖，即 `fusepy`。
*   `myfs/`: 这是文件系统的挂载点。在运行程序之前，你需要手动创建这个目录。

## 依赖

*   fusepy (>= 3.0.1)

## 安装和使用

### 1. 安装 FUSE

**Ubuntu:**

```bash
sudo apt update
sudo apt install  libfuse-dev
```

**macOS:**

使用 Homebrew 安装：

```bash
brew install macfuse
```
或者使用官方安装包安装，下载地址：https://osxfuse.github.io/

### 2. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 3. 创建挂载点

```bash
mkdir myfs
```

### 4. 运行

```bash
python fs.py
```

这将把 SimpleFS 文件系统挂载到 `./myfs` 目录。你可以在另一个终端窗口中访问该目录，并查看文件系统内容。

### 5. 卸载

要卸载文件系统，请按 Ctrl+C 停止 `fs.py` 进程。

## 示例

运行程序后，你可以在 `./myfs` 目录下看到以下内容：

```
myfs/
├── hello.txt
└── mydir/
```

你可以读取 `hello.txt` 文件的内容：

```bash
cat myfs/hello.txt
# 输出: Hello from FUSE!
```

## 注意事项
- 因为是在内存中，所以程序结束后，数据会丢失。

## 许可证

本项目采用 MIT 许可证。
