****
RADALYZE built by Adam Seelye as Project 0 for training at Revature
****

- Radalyze is a Python app that reads historical Gamma Radiation detector data from
detectors based in different sites around the U.S.A. and displays the data in a graph
format, all in a command line interface.


- To start using the app, there are a few Python packages that must be installed.
It is recommended to run the app in a virtual environment as well.

****

Linux:

````
  cd <directory>
  
  git clone https://github.com/adamseelye/radalyze
  
  python -m venv .
  
  pip install mysql-connector
  pip install bcrypt
  pip install plotext
  pip install pandas
  
````
****

The program will not run out of the box - \
A MySQL DB must be defined by the user (the code points to a local-only IP address) \
Add the parameters in the file "connector.py" beginning on line 8.

The database table structure is defined in the file "proj_0.png".
There are 3 tables; one containing User information, one containing logs,
and one containing the encrypted user passwords.
****

Thanks for checking it out!
