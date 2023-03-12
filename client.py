"""
This script creates a dictionary, writes its content to a text file, serialises it, 
encrypts the text file, and sends both the serialised dictionary and the encrypted text file 
to a server using HTTP POST. The user is prompted to specify the pickling format, and whether 
or not to encrypt the text file.

Usage:
    Run the script, and follow the prompts to specify the pickling format and encryption 
    options. The serialised dictionary and encrypted text file will be sent to the specified 
    server using HTTP POST.
"""

# pylint: disable=C0103
# pylint: disable=W0702

import base64
import json
import pickle
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
import requests
from cryptography.fernet import Fernet

# Variable declarations.
server_host = "localhost"
server_port = 8080
request_timeout = 60

# Define file names.
date_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
text_file_name = f"client_text_file_{date_str}.txt"

try:
    # Print a message indicating that the dictionary is being created.
    print("Creating dictionary...\n")

    # Create a dictionary with some key-value pairs.
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}

    # Print a message indicating that the dictionary was created, along with its contents.
    print(f"Created dictionary:\n{my_dict}\n")
except:
    # If an exception occurs, print an error message and exit the programme.
    print("Error occurred while creating dictionary. \n")
    sys.exit()

try:
    # Print a message indicating that a text file is being created.
    print("Creating text file...\n")

    # Open the text file in write mode and write some text to it.
    with open(text_file_name, "w", encoding="utf-8") as write_text_file:
        write_text_file.write("This is a text file written by my Python script. \n")
        write_text_file.write(f"Date (UTC): {datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')}")

    # Open the text file in read mode and read its contents into a variable.
    with open(text_file_name, "r", encoding="utf-8") as read_text_file:
        text_file_content = read_text_file.read()

    # Print a message indicating that the text file was created, along with its contents.
    print(f"Created text file with following content: \n{text_file_content}\n")
except:
    # If an exception occurs, print an error message and exit the programme.
    print("Error occurred while creating or reading text file. \n")
    sys.exit()

try:
    # Ask the user to enter a pickling format and convert it to uppercase.
    pickling_format = input("Enter the pickling format (BINARY, JSON, or XML): ")
    pickling_format = pickling_format.upper()

    # Depending on the specified format, pickle the dictionary accordingly.
    if pickling_format == "BINARY":
        serialised_dict = base64.b64encode(pickle.dumps(my_dict))
    elif pickling_format == "JSON":
        serialised_dict = json.dumps(my_dict)
    elif pickling_format == "XML":
        root = ET.Element('dict')
        for key, value in my_dict.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        serialised_dict = ET.tostring(root)
    else:
        # If the specified format is invalid, print an error message and use JSON format.
        print("Invalid pickling format. ")
        pickling_format = "JSON"
        serialised_dict = json.dumps(my_dict)

    # Print a message indicating which format was used to pickle the dictionary.
    print(f"Using {pickling_format} format. \n")

    # Print the serialised dictionary in the specified format.
    print(f"Serialised dictionary ({pickling_format}): \n{serialised_dict}\n")
except:
    # If an exception occurs, print an error message and exit the programme.
    print("Error occurred while processing dictionary. \n")
    sys.exit()

try:
    # Ask the user whether to encrypt the text file.
    encrypt = input("Do you want to encrypt the text file? (yes or no): ")

    if encrypt == "yes":
        # If the user wants to encrypt the text file, encrypt it using Fernet encryption.
        is_encrypted = "1"
        encryption_key = Fernet.generate_key()
        fernet = Fernet(encryption_key)
        text_file_encrypted = fernet.encrypt(bytes(text_file_content, encoding="utf-8"))
    else:
        # If the user doesn't want to encrypt the text file,
        # set the encryption key and encrypted text to default values.
        is_encrypted = "0"
        encryption_key = b""
        text_file_encrypted = text_file_content
except:
    # If an exception occurs, print an error message and exit the programme.
    print("Error occurred while processing text file. \n")
    sys.exit()

try:
    # Print message indicating sending serialised dictionary and text file via HTTP POST to server.
    print("Sending serialised dictionary and text file to server using HTTP POST...\n")

    # Send HTTP POST request with serialised dictionary as data and text file as files.
    response = requests.post(f"http://{server_host}:{server_port}",
                            data={ "SerialisedDictionary": serialised_dict },
                            files={ "TextFile": (text_file_name, text_file_encrypted) },
                            headers={
                                "IsEncrypted": is_encrypted,
                                "EncryptionKey": base64.b64encode(encryption_key),
                                "PicklingFormat": pickling_format
                                },
                            timeout=request_timeout)

    # Check if request was successful (status code 200).
    if response.status_code == 200:
        # Print success message along with response status code and content.
        print("Successfully sent serialised dictionary and text file. ")
        print(f" - Response Status: {response.status_code}")
        print(f" - Response Content: {response.text}")
    else:
        # Print failure message along with response status code and content.
        print("Failed to send serialised dictionary and text file. ")
        print(f" - Response Status: {response.status_code}")
        print(f" - Response Content: {response.text}")
except:
    # If an exception occurs, print an error message and exit the programme.
    print("Error occurred while sending request HTTP POST request to server. \n")
    sys.exit()
