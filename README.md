# Image_Forensic_Tool
Implement image metadata extraction, MD5 hashing and ELA analysis using Python.

# Image Forensic Analysis Tool for Tamper Detection

## 1. Project Overview

The **Image Forensic Analysis Tool for Tamper Detection** is a Python-based mini-project designed to analyze digital images and identify possible signs of image modification.

The tool uses image forensic techniques such as EXIF metadata extraction, MD5 hash generation, and Error Level Analysis (ELA) to examine image integrity.

## 2. Objectives

- To analyze digital images.
- To extract image metadata.
- To generate MD5 hash values.
- To compare original and modified images.
- To identify possible image manipulation using ELA.

## 3. Technologies Used

- **Programming Language:** Python
- **Image Processing:** Pillow
- **Metadata Extraction:** ExifRead
- **Hash Generation:** Hashlib
- **Analysis Technique:** Error Level Analysis (ELA)

## 4. Project Features

1. **EXIF Metadata Extraction:** Extracts available image information such as camera details, date, and software information.
2. **MD5 Hash Generation:** Generates a digital fingerprint for an image.
3. **Hash Comparison:** Compares the hash values of original and modified images.
4. **Error Level Analysis:** Generates an ELA image to visualize possible compression differences.
5. **Image Integrity Verification:** Identifies whether two image files have identical contents.

## 5. Project Structure

```text
Image_Forensic_Tool/
│
├── main.py
├── original.jpg
├── tampered.jpg
├── requirements.txt
├── README.md
└── ela_result.jpg
```

## 6. Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the project folder

```bash
cd Image_Forensic_Tool
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Execute the program

```bash
python main.py
```

### Step 5: Provide image paths

Enter the paths of:
- Original image
- Tampered image

The program analyzes both images and displays the results.

## 7. Expected Output

- Image metadata information.
- Original image MD5 hash.
- Tampered image MD5 hash.
- Image integrity comparison result.
- Generated ELA output image (`ela_result.jpg`).

## 8. Applications

- Digital image forensics.
- Cybersecurity investigations.
- Image authenticity verification.
- Digital evidence analysis.
- Fraud investigation support.

## 9. Limitations

- MD5 comparison verifies file identity, not image authenticity.
- ELA provides indicative results and cannot independently prove tampering.
- Images without EXIF information may not provide metadata.
- Advanced image manipulation may require additional forensic techniques.

## 10. Future Scope

- SHA-256 hash generation.
- Batch image analysis.
- Copy-move forgery detection.
- Graphical User Interface (GUI).
- Machine-learning-based image manipulation detection.

## 11. Conclusion

This project demonstrates how Python can be used for digital image forensic analysis. It combines metadata extraction, MD5 hashing, and Error Level Analysis to examine image files and identify possible modifications.

---

**Project Type:** Mini Project  
**Domain:** Cybersecurity / Digital Forensics  
**Language:** Python  
**Academic Year:** 2026–2027
