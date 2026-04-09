
### Color Detection & Barcode Scanning 

A computer vision project that combines real-time **color detection** and **barcode/QR code scanning** using OpenCV, pyzbar, and Pillow.

---

## ✨ Features
- Detect and classify colors in images or live video streams
- Scan and decode barcodes (EAN, UPC, Code128, QR Code, and more)
- Annotated output with bounding boxes and labels
- Supports both static images and real-time webcam input

---

##   Requirements

### Python Dependencies
```txt
numpy==2.4.2
Pillow==12.1.1
opencv-python==4.13.0
pyzbar
```

### System Dependencies
pyzbar requires the zbar shared library installed at the OS level:

**Linux (Ubuntu/Debian)**
```bash
sudo apt-get install libzbar0
```
**macOS**
```bash
brew install zbar
```
**Windows**
Download and install the zbar binary from http://zbar.sourceforge.net/ and make sure the DLL is on your system PATH.

---

##   Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/visionscan.git
cd visionscan

# 2. Install OS-level zbar (see above for your OS)

# 3. Install Python dependencies
pip install -r requirements.txt
```

---

##   Usage

**Color Detection**
```bash
python color_detection.py --image path/to/image.jpg
python color_detection.py --webcam
```

**Barcode Scanning**
```bash
python barcode_scan.py --image path/to/barcode.jpg
python barcode_scan.py --webcam
```


##  Troubleshooting

- **zbar not found** — make sure `libzbar0` (Linux) or `zbar` (macOS) is installed at the OS level, not just via pip
- **OpenCV import error** — try `pip uninstall opencv-python && pip install opencv-python==4.13.0`
- **Windows PATH issue** — restart your terminal after adding the zbar DLL folder to PATH

---

##  License
MIT
