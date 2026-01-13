<div align="center">

  <!-- Sostituisci questo link con il link reale al tuo logo se lo carichi nella repo -->
  <img src="logoBackgroundRemoverCD.png" alt="logo" width="120" height="auto" />
  
  # BackgroundRemoverCD
  
  **Remove image backgrounds instantly with a modern desktop interface.**

  <!-- BADGES - Puoi personalizzarli su shields.io -->
  ![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
  ![UI](https://img.shields.io/badge/UI-CustomTkinter-green.svg)
  ![License](https://img.shields.io/badge/license-MIT-orange.svg)
  ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

  [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Roadmap](#-roadmap)

</div>

---

## 📖 Overview

**BackgroundRemoverCD** is a simple yet powerful desktop application designed to remove backgrounds from images automatically. Built with Python and `customtkinter`, it offers a sleek, modern, and user-friendly interface. Whether you need transparent assets for design work or just want to clean up a photo, this tool handles it with a single click.

## 🖼️ Screenshots

<!-- Fai uno screenshot della tua app con il "Prima" e "Dopo" e salvalo nella cartella del progetto come 'demo.png' o carica una GIF -->
![App Screenshot](path/to/your/screenshot_or_demo.gif)
*(Example: Side-by-side comparison of the original image and the processed result)*

## ✨ Features

*   **🎨 Intuitive UI:** A clean, dark-mode friendly interface built with CustomTkinter.
*   **📂 Local File Selection:** Easy system-native dialogs to browse and select images.
*   **👁️ Live Preview:** Instantly compare the original image with the background-removed result side-by-side.
*   **💾 Auto-Save:** Processed images are automatically saved to your `Downloads` folder with zero friction.
*   **💻 Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.

## 🛠️ Tech Stack

*   **Python:** Core logic.
*   **CustomTkinter:** Modern GUI library based on Tkinter.
*   **Pillow (PIL):** Image manipulation and handling.
*   **WithoutBG:** The engine behind the background removal magic.

## 🚀 Installation

### Prerequisites
Ensure you have Python installed (version 3.x is recommended).

### Step-by-Step Guide

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/David-Cabu/BackgroundRemoverCD.git
    cd BackgroundRemoverCD
    ```

2.  **Create a Virtual Environment (Optional but Recommended):**
    *   *Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   *macOS/Linux:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install customtkinter Pillow withoutbg
    ```
    *Or, if a requirements file is present:*
    ```bash
    pip install -r requirements.txt
    ```

    > **Note:** Ensure `logoBackgroundRemoverCD.ico` and `logoBackgroundRemoverCD.png` are in the root directory for the app icon to load correctly.

## 🕹️ Usage

1.  Run the application:
    ```bash
    python Main.py
    ```
2.  Click **Search** to select an image (`.jpg`, `.png`, etc.).
3.  Review the original image in the left preview pane.
4.  Click **Remove** at the bottom.
5.  Wait a moment for the magic to happen. The transparent result will appear on the right.
6.  Check your **Downloads** folder for the file ending in `_WithoutBackground.png`.



##🔜 Roadmap

- [ ] Add support for batch processing (multiple images at once).
- [ ] Allow users to choose a custom save location.
- [ ] Add drag-and-drop functionality.
- [ ] Add a loading spinner during processing.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
