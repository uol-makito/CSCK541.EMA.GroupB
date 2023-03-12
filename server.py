"""
This script defines a HTTP server that can receive serialised dictionaries and encrypted text
files via HTTP POST requests, and then deserialise and decrypt them respectively. It also provides
options to print and/or save the received contents.

Usage:
    Run the script, and enter "print", "save", or "both" to choose how to process the received
    contents. Send HTTP POST requests to the server's address with a serialised dictionary and
    an encrypted text file in the format specified in the request headers. The script will then
    deserialise and decrypt the received contents, and optionally print and/or save them.
"""

# pylint: disable=C0103
# pylint: disable=W0702

import base64
import cgi
import json
import pickle
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.fernet import Fernet

# Variable declarations.
server_port = 8080
receive_print = 1
receive_save = 0

class MyHandler(BaseHTTPRequestHandler):
    """
    A subclass of BaseHTTPRequestHandler that handles HTTP POST requests.
    """

    def do_POST(self):
        """
        Handles a POST request. Receives a serialised dictionary and an encrypted text file,
        deserialises the dictionary, decrypts the text file, saves the received data to files,
        and sends a response back to the client.
        """

        # Define file names.
        date_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        dict_file_name = f"server_dict_file_{date_str}.txt"
        text_file_name = f"server_text_file_{date_str}.txt"

        try:
            # Capture HTTP POST variables using the "cgi" module.
            postvars = cgi.FieldStorage(fp=self.rfile,
                            headers=self.headers,
                            environ={'REQUEST_METHOD': 'POST'},
                            keep_blank_values=1,
                            strict_parsing=1)
        except:
            # If an exception occurs, print an error message and exit the programme.
            print("Error occurred while capturing HTTP POST variables. \n")
            sys.exit()

        try:
            # Retrieve serialised dictionary from the POST request.
            serialised_dict = postvars["SerialisedDictionary"].value

            # Check if the dictionary content is not None.
            if serialised_dict is not None:
                # Print message indicating that a dictionary has been received.
                print("Received dictionary. \n")

                # Retrieve the pickling format from the HTTP headers and convert to uppercase.
                pickling_format = str(self.headers.get("PicklingFormat")).upper()

                # Print a message indicating the dictionary format.
                print(f"Dictionary format is {pickling_format}. \n")

                # Depending on the format of the dictionary, deserialise it accordingly.
                if pickling_format == "BINARY":
                    my_dict = pickle.loads(base64.b64decode(serialised_dict))
                elif pickling_format == "JSON":
                    my_dict = json.loads(serialised_dict)
                elif pickling_format == "XML":
                    root = ET.fromstring(serialised_dict)
                    my_dict = {}
                    for child in root:
                        my_dict[child.tag] = child.text

                # If the receive_print flag is set, print the received dictionary content.
                if receive_print == 1:
                    print(f"Dictionary content (serialised): \n{serialised_dict}\n")
                    print(f"Dictionary content (deserialised): \n{my_dict}\n")

                # If the receive_save flag is set, write the received dictionary content to a file.
                if receive_save == 1:
                    print(f"Writing received dictionary (serialised) to: \n{dict_file_name}\n")
                    with open(dict_file_name, "w", encoding="utf-8") as write_dict_file:
                        write_dict_file.write(f"{pickling_format}:\n{serialised_dict}")
                        write_dict_file.close()
        except:
            # If an exception occurs, print an error message and exit the programme.
            print("Error occurred while processing received dictionary. \n")
            sys.exit()


        try:
            # Get the encrypted bytes of the text file from the POST request.
            text_file_encrypted = bytes(postvars["TextFile"].value)

            # Check if text file content is not None.
            if text_file_encrypted is not None:
                # Print a message indicating that a text file has been received.
                print("Received text file. \n")

                # Check if the text file is encrypted.
                is_encrypted = self.headers.get("IsEncrypted")
                if is_encrypted == "1":
                    # Decode the encryption key from base64 and initialise Fernet object.
                    encryption_key = base64.b64decode(self.headers.get("EncryptionKey"))
                    fernet = Fernet(encryption_key)

                    # Print a message indicating that the text file is encrypted.
                    print("Received text file is encrypted. \n")

                    # Decrypt the text file content and decode it into a string.
                    text_file_content = fernet.decrypt(text_file_encrypted).decode("utf-8")

                    # If the receive_print flag is set, print the received text file content.
                    if receive_print == 1:
                        print(f"Received text file (encrypted): \n{encryption_key}\n")
                        print(f"Received text file (decrypted): \n{text_file_content}\n")
                else:
                    # Decode the text file content into a string.
                    print("Received text file is not encrypted. \n")
                    text_file_content = text_file_encrypted.decode("utf-8")

                    # If the receive_print flag is set, print the received text file content.
                    if receive_print == 1:
                        print(f"Received text file: \n{text_file_content}\n")

                # If the receive_save flag is set, write the received text file content to a file.
                if receive_save == 1:
                    print(f"Writing received text file to: \n{text_file_name}\n")
                    with open(text_file_name, "w", encoding="utf-8") as write_text_file:
                        write_text_file.write(text_file_content)
                        write_text_file.close()
        except:
            # If an exception occurs, print an error message and exit the programme.
            print("Error occurred while processing received text file. \n")
            sys.exit()

        try:
            # Send a 200 status code to indicate that the request was successfully received.
            self.send_response(200)

            # Set the content type of the response to text/html.
            self.send_header("Content-type", "text/html")

            # End the headers.
            self.end_headers()

            # Write the message "RECEIVED" to the response body.
            self.wfile.write(b"RECEIVED")
        except:
            # If an exception occurs, print an error message and exit the programme.
            print("Error occurred while sending response to client. \n")
            sys.exit()

try:
    # Set server address to localhost on a defined port.
    server_address = ("", server_port)

    # Create an HTTP server object with the specified server address and request handler class.
    httpd = HTTPServer(server_address, MyHandler)

    # Prompt user to choose receive action (print, save, or both) for the text file content.
    receive_action_choice = input("Please select receive action (print, save, both): ").lower()

    # Set receive_print and receive_save flags based on the user's input.
    if receive_action_choice == "print":
        receive_print = 1
        receive_save = 0
    elif receive_action_choice == "save":
        receive_print = 0
        receive_save = 1
    elif receive_action_choice == "both":
        receive_print = 1
        receive_save = 1
    else:
        # If the input is invalid, print an error message,
        # then set receive_print to 1 and receive_save to 0.
        print("Invalid receive option, using \"print\". \n")
        receive_print = 1
        receive_save = 0

    # Print a message indicating that a the HTTP server is being started.
    print(f"Starting HTTP server on port {server_port}...\n")

    # Start the HTTP server and serve requests indefinitely.
    httpd.serve_forever()
except:
    # If an exception occurs, print an error message and exit the programme.
    print(f"Error occurred while starting HTTP server on port {server_port}. \n")
    sys.exit()
