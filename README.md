The exe file can be obtained from:

https://drive.google.com/file/d/19doLF2Et5b7dUaDvkbVOusCfHF-jpS72/view?usp=sharing


You need to setup a mysql server on machine to build database:

https://dev.mysql.com/downloads/mysql/


To use the original Python code to run the program:
Start:
1. Go to https://www.anaconda.com/
2. Press "Download", download and install Anaconda
3. Open anaconda and open jupyter notebook


Packages operation:
install pandas
install mysql-connector-python
install tk


Easiest way to use the code in jupyter notebook:
1. Create new notebook
2. Copy UI_datarc.py content to new created notebook
3. Run the notebook


Generate exe program:
1. Open anaconda and open the notebook, output file as .py
1. Open Powershell Prompt from anaconda
2. Type in command "pip install pyinstaller" and press enter
3. After completion, type in command "pip install auto-py-to-exe" and press enter
4. After completion, type in command "auto-py-to-exe" and press enter, this will open program generater
5. Select the created .py file (Easy to build version is the UI_datarc.py)
6. You may add icon file .icon to assign an icon
6. Set "Onefile" option to "One File"
7. Set "Console Window" option to "Window Based"
8. You may choose the output directory by using "Setting"
9. Press "CONVERT .PY TO EXE" to generate exe program
10. Wait until completion (This takes amount of time)
11. Go to the output directory and run the generated exe program
