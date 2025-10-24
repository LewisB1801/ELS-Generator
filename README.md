# 🚓 ELS Generator

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/LewisB1801/ELS-Generator)](https://github.com/LewisB1801/ELS-Generator/releases)

Created by **Three Peaks Studios**  
Version 1.0

A **CustomTkinter-based Python tool** to bulk copy and rename files, with auto folder scanning for `.meta`, `.ytd`, and `.yft` files. Ideal for FiveM ELS projects and similar workflows.

---

## 📂 Features

- **Manual Mode**: Select a source file and output folder to duplicate and rename files using a `names.txt` list.  
- **Auto Generator**: Automatically scan folders and generate a `names.txt` with folder names containing allowed file types.  
- **Default Output Folder**: Automatically creates a `Complete` folder in the same directory as the EXE/script.  
- **Example Files**: Bundled `Example_Files` are extracted automatically on first run.  
- **Cross-platform**: Works as Python script or compiled EXE.

---

## 📝 Installation

### Python Version
- Python 3.13+ required
- Install dependencies:

pip install customtkinter

shell
Copy code

### Using the Python Script
1. Clone the repository:

git clone https://github.com/LewisB1801/ELS-Generator.git
cd ELS-Generator

markdown
Copy code

2. Run the script:

python ELS-Generator.py

yaml
Copy code

### Using the EXE
1. Download the latest release EXE from GitHub releases.  
2. Place it in your project folder.  
3. Launch the EXE — `Example_Files` and `Complete` folders will be created automatically.

---

## ⚙️ Usage

### Manual Mode
1. Browse for a **source file**.  
2. Browse for an **output folder** (defaults to `Complete` folder).  
3. Ensure `names.txt` exists or create a blank one.  
4. Click **Run Copy & Rename**.

### Auto Generator
1. Click **Scan Folder** to detect folders containing `.meta`, `.ytd`, or `.yft` files.  
2. The detected folder names are saved into `names.txt` automatically.  
3. Use manual mode afterward to copy and rename files.

---

## 🖼️ Screenshots

*Add your images here to showcase the UI or usage.*

![UI Screenshot](images/screenshot1.png)  
![Auto Scan Screenshot](images/screenshot2.png)  

---

## 🎥 Demo Video

*Add your demo video link here.*

[Watch the demo video](https://www.youtube.com/watch?v=YOUR_VIDEO_LINK)

---

## 📄 License

This project is released under the **MIT License**.

MIT License

Copyright (c) 2025 Three Peaks Studios

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🏷️ Acknowledgements

- **CustomTkinter**: [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- **Python**: [https://www.python.org](https://www.python.org)

---

## 🔗 Links

- Repository: [https://github.com/yourusername/ELS-Generator](https://github.com/LewisB1801/ELS-Generator)  
- Releases: [https://github.com/yourusername/ELS-Generator/releases](https://github.com/LewisB1801/ELS-Generator/releases)

---

*Created with ❤️ by Three Peaks Studios, 2025*
