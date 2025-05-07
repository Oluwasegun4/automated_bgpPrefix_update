#!/bin/env/python3

import subprocess
from netmiko import ConnectHandler

def command_to_get_prefix(prefix_list_name,as_set):
    command = ["bgpq4", "-A4l", prefix_list_name, as_set]
    return subprocess.run(command, capture_output=True, text=True)

def apply_config_to_device(file_name):
    device_details = {
        "device_type": "cisco_ios",
        "ip": "172.20.10.21",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco"
    }
    connection = ConnectHandler(**device_details)
    connection.enable()

    # with open(f"{file_name}") as f:
    #     config_lines = f.read().splitlines()
    
    output = connection.send_config_from_file(file_name)
    print(output)
    connection.save_config()
    connection.disconnect()
    




def main():
   as_set = "AS-GOOGLE-FIBER"
   prefix_list_name = "GOOGLE-FIBER-PREFIX"
   output = command_to_get_prefix(prefix_list_name,as_set)
   
   with open(f"{prefix_list_name}.txt", "w") as file:
       file.write(output.stdout)
       if output.returncode != 0:
            print("Error running command:", output.stderr)

   apply_config_to_device(f"{prefix_list_name}.txt")

    

       
        








if __name__ == "__main__":
    main()
