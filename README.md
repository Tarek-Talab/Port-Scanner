# Port-Scanner
This Python script is a simple, console-based Port Scanner tool developed to demonstrate the fundamental principles of network security in a practical way. It is used to scan a specified IP address over a defined port range to detect which services are active (open).

2. Installation (Kurulum)
Install the required external Python libraries using the following command:

Bash

pip install pyfiglet termcolor colorama
3. Usage (Kullanım)
Run the script from your terminal:

Bash

python port_scanner.py
The script will prompt you for the necessary input:

[+] IP: Enter the target IP address (e.g., 127.0.0.1 or a server IP).

[+] Port BaşlangıÇ sınırı: Enter the starting port number (e.g., 1).

[+] Port bitiş sınırı: Enter the ending port number (e.g., 1024).

The script will then print the status of each port within the specified range, highlighting the active (open) services.
