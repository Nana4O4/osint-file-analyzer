
# OSINT File Analyzer

A beginner-friendly Python project for analyzing local image files.

## Features

- Extract file name and extension
- Calculate file size
- Read last modification timestamp
- Calculate SHA-256 and MD5 hashes
- Extract available EXIF metadata
- Handle unrecognized image files
- Export results to JSON

## Technologies

- Python
- Pillow
- pathlib
- hashlib
- json

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

Place a sample image in the `samples` folder.

Update the image path in `main.py`.

Run:

```bash
python main.py
```

The program creates a `report.json` file.

## Limitations

- The input path is currently hard-coded.
- Some images do not contain EXIF metadata.
- MD5 should not be used for security-sensitive integrity verification.
- The tool does not prove the authenticity of an image.
