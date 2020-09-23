#!/usr/bin/env python
import subprocess
import optparse
import re
#programa responsável por mudar o MAC address de uma interface.

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Altera o Endereco mac")
    parser.add_option("-m", "--macaddress", dest="new_mac", help="novo endereco mac")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] digite um interface correta, use -- help para mais info")
    elif not options.new_mac:
        parser.error("[-] digite um mac, use -- help para mais info")
    return options



def change_mac(interface,new_mac):
    print(" [+] mudando endereco mac " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_result = ifconfig_result.decode('utf-8')
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return  mac_address_search_result.group(0)
    else:
        print("[-] nao consegui ler o macaddres")



options = get_arguments()
current_mac = get_current_mac(options.interface)
print("MAC atual = "+ str(current_mac))
change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] Endereco MAC alterado com sucesso")
else:
    print("[-] Nao foi alterado endereco mac")
