import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def shuffle_pixels(image_data, key):
    """Shuffle pixel values based on a simple algorithm.
    
    Args:
        image_data: The image data as a NumPy array.
        key: An integer used for seeding the random number generator.
    
    Returns:
        shuffled_data: The shuffled pixel data as a NumPy array.
    """
    height, width, channels = image_data.shape
    index_array = np.arange(height * width)  # Create an array of indices for the pixels
    np.random.seed(key)  # Ensure reproducibility with the key
    np.random.shuffle(index_array)  # Shuffle the indices randomly

    # Create an array to hold the shuffled pixel data
    shuffled_data = np.zeros_like(image_data)
    
    # Reorder pixels based on the shuffled indices
    for i, new_index in enumerate(index_array):
        row, col = divmod(new_index, width)  # Calculate the original row and column from the index
        shuffled_data[row, col] = image_data[i // width, i % width]  # Assign the shuffled pixel value

    return shuffled_data  # Return the shuffled pixel data

def encrypt_image(input_image_path, key):
    """Encrypt the input image using pixel shuffling.
    
    Args:
        input_image_path: The path to the image file to be encrypted.
        key: An integer used for seeding the random number generator.
    
    Returns:
        encrypted_image_path: The path to the saved encrypted image file.
    """
    try:
        # Open the image file and convert it to a NumPy array
        image = Image.open(input_image_path)
        image_data = np.array(image)
        
        # Shuffle the pixels using the defined key
        encrypted_data = shuffle_pixels(image_data, key)
        
        # Create a new image from the shuffled data and save it
        encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
        encrypted_image_path = os.path.splitext(input_image_path)[0] + "_encrypted.png"
        encrypted_image.save(encrypted_image_path)  # Save the encrypted image
        return encrypted_image_path  # Return the path of the saved image
    except Exception as e:
        # Show an error message if encryption fails
        messagebox.showerror("Error", f"Error encrypting image: {e}")

def decrypt_image(encrypted_image_path, key):
    """Decrypt the encrypted image using the reverse pixel shuffling.
    
    Args:
        encrypted_image_path: The path to the encrypted image file to be decrypted.
        key: An integer used for seeding the random number generator.
    
    Returns:
        decrypted_image_path: The path to the saved decrypted image file.
    """
    try:
        # Open the encrypted image file and convert it to a NumPy array
        encrypted_image = Image.open(encrypted_image_path)
        encrypted_data = np.array(encrypted_image)
        
        height, width, channels = encrypted_data.shape
        index_array = np.arange(height * width)  # Create an array of indices for the pixels
        np.random.seed(key)  # Seed the random number generator with the key
        shuffled_indices = np.random.permutation(index_array)  # Create a shuffled index array
        
        # Create an array to hold the original pixel data
        original_data = np.zeros_like(encrypted_data)

        # Restore the original pixels using the shuffled indices
        for i, original_index in enumerate(index_array):
            row, col = divmod(original_index, width)  # Calculate the original row and column from the index
            original_data[row, col] = encrypted_data[shuffled_indices[i] // width, shuffled_indices[i] % width]  # Assign the original pixel value

        # Create a new image from the original data and save it
        decrypted_image = Image.fromarray(original_data.astype(np.uint8))
        decrypted_image_path = os.path.splitext(encrypted_image_path)[0] + "_decrypted.png"
        decrypted_image.save(decrypted_image_path)  # Save the decrypted image
        return decrypted_image_path  # Return the path of the saved image
    except Exception as e:
        # Show an error message if decryption fails
        messagebox.showerror("Error", f"Error decrypting image: {e}")

def select_file():
    """Open a file dialog to select any file.
    
    Returns:
        file_path: The path to the selected file.
    """
    # Open the file dialog to select any file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*")]
    )
    return file_path  # Return the path of the selected file

def perform_encryption():
    """Handle the encryption button click."""
    input_image = select_file()  # Prompt user to select a file
    if input_image:
        try:
            key = int(key_entry.get())  # Get the key from the entry field
            encrypted_image_path = encrypt_image(input_image, key)  # Encrypt the selected image
            if encrypted_image_path:
                # Show a success message with the path of the encrypted image
                messagebox.showinfo("Success", f"Image encrypted and saved as {encrypted_image_path}")
        except ValueError:
            # Show an error message if the key is invalid
            messagebox.showerror("Error", "Please enter a valid integer key.")

def perform_decryption():
    """Handle the decryption button click."""
    input_image = select_file()  # Prompt user to select a file
    if input_image:
        try:
            key = int(key_entry.get())  # Get the key from the entry field
            decrypted_image_path = decrypt_image(input_image, key)  # Decrypt the selected image
            if decrypted_image_path:
                # Show a success message with the path of the decrypted image
                messagebox.showinfo("Success", f"Image decrypted and saved as {decrypted_image_path}")
        except ValueError:
            # Show an error message if the key is invalid
            messagebox.showerror("Error", "Please enter a valid integer key.")

# Create the main window for the GUI
root = tk.Tk()
root.title("Image Encryption Tool")

# Create and place the widgets in the GUI
tk.Label(root, text="Enter Key (0-255):").pack(pady=10)  # Label for key input
key_entry = tk.Entry(root)  # Entry field for user to input the key
key_entry.pack(pady=5)  # Place the entry field in the GUI

# Buttons to trigger encryption and decryption
tk.Button(root, text="Encrypt Image", command=perform_encryption).pack(pady=20)
tk.Button(root, text="Decrypt Image", command=perform_decryption).pack(pady=20)

# Start the Tkinter main loop to run the application
root.mainloop()
