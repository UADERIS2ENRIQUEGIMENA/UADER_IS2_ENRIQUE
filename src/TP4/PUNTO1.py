import os
import re
import subprocess

class Ping:
    def __init__(self):
        pass

    def execute(self, ip_address):
        if not self._is_valid_ip(ip_address):
            print("Invalid IP address")
            return

        for _ in range(10):
            response = os.system("ping -c 1 " + ip_address)
            if response == 0:
                print(ip_address, 'is reachable')
            else:
                print(ip_address, 'is unreachable')

    def execute_free(self, ip_address):
        for _ in range(10):
            response = os.system("ping -c 1 " + ip_address)
            if response == 0:
                print(ip_address, 'is reachable')
            else:
                print(ip_address, 'is unreachable')

    def _is_valid_ip(self, ip_address):
        return re.match(r'^192\.', ip_address) is not None


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.execute_free("www.google.com")
        else:
            self.ping.execute(ip_address)


# Ejemplo de uso
proxy = PingProxy()
proxy.execute("192.168.0.1")  # Realiza ping a la dirección IP 192.168.0.1
proxy.execute("192.0.2.1")  # No realiza ping, dirección IP no válida
proxy.execute("192.168.0.254")  # Realiza ping a www.google.com usando execute_free de Ping
