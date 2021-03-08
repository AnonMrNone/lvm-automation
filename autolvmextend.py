import subprocess
def extendlvm():
    dev = input("[*] Enter the device path (eg: /dev/vgname/lvname) : ")
    size = input("[*] Enter the size to be extended (eg: 5G) : ")
    lvextend = subprocess.getstatusoutput("lvextend --size +{0} {1}".format(size,dev))
    if lvextend[0] == 0:
        resize2fs = subprocess.getstatusoutput("resize2fs {0}".format(dev))
        if resize2fs[0] == 0:
            print("[*] Done")
        else:
            print("[*] Problem with resize2fs")
    else:
        print("[*] Problem with lvextend")

extendlvm()
