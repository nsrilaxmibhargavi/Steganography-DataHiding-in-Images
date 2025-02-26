# Steganography-DataHiding-in-Images

### Project Overview:
This project implements image steganography using Python, allowing users to securely hide and retrieve secret messages within images. It features a passcode-based security layer, ensuring that only authorized users can decrypt hidden data. The GUI, built with Tkinter, makes encryption and decryption easy and accessible for all users.

### Installation of this Repository:
- __Clone the Repository__: Open your terminal or command prompt and run <br>


               git clone https://github.com/nsrilaxmibhargavi/Steganography-DataHiding-in-Images.git

  
- __Navigate to the project directory:__
  cd Steganography-DataHiding-in-Images

- __Install the required Dependencies__
- __Run the Application__



### Working

- __Encryption Process:__

        - Select an image file to embed the secret message.
        - Enter the message and a passcode for security.
        - The program hides the message within the image using pixel manipulation and saves an encrypted copy.

- __Decryption Process:__

        - Load the encrypted image.
        - Enter the correct passcode to extract the hidden message.
        - If the passcode matches, the message is revealed; otherwise, access is denied.
  
### Conclusion:

This project demonstrates a secure and user-friendly approach to steganography using Python.
The passcode-based decryption ensures that only authorized users can retrieve hidden messages.
The GUI interface makes it easy for anyone to use without technical expertise.
Future enhancements can include support for multiple file types, video steganography, and AI-driven security improvements.

### License:
This project is licensed under the MIT License.
