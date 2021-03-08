#!/usr/bin/env python
# coding: utf-8

# In[2]:


import subprocess, os


# In[21]:


def createlv():
    print("--------------------------------------------")
    print("                   AUTOLVM                  ")
    print("--------------------------------------------")
    print(subprocess.getoutput('lsblk'))
    dev = input("[*] Choose the devices for PV seperated by space (eg: /dev/sdc /dev/sde) : ").split(" ")
    for i in dev:
        pvcreate = subprocess.getstatusoutput("pvcreate {0}".format(i))
        if pvcreate[0] == 0:
            print("{0} pv created".format(i))
        else:
            print("{0} pv failed".format(i))

    vgname = input("[*] Enter VG name: ")
    lis = ' '.join(dev)
    vgcreate = subprocess.getstatusoutput("vgcreate {0} {1}".format(vgname,lis))
    
    lvname = input("[*] Enter LV name: ")
    size = input("[*] Enter Size of LV eg(10G): ")
    lvcreate = subprocess.getstatusoutput("lvcreate --size {0} --name {1} {2}".format(size,lvname,vgname))
    
    mount = input("[*] Enter the full mountpoint/path: ")
    formating = subprocess.getstatusoutput("mkfs.ext4 /dev/{0}/{1}".format(vgname,lvname))
    mounting = subprocess.getstatusoutput("mount /dev/{0}/{1} {2}".format(vgname,lvname,mount))
    if mounting[0] == 0:
        print("[*] Done")
    else:
        print("[*] Some error while mounting")

        
createlv()
