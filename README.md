# Build a Simple Client-Server Network Application

This is a group project for the Software Development in Practice module at the University of Liverpool. 

The group consists of the following members:

1. Chi-Wei Lam (Project Manager & Tester)
2. Maria Petrochenkova (Software Architect)
3. Minh Lay (Software Engineer)


For this collaborative project, we were tasked with developing a simple client-server network application and carrying out several activities relating to the serialisation of data, the transfer of files, and the encryption of data once the network was formed.

## How to get started?

Ensure that you have installed the necessary packages listed in `requirements.txt` prior to starting.

To install the requirements file, run the following command in your terminal window: 
`pip install -r requirements.txt`

To establish the network, run this command in your terminal window:

```
$ python server.py
```

You have now initiated your server. Open a new terminal window and execute the
following command:

```
$ python client.py
```

Your client should now be connected to your server.


## How to use?

This application will execute using the dictionary object provided. However, should you wish to use 
a different data set or change the data type, please locate the dictionary object on line 29 of
the client.py file and make the necessary changes.

```bash
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
```

Once the server.py file has been initialised, follow the on-screen prompt to decide how to handle 
the data received from the client.py file.

Similarly, once the client.py file has been initialised, follow the on-screen prompt to choose 
the serialisation format and whether the file should be encrypted.


## Tests

This application run a basic set of manual unit and integration tests based on the following features: 

```
Our server has three modes:

• Print: only show the content, don’t save

• Save: only save the content, don’t show

• Both: print and save the content
```

```
Our client can send a dictionary object in three different formats:

• BINARY

• JSON

• XML
```

```
Our client has two options for sending files:

• Unencrypted

• Encrypted
```

The table below displays the observed results for all possible configuration combinations:

![image](https://user-images.githubusercontent.com/58013610/226113563-ce44c64e-0b29-468c-827c-c4bb8d8b85d5.png)

Please see the test result images along with the functional requirements specification in `/test/` 
for more information. 


## License


Licensed under the MIT License;
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://mit-license.org/

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
