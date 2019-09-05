# SSH CLI EXEC

send various command(s) to the device(s) via SSH and obtain result data

## Source

<https://github.com/hoelsner/python-script-examples>

## Installation

```bash
pip3 install netmiko
pip3 install paramiko
```

## Devices/Hosts file format

### devices.csv

```bash
device_ip
10.1.1.1
10.1.1.2
host01.domain.com
```

## Simple usage of netmiko

```python
net_connect=netmiko.ConnectHandler(device_type='cisco_ios',ip='10.1.1.1', username='user',password='pass')  
print(net_connect.send_command("show inventory"))
```

## Usage

```bash
python3 ./ssh-cli-exec.py -c devices.csv > ./exec-result.txt
```

supported device types can be obtained here
<https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py#L70>
