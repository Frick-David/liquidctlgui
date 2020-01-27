from liquidctl.driver import find_liquidctl_devices
# if __name__ == '__main__':
#  dirs = get_runtime_dirs()
#  print(dirs)


def list_devices():
     devices = []
     for dev in find_liquidctl_devices():
       devices.append(dev.description)
     return devices


 #  for dev in find_liquidctl_devices():
 #    dev.connect()
 #   try:
 #     print(dev.get_status())
 #     if dev.serial_number == '001':
 #       dev.set_fixed_speed('fan3', 42)
 #   finally:
 #     dev.disconnect()
 #      print(dev.description)

device_descs = list_devices()
