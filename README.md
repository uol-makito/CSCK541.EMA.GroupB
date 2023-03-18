# Build a Simple Client-Server Network Application

This is a group project for the University of Liverpool's Software Development
in Practice module. The group is formed of the following individuals:

1. Chi-Wei Lam (Project Manager & Tester)
2. Maria Petrochenkova (Software Architect)
3. Minh Lay (Software Engineer)

For this collaborative project, we were tasked with developing a simple client-server network
application and carrying out several activities relating to the serialisation of data, the transfer 
of files, and the encryption of data once the network was formed.


## How do I get started?

Ensure that you have installed the necessary packages listed in `requirements.txt` prior to starting.
To install the requirements file, run the following command in your terminal window: 
`pip install -r requirements.txt`

To establish the network, run this command in your terminal window:

```bash
$ python server.py
```

You have now initiated your server. Open a new terminal window and execute the
following command:

```bash
$ python client.py
```

Your client should now be connected to your server.


## How to use?

This application will execute using the dictionary object provided. However, should you wish to use 
a different data set or change the data type. Please locate the dictionary object on line 29 of
the client.py file and make the necessary changes.

```bash
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
```

Once the server.py file has been initialised, follow the on-screen prompt to decide how to handle 
the data received from the client.py file.

Similarly, once the client.py file has been initialised, follow the on-screen prompt to choose 
the serialisation format and whether the file should be encrypted.


## Tests

This code runs a basic set of manual unit and intergrated tests. Please see the test 
result images along with the functional requirement specification in `/test/` 
for more information. 

Our server has three modes:
-Print: only show the content, don’t save
-Save: only save the content, don’t show
-Both: print and save the content

Our client can send a dictionary object in three different formats:
-BINARY
-JSON
-XML

Our client has two options for sending files:
-Unencrypted
-Encrypted

![image](https://user-images.githubusercontent.com/58013610/226113563-ce44c64e-0b29-468c-827c-c4bb8d8b85d5.png)

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
