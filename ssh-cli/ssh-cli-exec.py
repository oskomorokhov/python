import getpass
import csv
from argparse import ArgumentParser
from netmiko import ConnectHandler

if __name__ == "__main__":
    parser = ArgumentParser(description='Arguments')
    parser.add_argument('-c', '--csv', required=True, action='store', help='Location of CSV file')
    args = parser.parse_args()

    device_type = getpass._raw_input('Device Type: ')
    ssh_username = getpass.getpass(prompt='Username: ')
    ssh_password = getpass.getpass()
    ssh_command = getpass._raw_input('Command:# ')

    with open(args.csv, "r") as file:
        reader = csv.DictReader(file)
        for device_row in reader:
            ssh_session = ConnectHandler(device_type=device_type, ip=device_row['device_ip'],
                                         username=ssh_username, password=ssh_password)
            print("-------- {0} ---------".format(device_row['device_ip']))
            print(ssh_session.send_command(ssh_command))