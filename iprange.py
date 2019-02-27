#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
global boatList, final_ip, finalIPlist
Exit = 0
num = 0
boatList=[]
finalIPlist = []
final_ip = ""
while True:


    def get_lst():  #get filenames in directory ending with .lst
        global boat_list, boat_dict, num
        num = 0

        boat_dict = {}
        print("--------------------------------------------------------------\n "
              "Available Projects\n--------------------------------------------------------------")
        for item in os.listdir():#get filenames of files.lst

            if item.find(".lst") > 0:
                num =  num + 1
                boat_list = (str(num)+". " + item[:-4])


                boat_dict[str(num)] = [str(item)]

                print(str(num) + "." + str(item[:-4]))


                #print (boat_list)



    def set_ip(boat_number):

        count = 0
        boat_name = boat_dict[boat_number]
        Boat_name = str(boat_name)
        BoatName = Boat_name[2:-2]
        print("Setting up IP ranges for " + BoatName)

        cmd = "netsh interface ip set address " + Ethernet_ad + " dhcp"
        os.system(cmd)
        print("resetting Ethernetadapter to DHCP")



        for Line in finalIPlist:
            if count == 0:
                count = 1
                cmd = "netsh interface ip set address " + Ethernet_ad + " static " + Line + " " + "255.255.255.0"
                os.system(cmd)
                first_ip = Line
                print("setting static IP to " + Line)


            if Line != first_ip:

                cmd = "netsh interface ip add address " + Ethernet_ad + " " + Line + " " + "255.255.255.0"
                os.system(cmd)


            print ( "Adding IP address " + Line)


    def ip_list(boat_number):
        global boatList
        boat_name = boat_dict[boat_number]
        Boat_name = str(boat_name)
        BoatName = Boat_name[2:-2]
        f_ip = open(str(BoatName), "r")  # open project file
        print("project conatins following ip-addresses:")
        for line in f_ip:
            boatList.append(line)
            print(line)
        f_ip.close


    def set_dhcp():
        cmd = "netsh interface ip set address " + Ethernet_ad + " dhcp"
        os.system(cmd)
        print (Ethernet_ad + "is set to DHCP")


    def EthernetAdapter():
        global Ethernet_ad, final_ip
        Ethernet_num = input("Ethernet adapter number (1,2....: ")
        print("____________________________________________________")
        if Ethernet_num == "1":
            Ethernet_ad = '"Ethernet"'
        else:
            Ethernet_ad = '"Ethernet ' + str(Ethernet_num) + '"'
            print ("changing " + Ethernet_ad)


    def last_ip(ip_last_part):
        global final_ip, finaIPlist
        for item in boatList:
            try:
                ip = item.split(".")
                ip[3] = str(ip_last_part)
                seperator = "."
                final_ip = (seperator.join(ip))
                finalIPlist.append(final_ip)
            except:
                pass

        print (finalIPlist)



    get_lst()
    print("____________________________________________________")
    print ("\r\nTo set back to dhcp, type in '0' \r\nPress Enter to exit program")
    print("____________________________________________________")

    boat_number = input("Project number: ")

    if boat_number == '':
        break
    EthernetAdapter()
    if boat_number == '0':
        set_dhcp()
    else:
        ip_list(boat_number)
        ip_last_part = input("change last part of ip address to: ")
        last_ip(ip_last_part)
        if int(ip_last_part) < 255 and int(ip_last_part)> 0:
            set_ip(boat_number)
    if boat_number == '':
        break







