# PDF Duplex Combiner

The PDF Duplex Combiner tool merges two separately scanned PDF documents—one containing odd-numbered pages and another containing even-numbered pages—into a single, correctly ordered duplex PDF. This is especially helpful if your scanner only supports single-sided scans.

## How to Use

Follow the scanning instructions, then either download the pre-built program from the releases or build it yourself following the provided instructions.

### Scanning Instructions

1. Place your document stack face-up in the scanner. Scan using single-sided mode. Save this file as `odd.pdf`. It should include pages 1, 3, 5, etc.
2. Flip the entire stack so the backside is facing up. Scan again using single-sided mode. The resulting file (`even.pdf`) will have pages in reverse order (e.g., 6, 4, 2).
3. Use PDF Duplex Combiner to merge these PDFs into a properly ordered duplex file.

## Download from Release

Go to the [releases page](#) and download the executable for your operating system. Run the executable and follow the prompts.

## Building from Source (Alternative to Downloading)

### Using Poetry

Ensure you have [Poetry](https://python-poetry.org/) 2.1.3 and poetry-plugin-shell 1.0.1 installed, then execute:

```bash
poetry shell
poetry install --no-root  # installs PyPDF2 and development dependencies
```

### Create a Windows Executable

To build your own executable:

```bash
pyinstaller --onefile --windowed --name pdf_duplex_combiner gui.py
```

Alternatively, download the pre-built executable from the release page.

---

# PDF 双面合并工具

PDF 双面合并工具用于将两个单独扫描的 PDF 文件——一个包含奇数页，另一个包含偶数页——合并为一个顺序正确的双面 PDF 文件。特别适用于只支持单面扫描的扫描仪。

## 如何使用

请先按下方说明完成扫描步骤，然后可以选择从发布页面下载已构建好的程序，或按照说明自行构建。

### 扫描说明

1. 将整叠纸张正面朝上放入扫描仪，使用单面扫描模式，保存为 `odd.pdf`，应包含第 1、3、5 等页。
2. 将整叠纸张翻面，背面朝上再次使用单面扫描，保存为 `even.pdf`，该文件中页面通常是倒序的（如 6、4、2）。
3. 使用本工具导入两个 PDF，即可合并为顺序正确的双面文档。

## 从发布版下载

访问[发布页面](#)，下载适用于您操作系统的可执行文件。运行后按提示操作。

## 自行构建程序（作为下载的替代方案）

### 使用 Poetry

确保已安装 [Poetry](https://python-poetry.org/) 2.1.3 和 poetry-plugin-shell 1.0.1，然后执行以下命令：

```bash
poetry shell
poetry install --no-root  # 安装 PyPDF2 及开发依赖
```

### 创建 Windows 可执行文件

通过以下命令生成可执行文件：

```bash
pyinstaller --onefile --windowed --name pdf_duplex_combiner gui.py
```

或者直接从发布页面下载已构建好的可执行文件。
