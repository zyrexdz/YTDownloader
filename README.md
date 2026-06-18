<h1 align="center">
  ⚡ Zyre Downloader ⚡
</h1>

<p align="center">
  <strong>The fastest, sleekest, and most efficient YouTube downloader built in Python.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/platform-windows-lightgray.svg" alt="Platform">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

## 🚀 Overview

**Zyre Downloader** is a beautifully designed, highly optimized terminal based YouTube downloading tool. Powered by the incredible `yt-dlp` backend and the `rich` UI library, it offers very fast downloads and a stunning command line interface

Forget messy commands and full of ads software. Zyre Downloader gives you a premium, simple interface that just works and it even compiles itself into a standalone global executable for you!

## ✨ Features

- 🏎️ **Very Fast:** Utilizes concurrent fragment downloading to maximize your bandwidth.
- 🎨 **Stunning UI:** Custom ASCII banners, dynamic progress bars, and colored terminal menus.
- 🎵 **Multiple Formats:** Easily grab MP4, MP3, lossless WAV, the "Best Available" combination, or input your own custom format extension.
- 🧠 **Smart FFmpeg Detection:** Automatically detects if your system is missing `FFmpeg` (required for audio conversion) and provides an interactive, copy-paste guide to install it.
- 🛠️ **Auto-Build & Global Install:** Includes a seamless `run.bat` setup script that installs dependencies, compiles the script into a standalone `.exe`, and optionally installs it globally so you can run `ytdownload` from anywhere on your PC!

## 📦 Installation & Usage

You don't even need to touch the Python code to get started.

1. **Clone or Download the repository:**
   ```bash
   git clone https://github.com/zyrexdz/YTDownloader
   cd YTDownloader
   ```

2. **Run the Setup Script (Windows):**
   Simply double-click **`run.bat`**.
   
   The script will automatically:
   - Install required Python dependencies (`yt-dlp` and `rich`).
   - Install `pyinstaller` and compile the code into a lightning-fast `.exe` file.
   - Ask if you want to install Zyre Downloader globally to your Command Prompt.

3. **Enjoy!**
   If you chose the global install, you can now open *any* Command Prompt or PowerShell window and simply type:
   ```cmd
   ytdownload
   ```
   to launch the downloader instantly!

## 🔧 Manual Setup (Developers)

If you prefer to run the raw Python script yourself:

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python ytdownload.py
   ```

## 📝 Requirements
- Python 3.7+
- [FFmpeg](https://ffmpeg.org/) (Highly recommended for MP3/WAV audio extraction)
- `yt-dlp`
- `rich`

## 🤝 Contributing
Pull requests are welcome! If you have ideas for cooler animations or faster downloading protocols, feel free to open an issue or submit a PR.

## 📄 License
This project is open-source and available under the [MIT License](https://github.com/zyrexdz/YTDownloader/blob/main/LICENSE). Stay cool! 😎
