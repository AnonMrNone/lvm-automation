import subprocess
def deletelvm():
    yn = input("[*] Have you mounted LV?(y/n): ")
    if yn == 'y':
        dev = input("[*] Enter the device name (eg: /dev/vgname/lvname): ")
        drives = input("[*] Enter the drive name(s) seperated with space (eg: /dev/sdb /dev/sdc): ")
        vgname = dev.split("/")[2]
        umount = subprocess.getstatusoutput("umount {0}".format(dev))
        if umount[0] == 0:
            lvchange = subprocess.getstatusoutput("lvchange -an {0}".format(dev))
            if lvchange[0] == 0:
                lvremove = subprocess.getstatusoutput("lvremove {0}".format(dev))
                if lvremove[0] == 0:
                    vgchange = subprocess.getstatusoutput("vgchange -an {0}".format(vgname))
                    if vgchange[0] == 0:
                        vgremove = subprocess.getstatusoutput("vgremove {0}".format(vgname))
                        if vgremove[0] == 0:
                            pvremove = subprocess.getstatusoutput("pvremove {0}".format(drives))
                            if pvremove[0] == 0:
                                print("[*] Done")
                            else:
                                print("[*] Problem with pvremove")
                        else:
                            print("[*] Problem with vgremove")
                    else:
                        print("[*] Problem with vgchange")
                else:
                    print("[*] Problem with lvremove")
            else:
                print("[*] Problem with lvchange")
        else:
            print("[*] Problem with umount")
    else:
        print("[*] Support yet to come")

deletelvm()
