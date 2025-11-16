# 🎥 AURORA Media Engine

|[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)](https://www.python.org/)|[![Platform](https://img.shields.io/badge/Platform-Windows-success?logo=windows)](https://www.microsoft.com/)|[![VLC Engine](https://img.shields.io/badge/VLC-Engine-orange?logo=vlc)](https://www.videolan.org/)|[![GitHub Repo](https://img.shields.io/badge/GitHub-AURORA--Media--Engine-lightgrey?logo=github)](https://github.com/bylickilabs)|[![License](https://img.shields.io/badge/License-Closed--Source-important)](#)|
|---|---|---|---|---|

- AURORA Media Engine is a powerful, modern Windows media player built with Python, VLC Engine, and CustomTkinter.  
- It focuses on high-quality playback of local media files (MP4, MKV) combined with SRT subtitle support, language switching, and a clean fullscreen video mode.

> Designed by Thorsten Bylicki — © BYLICKILABS

<br>

---

<br>

## 🚀 Features

| Category | Capabilities |
|----------|--------------|
| Media Support | MP4, MKV, AVI, MOV |
| Subtitles | SRT loading & synchronized display |
| Playback | Play/Pause, Stop, Seekbar, Time Display |
| Audio | Volume control (0–100%) |
| UI/UX | Modern dark UI, Multi-Language (DE/EN) |
| Fullscreen | Borderless fullscreen via double-click |
| Integration | Direct GitHub access from UI |
| Branding | Custom App Icon & Application Metadata |

> 🎯 Focus: Stability, precision, and an intuitive modern user experience

<br>

---

<br>

## ⚙️ Installation

> AURORA Media Engine requires **Python 3.12+** and **VLC runtime libraries** installed on the system.

### 🔹 Install VLC (mandatory)
> Download and install the standard VLC Player for Windows:
  ➡ [VLC](https://www.videolan.org/vlc/)

> During installation, ensure the following:
  - ✔ VLC is installed in default path on Windows
  - ✔ “Web plugins / VLC scripting interfaces” selected  
  - ✔ libvlc is registered system-wide

<br>

---

<br>

### 🔹 Install Python dependencies

> Open PowerShell inside the application folder:

```bylickilabs
pip install -r requirements.txt
```

---

> If a requirements.txt is not yet available, install manually:
```bylickilabs
pip install customtkinter python-vlc
```

---

> Folder structure

```bylickilabs
AURORA_Media_Engine/
│ app.py
└─ requirements.txt
```

---

> Run the Application

```bylickilabs
python app.py
```

---

> 💡 On first launch, you can load:
  - 📝 Optional: SRT subtitle file
  - ▶ Video file

<br>

---

<br>

> 🛑 Common Installation Problem

| Issue | Cause | Fix |
|-------|-------|-----|
| FileNotFoundError: libvlc.dll | VLC runtime not found | Install VLC 64-bit |
| App starts but no video | VLC not configured correctly | Reinstall VLC |

<br>

---

<br>

## 🎬 Usage Guide

> Once the application is running, the main interface provides intuitive playback controls.

### ▶️ Opening Media

1. Click **“Open Video”**
2. Select a local media file  
   Supported formats: `.mp4`, `.mkv`, `.avi`, `.mov`

> (Optional) To add subtitles:
  - 1. Click **“Open Subtitle”**
  - 2. Select an `.srt` file  
    - → Subtitles will load automatically

<br>

---

<br>

### 🕹 Playback Control

| Control | Description |
|---------|-------------|
| Play/Pause | Starts or pauses the video |
| Stop | Stops playback immediately |
| Seekbar | Drag to jump forward/backward |
| Time Display | Shows current & total runtime |

> Volume can be adjusted with the **Volume slider** (0–100%).

<br>

---

<br>

### 🌍 Language Switching (DE/EN)

> Click on the **DE / EN** buttons in the upper-right area:
  - ✔ UI text instantly updates  
  - ✔ Playback continues uninterrupted  
  - ✔ No restart required

<br>

---

<br>

### 🖥 Fullscreen Mode

| Action | Result |
|--------|--------|
| Double-click video | Toggle fullscreen on/off |

---

> 🖼 In fullscreen mode:
  - ✔ Playback controls and top bar are hidden  
  - ✔ Only the video is visible

<br>

---

<br>

### ℹ Application Information

> Click **Info** to open the information dialog:

Includes:
- App Name & Version
- Developer / Company Name
- Quick access links:
  - Website
  - GitHub
  - Support Email

<br>

---

<br>

### 💡 Quality Tip

> To ensure the best subtitle display:
  - Keep `.srt` and video file named similarly
  - Place both files in the same folder

> Enjoy a modern and focused playback experience with a minimal interface and full control.

<br>

---

<br>

## ⚖️ License & Legal Notice

> AURORA Media Engine is a proprietary software product.
  - All rights are exclusively reserved by:

**© Thorsten Bylicki — © BYLICKILABS**  
  - All trademarks and brand names are the property of their respective owners.
  - [LICENSE](LICENSE)

<br>

---

<br>

### VLC / Third-Party Components

>AURORA Media Engine makes use of the **VLC media playback engine**.
 - You must comply with the associated licenses and terms provided by:

🔗 [VLC LEGAL](https://www.videolan.org/legal.html)

> All other dependencies remain the intellectual property of their authors.

<br>

---

<br>

### Legal Disclaimer

> This software is provided **as-is**, without any warranties.  
  - The developer assumes no liability for:
    - Data loss
    - Hardware damage
    - Malfunction caused by third-party libraries
    - Incorrect installation

> Any usage is at the user’s own risk.

<br>

---

<br>

### Contact

- 📧 Support: **bylicki@mail.de**  
- 🌐 Website: **https://www.bylickilabs.de**  
- 🐙 GitHub: **https://github.com/bylickilabs**

---

**AURORA Media Engine**  
- Built with pride, precision, and passion for advanced media technology.

---
