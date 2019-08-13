# Ugliest IPv4 Calc in the world
import re


def input_get():
    # Gather input, validate against regex, assign defaults
    ip = input("Enter IPv4 Address: ")
    ip_pattern = re.compile(
        "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    ip = "192.168.0.0" if not (ip and (ip_pattern.fullmatch(ip))) else ip
    print(ip)
    mask = input("Enter Prefix or Mask: ")
    mask_pattern = re.compile(
        "^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$")
    prefix_pattern = re.compile("^([0-9]|[1-2][0-9]|[3][0-2])$")
    mask = "24" if not(mask and (mask_pattern.fullmatch(
        mask) or prefix_pattern.fullmatch(mask))) else mask_ds2bs(mask)
    print(mask)
    s_mask = input("Enter Subnet/Supernet Prefix or Mask: ")
    s_mask = "25" if not(s_mask and (mask_pattern.fullmatch(
        s_mask) or prefix_pattern.fullmatch(s_mask))) else mask_ds2bs(s_mask)
    print(s_mask)
    return (ip, int(mask), int(s_mask))


def per(n):
    # Utility foo to derive bits-to-flip & their permutations
    l = []
    for i in range(2**n):
        s = bin(i)[2:].zfill(n)
        l.append(s)
    return l


def ip_ds2bs(ip_d_string):
    # Convert IP in decimal notation(delimimed with dots) into 32-bit bin string
    ip_d_arr = ip_d_string.split(".")
    ip_b_arr = (bin(int(object))[2:].zfill(8) for object in ip_d_arr)
    ip_b_str = ''.join(ip_b_arr)
    return ip_b_str


def ip_bs2ds(ip_b_str, oct=8):
    # Convert IP in 32-bit bin string notation into decimal notation(delimited with dots)
    ip_d_str = '.'.join(
        list((str(int(ip_b_str[i:i+oct], 2)) for i in range(0, len(ip_b_str), oct))))
    return ip_d_str


def mask_ds2bs(mask_d_str):
    # TBD Convert mask in decimal notation(delimited with dots) into prefix (dec str)
    if int(mask_d_str) in range(33):
        return mask_d_str
    mask_d_arr = mask_d_str.split(".")
    mask_b_arr = (bin(int(object))[2:].zfill(8) for object in mask_d_arr)
    prefix = (''.join(mask_b_arr)).count("1")
    return prefix


def subnet_main(ip, prefix, s_prefix):
    # Derive number of subnets within network,total number of hosts,subnet addresses(bin str) or supernet
    ip_b_str = ip_ds2bs(ip)
    net_b_str = ip_b_str[:prefix]+(32-prefix)*'0'
    net_d_str = ip_bs2ds(net_b_str)
    if prefix < s_prefix:
        print("subnetmain if")
        n_subnets = 2**(s_prefix-prefix)
        n_hosts_total = 2**(32-prefix)-(2*n_subnets)
        subnets = []
        if n_subnets > 1:
            for i in range(n_subnets):
                subnet = net_b_str[:prefix] + \
                    per(s_prefix-prefix)[i]+net_b_str[s_prefix:]
                subnets.append(subnet)
                return (subnets, n_subnets, net_b_str, n_hosts_total)
    else:
        print("subnetmain else")
        supernet = net_b_str[:s_prefix]+(32-s_prefix)*'0'
        return (supernet, net_d_str, net_b_str)


def subnet_detail(subnet_b_str, s_prefix):
    # Derive Hosts Range & Broadcast Address
    hostmin = subnet_b_str[:-1]+"1"
    hostmax = (subnet_b_str[:s_prefix]+(32-s_prefix)*'1')[:-1]+'0'
    bcast = subnet_b_str[:s_prefix]+(32-s_prefix)*'1'
    n_hosts = 2**(32-s_prefix)-2
    result = list((ip_bs2ds(i) for i in (hostmin, hostmax, bcast)))
    result.append(n_hosts)
    return result


def execute():
    # Master foo
    input = input_get()
    data = subnet_main(*input)
    print(data[2], input[1])
    print("\r\nNetwork:   %s/%s" % (ip_bs2ds(data[2]), input[1]))
    print("Host_min:  %s \nHost_max:  %s \nBroadcast: %s \nHosts: %d" %
          (tuple(subnet_detail(data[2], input[1]))))
    if input[1] < input[2]:
        print("\r\nSubnets: %d" % data[1])
        print("Hosts total: %d" % data[3])
        for j, i in enumerate(data[0]):
            print("\r\nSubnet %d:\nNetwork:   %s/%s" %
                  (j+1, ip_bs2ds(i), input[2]))
            print("Host_min:  %s \nHost_max:  %s \nBroadcast: %s \nHosts: %d" %
                  (tuple(subnet_detail(i, input[2]))))
    else:
        print("execute else")
        print("Supernet: %s/%s" % (ip_bs2ds(data[0]), input[2]))
        print("Host_min:  %s \nHost_max:  %s \nBroadcast: %s \nHosts: %d" %
              (tuple(subnet_detail(data[0], input[2]))))
