# Ugliest IPv6 Calc in the world
import re


def input_get():
    # Gather input, validate against regex, assign defaults
    ip = input("Enter IPv4 Address: ")
    # ip_pattern=re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    ip = "2001:0123:4567:FFFF:FFFF:FFFF:FFFF:FFFF" if not ip else ip
    print(ip)
    mask = input("Enter Prefix or Mask: ")
    # mask_pattern=re.compile("^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$")
    # prefix_pattern=re.compile("^([0-9]|[1-2][0-9]|[3][0-2])$")
    mask = "48" if not mask else mask_ds2bs(mask)
    print(mask)
    s_mask = input("Enter Subnet/Supernet Prefix or Mask: ")
    s_mask = "64" if not s_mask else mask_ds2bs(s_mask)
    print(s_mask)
    return (ip, int(mask), int(s_mask))


def per(n):
    # Utility foo to derive bits-to-flip & their permutations
    # l=[]
    #print("per p argument",n)
    for i in range(2**n):
        p = bin(i)[2:].zfill(n)
        #print("per p",p)
        yield p


def ip_ds2bs(ip_d_string):
    # Convert IP in hex notation(delimimed with dots) into 128-bit bin string
    #print("ip_ds2bs argument",ip_d_string)
    ip_d_arr = ip_d_string.split(":")
    ip_b_arr = (bin(int(object, 16))[2:].zfill(16) for object in ip_d_arr)
    ip_b_str = ''.join(ip_b_arr)
    #print("ip_ds2bs result",ip_b_str)
    return ip_b_str


def ip_bs2ds(ip_b_str, oct=16):
    # Convert IP in 128-bit bin string notation into hex notation(delimited with colons)
    #print("ip_bs2ds arguments",ip_b_str,oct)
    ip_d_str = ':'.join(hex(int(ip_b_str[i:i+oct], 2))[2:].zfill(4)
                        for i in range(0, len(ip_b_str), oct))
    #print("ip_bs2ds result",ip_d_str)
    return ip_d_str


def mask_ds2bs(mask_d_str):
    # TBD Convert mask in decimal notation(delimited with dots) into prefix (dec str)
    if int(mask_d_str) in range(129):
        return mask_d_str
    mask_d_arr = mask_d_str.split(".")
    mask_b_arr = (bin(int(object, 16))[2:].zfill(16) for object in mask_d_arr)
    prefix = (''.join(mask_b_arr)).count("1")
    return prefix


def subnet_main(ip, prefix, s_prefix):
    # Derive number of subnets within network,total number of hosts,subnet addresses(bin str) or supernet
    ip_b_str = ip_ds2bs(ip)
    # print("subnet_main,ip_b_str",ip_b_str)
    net_b_str = ip_b_str[:prefix]+(128-prefix)*'0'
    # print("subnet_main,net_b_str",net_b_str)
    net_d_str = ip_bs2ds(net_b_str)
    if prefix < s_prefix:
        #print("subnetmain if prefix<s_prefix")
        n_subnets = 2**(s_prefix-prefix)
        # print("subnet_main,n_subnets",n_subnets)
        n_hosts_total = 2**(128-prefix)
        # print("subnet_main,n_hosts_total",n_hosts_total)
        subnets = []
        bits_to_flip = per(s_prefix-prefix)
        for i in range(n_subnets):
            subnet = net_b_str[:prefix]+next(bits_to_flip)+net_b_str[s_prefix:]
            # print("subnet_main,subnet",subnet)
            subnets.append(subnet)
            # print("subnet_main,list(subnets)",list(subnets))
            #print("subnet appended")
        return (subnets, n_subnets, net_b_str, n_hosts_total)
    else:
        #print("subnetmain else")
        supernet = net_b_str[:s_prefix]+(128-s_prefix)*'0'
        return (supernet, net_d_str, net_b_str)


def subnet_detail(subnet_b_str, s_prefix):
    # Derive Hosts Range & Broadcast Address
    #print("subnet_detail arguments",subnet_b_str,s_prefix)
    hostmin = subnet_b_str[:-1]+"0"
    #print("subnet_detail hostmin",hostmin)
    hostmax = (subnet_b_str[:s_prefix]+(128-s_prefix)*'1')[:-1]+'1'
    #print("subnet_detail hostmax",hostmax)
    # bcast=subnet_b_str[:s_prefix]+(128-s_prefix)*'1'
    n_hosts = 2**(128-s_prefix)
    #print("subnet_detail n_hosts",n_hosts)
    result = list((ip_bs2ds(i) for i in (hostmin, hostmax)))
    #print("subnet_detail result",result)
    result.append(n_hosts)
    #print("subnet_detail result,appended with n_hosts",result)
    return result


def output_subnet(subnets_arr, l='', id=''):
    run_count = +1
    if len(subnets_arr) > 100:
        limit = 10
    else:
        limit = len(subnets_arr)
    if id:
        print("\r\nSubnet %d:\nNetwork:   %s/%s" %
              (j+1, ip_bs2ds(id), input[2]))
        print("Host_min:  %s \nHost_max: %s \nHosts: %d" %
              (tuple(subnet_detail(id, input[2]))))
    else:
        for j, i in enumerate(subnets_arr[:limit]):
            print("\r\nSubnet %d:\nNetwork:   %s/%s" %
                  (j+1, ip_bs2ds(i), input[2]))
            print("Host_min:  %s \nHost_max: %s \nHosts: %d" %
                  (tuple(subnet_detail(i, input[2]))))


def execute():
    # Master foo
    input = input_get()
    data = subnet_main(*input)
    # print(len(data[0]),data[1],data[2])
    print("\r\nNetwork:   %s/%s" % (ip_bs2ds(data[2]), input[1]))
    print("Host_min:  %s \nHost_max:  %s \nHosts: %d" %
          (tuple(subnet_detail(data[2], input[1]))))
    if input[1] < input[2]:
        print("\r\nSubnets: %d" % data[1])
        print("Hosts total: %d" % data[3])
        # print(len(data[0]))
        if len(data[0]) > 100:
            limit = 10
        else:
            limit = len(data[0])
        for j, i in enumerate(data[0][:limit]):
            print("\r\nSubnet %d:\nNetwork:   %s/%s" %
                  (j+1, ip_bs2ds(i), input[2]))
            print("Host_min:  %s \nHost_max:  %s \nHosts: %d" %
                  (tuple(subnet_detail(i, input[2]))))
    else:
        #print("execute else")
        print("Supernet: %s/%s" % (ip_bs2ds(data[0]), input[2]))
        print("Host_min:  %s \nHost_max: %s \nHosts: %d" %
              (tuple(subnet_detail(data[0], input[2]))))
