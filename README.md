# PDF_Duplex_Combiner

When your scanner can only scan single pages, not duplex pages, this tool merges (shuffles) your odd pages and even pages into one PDF document.

## Scanning SOP

### English

1. Place your document stack face up in the scanner and scan single sided. Save the result as `odd.pdf`. This PDF will contain pages 1, 3, 5 and so on.
2. Flip the entire stack so the backs are facing up. Scan again in single-sided mode to capture the even pages. The second PDF will be in reverse order (for six pages it will be 6, 4, 2). Save this file as `even.pdf`.
3. Load these two PDFs into this tool and merge them to create the correctly ordered duplex file.

### 中文

1. 将整叠文件正面朝上放入扫描仪，以单面模式扫描，保存为 `odd.pdf`，其中包含第 1、3、5……页。
2. 将文件翻转，背面朝上再次单面扫描，保存为 `even.pdf`，顺序为 6、4、2 等。
3. 在本软件中导入这两个 PDF，即可自动合成为正确顺序的双面文档。

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

You can build your own .exe file by running this command in terminal, or download from release.
pyinstaller --onefile --windowed --name pdf_duplex_combiner gui.py


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

运行以下terminal指令来打包.exe文件，或者从release下载
pyinstaller --onefile --windowed --name pdf_duplex_combiner gui.py
