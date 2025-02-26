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

### Screenshots:

- The main GUI to perform encryption and decryption:
  
  ![image](https://github.com/user-attachments/assets/ef44b5a2-d783-42d3-abfd-787cd53d37b8)

- The confirmation message that appears after encryption:     

  ![image](https://github.com/user-attachments/assets/4ad176f6-f01b-4792-a2b1-4c44484ecc80)

- The message that appears after correct passcode is entered to view the secret message:

  ![image](https://github.com/user-attachments/assets/678d7d3a-b869-4871-b780-c8f83aa88ff6)

- The message that appears after incorrect passcode is entered to view the secret message:

  ![image](https://github.com/user-attachments/assets/73469f2e-0bdc-44c2-b8da-d53ead86ecf4)

- The demo is the image before a hidden message is added to it and demo_encrypted is the image in which a secret message is present.
- They both look the same but using the correct passcode the secret message can be seen.

  ![image](https://github.com/user-attachments/assets/4e8ee3a1-c3ed-47dc-956b-6400b0192310)

  
### Conclusion:

This project demonstrates a secure and user-friendly approach to steganography using Python.
The passcode-based decryption ensures that only authorized users can retrieve hidden messages.
The GUI interface makes it easy for anyone to use without technical expertise.
Future enhancements can include support for multiple file types, video steganography, and AI-driven security improvements.

### License:
This project is licensed under the MIT License.
