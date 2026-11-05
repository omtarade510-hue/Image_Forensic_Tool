
import hashlib
import exifread
import os
from PIL import Image, ImageChops, ImageEnhance

# 1. Generate MD5 Hash
def generate_hash(image_path):
    hasher = hashlib.md5()

    with open(image_path, 'rb') as file:
        hasher.update(file.read())

    return hasher.hexdigest()


# 2. Extract Metadata
def extract_metadata(image_path):
    print("\n--- IMAGE METADATA ---")

    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file)

    if not tags:
        print("No EXIF metadata found.")
    else:
        for tag in tags:
            print(tag, ":", tags[tag])


# 3. Error Level Analysis
def error_level_analysis(image_path):
    original = Image.open(image_path).convert("RGB")

    folder = os.path.dirname(os.path.abspath(image_path))
    temp_path = os.path.join(folder, "compressed_temp.jpg")
    output_path = os.path.join(folder, "ela_result.jpg")

    original.save(temp_path, "JPEG", quality=95)

    compressed = Image.open(temp_path)
    diff = ImageChops.difference(original, compressed)

    diff = ImageEnhance.Brightness(diff).enhance(30)
    diff.save(output_path)

    compressed.close()
    os.remove(temp_path)

    print("ELA image saved:", output_path)


# MAIN PROGRAM
print("IMAGE FORENSIC ANALYSIS TOOL")

original_path = input("Enter original image path: ")
tampered_path = input("Enter tampered image path: ")

if not os.path.isfile(original_path) or not os.path.isfile(tampered_path):
    print("Error: Image file not found.")

else:
    print("\nORIGINAL IMAGE ANALYSIS")
    extract_metadata(original_path)
    hash1 = generate_hash(original_path)
    print("Original MD5 Hash:", hash1)

    print("\nTAMPERED IMAGE ANALYSIS")
    extract_metadata(tampered_path)
    hash2 = generate_hash(tampered_path)
    print("Tampered MD5 Hash:", hash2)

    print("\n--- INTEGRITY RESULT ---")

    if hash1 == hash2:
        print("Both images have identical file contents.")
    else:
        print("Images are different. Possible modification detected.")

    print("\n--- ELA ANALYSIS ---")
    error_level_analysis(tampered_path)

    print("\nAnalysis Completed Successfully!")
