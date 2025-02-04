import time
import pywifi
from pywifi import Profile, const
import pywifi.iface


def get_switch_network():
    wifi = pywifi.PyWiFi()
    iface: pywifi.iface.Interface = wifi.interfaces()[0]
    for network in iface.scan_results():
        if network.ssid.startswith("switch_"):
            return network.ssid


def connect_to_switch(ssid: str, password: str):
    wifi = pywifi.PyWiFi()
    iface: pywifi.iface.Interface = wifi.interfaces()[0]

    for network in iface.scan_results():
        if network.ssid == ssid:
            if iface.status() == const.IFACE_DISCONNECTED:
                profile = Profile()
                profile.ssid = ssid
                profile.auth = network.auth
                profile.akm = network.akm
                profile.cipher = const.CIPHER_TYPE_CCMP
                profile.key = password

                iface.remove_all_network_profiles()
                network_profile = iface.add_network_profile(profile)
                iface.connect(network_profile)
                while iface.status() == const.IFACE_CONNECTING:
                    time.sleep(0.3)
                print("Switch Connected")
                return True
    return False


def disconnect_to_swicth():
    wifi = pywifi.PyWiFi()
    iface: pywifi.iface.Interface = wifi.interfaces()[0]
    print("Disconnecting Switch")
    iface.disconnect()
