# Data erasure certificates download
A program that automates the process of downloading data erasure certificates.
<br/>
Due to confidentiality reasons, I am unable to disclose the specific data erasure platform and login details used in this program. However, I developed this program as a self-initiative during my previous role to streamline the processing time and automate the process. I am sharing this program on my GitHub profile as a demonstration of my abilities. 
<br/>
Please note that the program will not function without access to the appropriate data erasure platform and login details.
___
## __Libraries that require installation__
* [TKinter installation guide](https://docs.python.org/3/library/tkinter.html)
* [Selenium (Chrome Driver) installation](https://pypi.org/project/selenium/)
* [Pyautogui installation](https://pyautogui.readthedocs.io/en/latest/install.html)
* [pandas installation](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
___
## Prerequisites
- Python 3.10 or later
- An IDE such as PyCharm, VS Code, or Sublime Text
- Google Chrome, updated to the latest version
- Selenium Chrome driver that matches the version of Google Chrome
- An empty 'pdf' folder in the same location as the program
- A CSV file named 'IMEI.csv' containing IMEI and/or Serial Numbers, saved in the same folder as the program
- No files from previous database downloads in the same folder as the program
___
## Usage Instructions
1. Ensure that the 'pdf' folder is empty
2. Place the IMEI and/or Serial Numbers in a 'IMEI.csv' file and save it in the same folder as the program
3. Remove any files from previous database downloads in the same folder as the program
4. Open the "db_download_app.py" in your IDE and press "Run"
5. In the pop-up window, select the following folders:
   - The folder where the program files are located
   - The folder where the Chrome driver for Selenium is located
   - Enter the date from which to look in the PhoneCheck database and export everything from that date (in the format of mm/dd/yyyy)
6. Enter login credentials
7. Wait while the program extracts the data, matches the IMEI/SN numbers with the database, and downloads the certificates
8. Do not use the machine while the certificates are downloading as it may cause the program to crash


**Note**: Due to confidentiality reasons, the data erasure platform and login details cannot be disclosed. As a result, the program will not work without access to these resources.
___
## Time comparison
The program has been tested and compared to manual processes. Results show that the program is significantly faster, with a time savings of up to 82% for 100 devices. See the table below for detailed results.

|Sub-process|Quantity|Manual time(second)|Program time(seconds)|
|:---------:|:---------:|:---------:|:---------:|
|Login|N/A|17|9|
|Access Database|N/A|122|80|
|**Sub-total**|   |**139**|**89**|
|Display certificate|1|16|2|
|Download certificate PDF|1|28|5|
|**Sub-total**|**1**|**44**|**7**|
|**Grand total**|**1**|**183**|**98**|

**Outcome: Program timing is 85 seconds faster than manual (46% faster) for 1 device**

|Sub-process|Quantity|Manual time(second)|Program time(seconds)|
|:---------:|:---------:|:---------:|:---------:|
|Login|N/A|17|9|
|Access Database|N/A|122|80|
|**Sub-total**|   |**139**|**89**|
|Display certificate|10|160|20|
|Download certificate PDF|10|280|50|
|**Sub-total**|**10**|**440**|**70**|
|**Grand total**|**10**|**579**|**159**|

**Outcome: Program timing is 420 seconds faster than manual (72% faster) for 10 devices**

|Sub-process|Quantity|Manual time(second)|Program time(seconds)|
|:---------:|:---------:|:---------:|:---------:|
|Login|N/A|17|9|
|Access Database|N/A|122|80|
|**Sub-total**|   |**139**|**89**|
|Display certificate|100|1600|200|
|Download certificate PDF|100|2800|500|
|**Sub-total**|**100**|**4400**|**700**|
|**Grand total**|**100**|**4539**|**789**|

**Outcome: Program timing is 3570 seconds (59.5 minutes) faster than manual (82% faster) for 100 devices**

|Sub-process|Quantity|Manual time(second)|Program time(seconds)|
|:---------:|:---------:|:---------:|:---------:|
|Login|N/A|17|9|
|Access Database|N/A|122|80|
|**Sub-total**|   |**139**|**89**|
|Display certificate|1000|16000|2000|
|Download certificate PDF|1000|28000|5000|
|**Sub-total**|**1000**|**44000**|**7000**|
|**Grand total**|**1000**|**44139 (12.25 hrs)**|**7089 (1.96 hrs)**|

**Outcome: Program timing is 37050 seconds (approx 10hrs) faster than manual (83% faster) for 1000 devices**
