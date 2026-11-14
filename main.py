from pathlib import Path
from datetime import datetime
import json
import hashlib
from PIL import Image
from PIL import UnidentifiedImageError

photo = Path("samples/sample.jpg")

if photo.is_file():
    print("file found")
    print("File name:", photo.name)
    print("Extension:", photo.suffix)

    size = photo.stat().st_size
    print("File Size:", size, "bytes")

    size_kiB = size / 1024
    print("File Size(kiB):", round(size_kiB, 2))

    modified_time = photo.stat().st_mtime
    print("Modified timeset:", modified_time)

    readable_time = datetime.fromtimestamp(modified_time)
    print("Last Modified:", readable_time)

    with open(photo, "rb") as image_file:
        file_data = image_file.read()

    sha256_hash = hashlib.sha256(file_data).hexdigest()
    print("SHA-256:", sha256_hash)

    md5_hash = hashlib.md5(file_data).hexdigest()
    print("MD5:", md5_hash)

    try:
        with Image.open(photo) as img:
            exif_data = img.getexif()
        image_valid = True

    except UnidentifiedImageError:
        print("Invalid image file")
        exif_data = {}
        image_valid = False

    exif_dict = dict(exif_data)
    print("EXIF:", exif_dict)

    report = {
        "file_name": photo.name,
        "extension": photo.suffix,
        "size_bytes": size,
        "size_kib": round(size_kiB, 2),
        "last_modified": str(readable_time),
        "sha256": sha256_hash,
        "md5": md5_hash,
        "exif": exif_dict,
        "image_valid": image_valid,
    }

    print(report)

    with open("report.json", "w", encoding="utf-8") as output_file:
        json.dump(report, output_file, indent=4)

        print("Report saved successfully!")


else:
    print("file not found")
