# Build a Simple Client-Server Network Application

This is a group project for the University of Liverpool's Software Development
in Practice module. The group is formed of the following individuals:

1. Chi-Wei Lam (Project Manager & Tester)
2. Maria Petrochenkova (Software Architect)
3. Minh Lay (Software Engineer)

For this collaborative project, we were tasked with developing a simple client-server network applica-
tion and carrying out several required activities relating to the serialisation of data, the transfer of files,
and the encryption of data once the network was formed. 


## How do I get started?

Before you begin, ensure you install the necessary packages that can be
found in `requirements.txt`.

To install the requirements file, run the following command in your terminal window: `pip install -r requirements.txt`

To establish the network, run this command in your terminal window:

```bash
$ python3 server.py
```

You have now initiated your server. Open a new terminal window and execute the
following command:

```bash
$ python3 client.py
```

Your client should now be connected to your server.


## Tests

This code runs a basic set of unit and performance tests. Please see the
unit and performance within `/test/` for more information. 


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
