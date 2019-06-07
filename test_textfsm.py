import textfsm

with open('netsh_wlan_show_interface.template', 'r') as template:
    with open('WLANstat_20192405.txt', 'r') as data_file:
    
        re_table = textfsm.TextFSM(template)
        data = re_table.ParseText(data_file.read())

        print(data)