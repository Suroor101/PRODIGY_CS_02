

# **Image Encryption Tool**  

This Python program allows you to **encrypt** and **decrypt images** using a pixel-shuffling algorithm. It comes with a **Tkinter GUI** for a smooth user experience. The tool ensures your images remain secure with a unique key-based encryption process.  

---

## **Features**  
- **Encrypt Images**: Secure your images using a custom pixel-shuffling method.  
- **Decrypt Images**: Restore encrypted images back to their original form.  
- **User-Friendly GUI**: Simple interface to upload and process images.  
- **Cross-Platform**: Works on any system with Python and necessary libraries installed.  

---

## **Requirements**  
- Python 3.x  
- Required Libraries:  
  - `numpy`  
  - `Pillow` (PIL)  
  - `tkinter` (comes pre-installed with Python)  

---

## **How to Run the Program**  
1. **Clone or Download the Repository**  
   ```bash
   git clone https://github.com/Suroor101/PRODIGY_CS_02.git
   cd PRODIGY_CS_02
   ```

2. **Install Required Libraries**  
   ```bash
   pip install numpy pillow
   ```

3. **Run the Program**  
   ```bash
   python image_encryption.py
   ```  

---

## **How to Use**  

1. Launch the program.  
2. Enter an **encryption key** (a number between 0 and 255).  
3. Choose to **Encrypt** or **Decrypt** an image:  
   - Click "Encrypt" to secure your image.  
   - Click "Decrypt" to restore your encrypted image.  
4. Use the file dialog to select an image file.  
5. The processed image is saved automatically in the same directory with a modified file name (`_encrypted` or `_decrypted`).  

---

## **Important Notes**  
- The same key used for encryption must be used for decryption to restore the original image.  
- Supported file formats: `.png`, `.jpg`, `.jpeg`.  

