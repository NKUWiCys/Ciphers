# coding demonstration for WiCys on cryptography libraries

# importing the libraries
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

if __name__ ==  "__main__":
    print("Welcome to the WiCys Cryptography Libraries Demonstration!")
    text = input("Enter a message to encrypt: ")
    
    # step 1: create a key
    #AES supports 32,  64 or 128 bytes keys
    key = os.urandom(32)
    
    # step2: create an initialization vector
    iv = os.urandom(16)
    
    # step 3: create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    
    # step 4: create an encryptor object
    encryptor = cipher.encryptor()
    
    # step 5: create a decryptor object
    decryptor = cipher.decryptor()
    
    # step 6: create a padding object - needs to be a multiple of 16 bytes
    padder = padding.PKCS7(128).padder()
    unpadder  = padding.PKCS7(128).unpadder()
    
    # step 7: pad the data
    paddedText = padder.update(text.encode()) + padder.finalize()
    
    # step 8: encrypt the text
    ciphertext = encryptor.update(paddedText) + encryptor.finalize()
    print("Encrypting....")
    print("Encrypted text: " + str(ciphertext))
    
    # step 9: decrypt the text
    print("Decrypting....")
    decryptedText = decryptor.update(ciphertext) + decryptor.finalize()
    text = unpadder.update(decryptedText) + unpadder.finalize()
    print("Decrypted text: " + text.decode())
    
