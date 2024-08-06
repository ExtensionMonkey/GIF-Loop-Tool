# Simple Reddit GIF Looper

**Description:**
Simple Reddit GIF Looper is a user-friendly application designed for creating looping GIFs with ease. The tool allows users to load a GIF, set the frame rate, upscale the image, and save the modified version. It features a straightforward GUI implemented using Tkinter, making it accessible for users of all levels.

**Features:**
- **Load GIFs**: Easily load GIF files from your computer.
- **Frame Rate Adjustment**: Set the desired frame rate (1-120 fps) for the output GIF.
- **Upscaling Options**: Choose from various upscaling factors (None, x2, x4, x8) to resize the GIF.
- **Looping**: Automatically creates a looping effect by reversing and appending frames.
- **Save Modified GIFs**: Save the processed GIF to your desired location.
- **Interactive Labels**: Labels providing information about the original and output GIF sizes.
- **Attribution and Donation Links**: Links to the creator’s Reddit profile and a donation page.

**Technical Details:**
- **GUI Framework**: Tkinter
- **Image Processing**: PIL (Pillow) library
- **Multithreading**: Ensures smooth performance during GIF processing
- **File Dialogs**: Used for loading and saving GIF files

**Usage Instructions:**
1. **Load a GIF**: Click on "Load GIF" to select a GIF file from your computer.
2. **Set Frame Rate**: Enter the desired frame rate in the provided entry box.
3. **Choose Upscaling**: Select an upscaling option if you wish to resize the GIF.
4. **Save GIF**: Click on "Save GIF" to save the processed GIF. The application will process the GIF in a separate thread and display a success message upon completion.

**Installation:**
Ensure you have Python and the required libraries installed:

```python
pip install tkinter Pillow

python GifLooper.py
