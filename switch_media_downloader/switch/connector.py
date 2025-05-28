import time

import pywifi
import pywifi.iface
from pywifi import Profile, const

from switch_media_downloader.controllers.string_localization import StringLocalization


def get_switch_network() -> str:
        wifi = pywifi.PyWiFi()
        if len(wifi.interfaces()) != 0:
                iface: pywifi.iface.Interface = wifi.interfaces()[0]
                for network in iface.scan_results():
                        if network.ssid.startswith("switch_"):
                                return network.ssid
                return None
        return None


def connect_to_switch(ssid: str, password: str) -> bool:
        wifi = pywifi.PyWiFi()
        iface: pywifi.iface.Interface = wifi.interfaces()[0]

        for network in iface.scan_results():
                if network.ssid == ssid and iface.status() == const.IFACE_DISCONNECTED:
                        profile = Profile()
                        profile.ssid = ssid
                        profile.auth = network.auth
                        profile.akm = network.akm
                        profile.cipher = const.CIPHER_TYPE_CCMP
                        profile.key = password

                        iface.remove_all_network_profiles()
                        network_profile = iface.add_network_profile(profile)
                        iface.connect(network_profile)
                        while iface.status() != const.IFACE_CONNECTED:
                                time.sleep(0.3)
                        print(
                                StringLocalization().get_localizated_string(
                                        "switch_connection_enter_text"
                                )
                        )
                        return True
        return False


def disconnect_to_swicth():
        wifi = pywifi.PyWiFi()
        iface: pywifi.iface.Interface = wifi.interfaces()[0]
        print(StringLocalization().get_localizated_string("switch_connection_exit_text"))
        iface.disconnect()
        return True
