# 🎨 ASCII Art Generator

A simple but powerful **Python ASCII Art Generator** that turns **images and text into ASCII art** directly in your terminal.

Customize your output with colors, choose from **500+ PyFiglet fonts**, and export your creations to text files.

---

## ✨ Features

* 🖼️ **Image → ASCII**
* 🔤 **Text → ASCII**
* 🎨 6 terminal color families
* 🔥 **500+ ASCII text fonts**
* 📐 Custom image width
* 💾 Export ASCII art to `.txt`
* 🖥️ Terminal-based interface
* ⚡ Lightweight and fast
* 🐍 Written entirely in Python
* 🧩 Separate `color.py` color module

---

## 📊 GitHub Stats

![GitHub Stars](https://img.shields.io/github/stars/vxlxv/ascii-art-generator?style=for-the-badge)

![GitHub Forks](https://img.shields.io/github/forks/vxlxv/ascii-art-generator?style=for-the-badge)

![GitHub Issues](https://img.shields.io/github/issues/vxlxv/ascii-art-generator?style=for-the-badge)

![GitHub License](https://img.shields.io/github/license/mit/ascii-art-generator?style=for-the-badge)

![GitHub Last Commit](https://img.shields.io/github/last-commit/vxlxv/ascii-art-generator?style=for-the-badge)

### Project Information

|                   |                  |
| ----------------- | ---------------- |
| 🐍 Language       | Python           |
| 🔤 Fonts          | **500+**         |
| 🖼️ Image Support | Yes              |
| 🎨 Colors         | 6                |
| 💾 Export         | `.txt`           |
| 📦 Dependencies   | 2                |
| 🖥️ Interface     | Terminal / CLI   |
| 📜 License        | Add your license |


---

## 📸 What It Does

### Image → ASCII

Convert an image such as:

```text
cat.png
```

into terminal ASCII art:

```text
             .:-=+*##%%%%%%##*+=-:.
          .:=*#%%%%%%%%%%%%%%%%%%#*=:
        .-*#%%%%%%%%%%%%%%%%%%%%%%%%#*-
       -*%%%%%%#*=-:.       .:-=*#%%%%-
      =#%%%%#=.                   .=#%%=
     +%%%%*:                       .:*%%+
    =%%%%=                           =%%%
   .#%%%:             .               %%%
   :%%%+          .     .             +%%%
   +%%%:         .       .             %%%
   #%%#                         .      #%%#
   %%%+              ..              +%%%
   #%%#          .        .          #%%#
   +%%%:                             :%%%
    %%%#:                           =%%%
     *%%%%=.                     .=%%%%*
      +#%%%%#*=-:.         .:-=*#%%%%#+
```

The image width can be customized to control the level of detail.

---

## 🔤 Text → ASCII

Enter normal text:

```text
ASCII
```

and turn it into large ASCII lettering:

```text
    _    ____   ____ ___ ___
   / \  / ___| / ___|_ _|_ _|
  / _ \ \___ \| |    | | | |
 / ___ \ ___) | |___ | | | |
/_/   \_\____/ \____|___|___|
```

The generator automatically detects the fonts available in your PyFiglet installation.

### 🔥 500+ Fonts

Instead of relying on a small hardcoded font list, the program reads the installed PyFiglet fonts:

```python
pyfiglet.FigletFont.getFonts()
```

This gives you access to **500+ fonts**, depending on the installed PyFiglet version.

Examples include:

```text
standard
slant
big
doom
banner
digital
bubble
block
isometric1
larry3d
lean
mini
script
small
starwars
univers
```

---

# 🎨 Colors

The project includes a dedicated `color.py` module.

Available color families:

* 🔴 Red
* 🟢 Green
* 🔵 Blue
* 🟡 Yellow
* 🟣 Purple
* 🩵 Cyan

Each color family contains multiple ANSI color variants.

Example:

```python
from color import Red

print(
    Red.RED4 +
    "Hello ASCII!" +
    Red.RESET
)
```

---

# 📁 Project Structure

```text
ascii-generator/
│
├── main.py
├── color.py
├── README.md
└── requirements.txt
```

---

# 📦 Requirements

You need:

* Python **3.8+**
* Pillow
* PyFiglet
* A terminal with ANSI color support

### Python

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Enter the project:

```bash
cd YOUR_REPOSITORY
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pillow pyfiglet
```

## 3. Run

```bash
python main.py
```

---

# 📄 requirements.txt

Create a file called:

```text
requirements.txt
```

with:

```text
Pillow
pyfiglet
```

Then install everything with:

```bash
pip install -r requirements.txt
```

---

# 🖥️ Usage

After starting the program:

```text
========================

       ASCII ART

========================

1. Picture -> ASCII
2. Text -> ASCII
3. Exit

Select:
```

## Picture Mode

Select:

```text
1
```

Then enter your image:

```text
Image path: ./images/cat.jpg
```

Choose the width:

```text
Width [80]: 100
```

Then choose a color:

```text
Choose a color:

1. Red
2. Green
3. Blue
4. Yellow
5. Purple
6. Cyan

Color [1]:
```

---

## Text Mode

Select:

```text
2
```

Enter your text:

```text
Enter text: Hello World
```

Choose a font from the available font list.

The program automatically checks which fonts are installed, so invalid font names won't break the application.

---

# 💾 Saving ASCII Art

Both modes support saving the generated ASCII art.

Example:

```text
Save to file? [y/N]: y

Filename [ascii.txt]: cat.txt
```

The resulting file contains the ASCII art without terminal ANSI color codes.

---

# 🛠️ Technologies

This project uses:

### Python

Main programming language.

### Pillow

Used for image processing and conversion.

```bash
pip install pillow
```

### PyFiglet

Used for generating large text-based ASCII art and providing **500+ fonts**.

```bash
pip install pyfiglet
```

### ANSI Escape Codes

Used for terminal colors and text styling.

---

# 🚀 Roadmap

Future features may include:

* [ ] GIF → ASCII
* [ ] Video → ASCII
* [ ] Webcam → ASCII
* [ ] Full RGB image ASCII
* [ ] True-color terminal output
* [ ] Animated ASCII
* [ ] Custom character sets
* [ ] Gradient ASCII
* [ ] Terminal size detection
* [ ] CLI arguments
* [ ] More export formats
* [ ] Configuration file
* [ ] Windows terminal improvements

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit them

```bash
git commit -m "Add my feature"
```

5. Push the branch

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

---

# ⭐ Support

If you like the project, consider giving it a ⭐ on GitHub!

It helps the project grow and motivates future development.

---

# 📜 License

This project is open source.

LICENSE IS IN THE REPO:

```text
MIT License
```

---

<div align="center">

### 🎨 Turn Images & Text Into ASCII Art

**Python • Pillow • PyFiglet • 500+ Fonts • ANSI Colors**

⭐ Star the repository if you like it!

</div>
