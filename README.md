# PDF_Duplex_Combiner

When your scanner can only scan single pages, not duplex pages, this tool merges (shuffles) your odd pages and even pages into one PDF document.

## Usage

### Using Poetry

```bash
poetry install --no-root  # install PyPDF2 and dev tools such as reportlab
poetry run pdf-duplex-combiner
poetry run pdf-duplex-combiner-gui  # Launch the GUI
```

### Using pip

1. Install [PyPDF2](https://pypi.org/project/PyPDF2/) for Python 3 if you plan to run the script. The GUI uses Tkinter, which is bundled with most Python installations. On some Linux distributions you may need to install the `python3-tk` package separately.
   ```bash
   pip install PyPDF2
   ```
2. Run the program:
   ```bash
   python main.py
   ```
   To launch the GUI instead, run:
   ```bash
   python gui.py
   ```
3. When prompted, provide the path to the PDF containing the odd-numbered pages.
4. Provide the path to the PDF containing the even-numbered pages. These pages are usually scanned in reverse order.
5. Enter a file name for the merged output PDF.

### Windows executable

A placeholder Windows executable (`pdf_page_merger.exe`) is included for convenience. It cannot be run directly because PyInstaller could not be used in this environment. If you need a real executable, install PyInstaller and build it from `main.py`.

---

## 中文使用说明

### 使用 Poetry

```bash
poetry install --no-root
poetry run pdf-duplex-combiner
poetry run pdf-duplex-combiner-gui  # 启动图形界面
```

### 使用 pip

1. 确保已经安装 Python 3，并运行以下命令安装依赖。GUI 基于 Tkinter，大多数 Python 发行版都已自带，如在 Linux 上缺失，可另外安装 `python3-tk`：
   ```bash
   pip install PyPDF2
   ```
2. 执行脚本：
   ```bash
   python main.py
   ```
   若要启动图形界面，运行：
   ```bash
   python gui.py
   ```
3. 根据提示输入奇数页 PDF 的路径。
4. 输入偶数页（通常是反向扫描）的 PDF 路径。
5. 输入合并后输出文件的名称。

`pdf_page_merger.exe` 文件仅为占位符，如需可执行文件，请自行使用 PyInstaller 打包。
