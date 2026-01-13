# BackgroundRemoverCD

A simple desktop application for removing backgrounds from images. Built with Python and `customtkinter`, this tool provides a user-friendly interface to quickly process your photos and save a version with a transparent background.

## Features

*   **Intuitive UI:** Clean and straightforward interface built with CustomTkinter.
*   **Local File Selection:** Easily browse and select images from your computer.
*   **Side-by-Side Preview:** Instantly compare the original image with the background-removed result.
*   **Automatic Saving:** The processed image is automatically saved to your user's "Downloads" folder.
*   **Cross-Platform:** Compatible with Windows, macOS, and Linux.

## How It Works

The application uses the `withoutbg` library to process the selected image and remove its background. The graphical user interface is rendered using `customtkinter`, providing a modern look and feel.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/David-Cabu/BackgroundRemoverCD.git
    cd BackgroundRemoverCD
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install customtkinter Pillow withoutbg
    ```
    *Note: You may also need to provide the application icon files (`logoBackgroundRemoverCD.ico` and `logoBackgroundRemoverCD.png`) in the root directory or update the paths in `AppGraphics.py`.*

## Usage

1.  Navigate to the cloned repository's directory.

2.  Run the application:
    ```bash
    python Main.py
    ```

3.  Click the **Search** button to select an image file from your system.

4.  A preview of your selected image will be displayed on the left.

5.  Click the **Remove** button at the bottom of the window.

6.  The application will process the image. Once complete, a preview of the image with a transparent background will appear on the right.

7.  The final image is saved in your "Downloads" folder with the suffix `_WithoutBackground.png`. The full path to the saved file will be displayed at the bottom of the application window.
