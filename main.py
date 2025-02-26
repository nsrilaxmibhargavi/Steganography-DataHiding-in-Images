import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import cv2
import numpy as np
import os

class SteganographyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Data Hiding in Images")
        self.geometry("650x700")
        self.configure(bg="#f0f0f0")
        self.resizable(False, False)
        
        
        self.setup_styles()
        
       
        self.create_encrypt_section()
        self.create_decrypt_section()

    def setup_styles(self):
        style = ttk.Style(self)
        
        style.theme_use('clam')
        style.configure("TLabel", font=("Helvetica", 11), background="#f0f0f0")
        style.configure("TButton", font=("Helvetica", 11), padding=5)
        style.configure("TEntry", font=("Helvetica", 11))
        style.configure("TLabelframe", font=("Helvetica", 12, "bold"), background="#e0e0e0", padding=10)
        style.configure("TLabelframe.Label", background="#e0e0e0")

    def create_encrypt_section(self):
        encrypt_frame = ttk.LabelFrame(self, text="Encrypt")
        encrypt_frame.pack(fill="x", padx=20, pady=15, ipady=10)

       
        for i in range(3):
            encrypt_frame.columnconfigure(i, weight=1, pad=10)

        
        ttk.Label(encrypt_frame, text="Select Image File:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.encrypt_image_path = tk.StringVar()
        self.encrypt_image_entry = ttk.Entry(
            encrypt_frame, textvariable=self.encrypt_image_path, width=40
        )
        self.encrypt_image_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        ttk.Button(encrypt_frame, text="Browse", command=self.browse_encrypt_image).grid(
            row=0, column=2, padx=10, pady=10, sticky="e"
        )

        ttk.Label(encrypt_frame, text="Enter Secret Message:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.secret_message = tk.StringVar()
        self.message_entry = ttk.Entry(
            encrypt_frame, textvariable=self.secret_message, width=40
        )
       
        self.message_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew", columnspan=2)

        
        ttk.Label(encrypt_frame, text="Enter Passcode:").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        self.encrypt_password = tk.StringVar()
        self.password_entry = ttk.Entry(
            encrypt_frame, textvariable=self.encrypt_password, width=40, show="*"
        )
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew", columnspan=2)

        
        ttk.Button(encrypt_frame, text="Encrypt Image", command=self.encrypt_image).grid(
            row=3, column=0, columnspan=3, padx=10, pady=20, sticky="ew"
        )

    def create_decrypt_section(self):
        decrypt_frame = ttk.LabelFrame(self, text="Decrypt")
        decrypt_frame.pack(fill="x", padx=20, pady=15, ipady=10)

       
        for i in range(3):
            decrypt_frame.columnconfigure(i, weight=1, pad=10)

        
        ttk.Label(decrypt_frame, text="Select Encrypted Image:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.decrypt_image_path = tk.StringVar()
        self.decrypt_image_entry = ttk.Entry(
            decrypt_frame, textvariable=self.decrypt_image_path, width=40
        )
        self.decrypt_image_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        ttk.Button(decrypt_frame, text="Browse", command=self.browse_decrypt_image).grid(
            row=0, column=2, padx=10, pady=10, sticky="e"
        )

       
        ttk.Label(decrypt_frame, text="Enter Passcode:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.decrypt_password = tk.StringVar()
        self.decrypt_password_entry = ttk.Entry(
            decrypt_frame, textvariable=self.decrypt_password, width=40, show="*"
        )
        self.decrypt_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew", columnspan=2)

        
        ttk.Button(decrypt_frame, text="Decrypt Image", command=self.decrypt_image).grid(
            row=2, column=0, columnspan=3, padx=10, pady=20, sticky="ew"
        )

    def browse_encrypt_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image File", 
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")]
        )
        if file_path:
            self.encrypt_image_path.set(file_path)

    def browse_decrypt_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Encrypted Image", 
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")]
        )
        if file_path:
            self.decrypt_image_path.set(file_path)

  
    def encrypt_image(self):
        image_path = self.encrypt_image_path.get()
        message = self.secret_message.get()
        password = self.encrypt_password.get()

        if not image_path or not message or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        img = cv2.imread(image_path)
        if img is None:
            messagebox.showerror("Error", "Selected image file could not be read.")
            return

       
        directory, filename = os.path.split(image_path)
        name, _ = os.path.splitext(filename)
        output_filename = f"{name}_encrypted.png"
        output_path = os.path.join(directory, output_filename)

        n, m, z = 0, 0, 0


        img[n, m, z] = np.uint8(len(password))
        img[n+1, m+1, (z+1) % 3] = np.uint8(len(message))
        n += 2
        m += 2
        z = (z+2) % 3

       
        for char in password + message:
            img[n, m, z] = np.uint8(ord(char))
            n += 1
            m += 1
            z = (z+1) % 3

        try:
            cv2.imwrite(output_path, img)
            messagebox.showinfo("Success", f"Image encrypted successfully!\nSaved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save encrypted image.\n{e}")

 
    def decrypt_image(self):
        image_path = self.decrypt_image_path.get()
        password_attempt = self.decrypt_password.get()

        if not image_path or not password_attempt:
            messagebox.showwarning("Input Error", "Please select an image and enter the passcode.")
            return

        img = cv2.imread(image_path)
        if img is None:
            messagebox.showerror("Error", "Selected image file could not be read.")
            return

        try:
            
            password_length = int(img[0, 0, 0])
            message_length = int(img[1, 1, (0+1) % 3])
            total_chars = password_length + message_length

           
            h, w, _ = img.shape
            available_steps = min(h, w) - 2
            if total_chars > available_steps:
                messagebox.showerror("Error", "The selected image does not appear to have any hidden message.")
                return

            n, m, z = 2, 2, (0+2) % 3

            
            extracted_password = ""
            for _ in range(password_length):
                extracted_password += chr(int(img[n, m, z]))
                n += 1
                m += 1
                z = (z+1) % 3

            if extracted_password != password_attempt:
                messagebox.showerror("Error", "Incorrect passcode! Decryption failed.")
                return

    
            message = ""
            for _ in range(message_length):
                message += chr(int(img[n, m, z]))
                n += 1
                m += 1
                z = (z+1) % 3

            messagebox.showinfo("Decrypted Message", f"Secret Message:\n{message}")

        except Exception:
            messagebox.showerror("Error", "The selected image does not appear to have hidden data.")

if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()
