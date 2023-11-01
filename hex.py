# By: Shuban Pal
# Algorithm: Hexadecimal
# Project: CSP Passion Project
# Date: 2023

import binascii

class hexadecimal:
  def __init__(self, text):
    self.text = text
  def encrypt(enc): # Main encryption algorithm
    encbytes = enc.text.encode('utf-8') # Encode the text to hex bytes
    hexverse = binascii.hexlify(encbytes) # Make the encbytesinto actual hex
    hex_string = hexverse.decode('utf-8') # Decode into a hex string
    return hex_string 

  def decrypt(dec): # Main decryption algorithm
    dec.text = dec.text.replace("0x", "") # Get rid of the "0x" in front if present in some hex representations
    bytes_object = bytes.fromhex(dec.text) # Get the bytes from the hex
    pt = bytes_object.decode("ASCII") # Decode into ASCII
    return pt

mycipher = hexadecimal("Hello World") 
print(mycipher.encrypt())

cipher2 = hexadecimal("48656c6c6f20576f726c64")
print(cipher2.decrypt())
