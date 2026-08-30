# File Organizer

A simple Python project that automatically sorts files in the current folder into categorized folders such as Images, Documents, Audio, Videos, Archives, and Scripts.

## What it does

The script scans the working directory and moves each file into a matching folder based on its extension.

Examples:
- `.jpg`, `.png` → `Images`
- `.pdf`, `.txt`, `.docx` → `Documents`
- `.mp3`, `.wav` → `Audio`
- `.mp4`, `.avi` → `Videos`
- `.zip`, `.rar` → `Archives`
- `.js`, `.html`, `.css` → `Scripts`

Files that do not match any known type are placed in an `Others` folder.

## Files in the project

- `main.py` – organizes files in the current directory

## How to run

1. Open the project folder.
2. Make sure Python is installed.
3. Run the script:

```bash
python main.py
```

## Notes

- The script uses the current working directory.
- It creates the required folders automatically if they do not exist.
- It skips directories and only organizes files.

## Example

If your folder contains:
- `photo.jpg`
- `notes.txt`
- `song.mp3`

Running the script will place them into:
- `Images/photo.jpg`
- `Documents/notes.txt`
- `Audio/song.mp3`
