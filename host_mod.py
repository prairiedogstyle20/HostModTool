#! /usr/bin/env python3

# Start of the host file mod program on linux

import platform
import os
import sys
#from PyQt5.QtWidgets import QApplication, QLabel, QButton, 

class HostLine:
    
    def __init__(self, new_host_name, new_ip_addr):
        self.host_name = new_host_name
        self.ip_addr = new_ip_addr

    def update_host(self, new_host_name):
        self.host_name = new_host_name

    def update_ip(self, new_ip_addr):
        self.ip_addr = new_ip_addr

class FileModifier():

    def __init__(self):
        self.file_path = ""
        self.list_HostLines = []
        self.system = self.isSystem() 
        self.is_admin = self.isAdmin()
        self.host_line_container = []

    def isSystem(self):
        curr_sys = platform.system()
        if curr_sys == 'Linux':
            self.file_path="/etc/hosts"
        elif curr_sys == 'Windows':
            self.file_path = "c:\windows\system32\drivers\etc\hosts"
        return curr_sys

    def isAdmin(self):
        curr_sys = platform.system()
        if curr_sys == "Linux":
            admin_type = (os.getuid() == 0) 
        elif curr_sys == "Windows":
            pass
        else:
            pass
        return admin_type
    
    def get_hosts(self):
        for line in open(self.file_path):
            if line[0].isnumeric(): 
                temp_value = line.split()
                self.host_line_container.append(HostLine(temp_value[1], temp_value[0]))

        for each in self.host_line_container:
            print(each.ip_addr + " " + each.host_name)

def main():
    controller = FileModifier()
    print(controller.system)
    print(controller.is_admin)
    controller.get_hosts()

if __name__ == '__main__':
    main() 
