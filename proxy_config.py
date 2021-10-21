from proxy_checker import ProxyChecker
from pathlib import Path
import os.path


class GettingProxyException(Exception):
    def __str__(self):
        return f"{super().__str__()}: Error while getting proxy!\n"

class ListEmptyException(Exception):
    def __str__(self):
        return f"{super().__str__()}: Your proxy list is empty, check path file or validate your proxy shema <ip>:<port>!\n"


def checker(proxy):
    checker = ProxyChecker()
    checked_status = checker.check_proxy(proxy)
    print(f"CHECKING: {proxy}")
    print(f"Proxy working status: {checked_status}\n")
    return checked_status


def get_proxy(proxies_file, is_check=False):
    proxy_list = []
    
    if not os.path.isfile(proxies_file):
        print(f"File '{proxies_file}' does not exist")
        raise ListEmptyException
    
    try:
        with open(proxies_file) as p_file:
            for proxy in p_file:
                if "\n" in str(proxy):
                    proxy = proxy[:-2]
                if is_check:
                    if checker(proxy):
                        proxy_list.append(proxy)
                else:
                    proxy_list.append(proxy)
    
    except Exception as e:
        raise GettingProxyException(f"An error at getting proxy ocurred: {e}")

    finally:
        if proxy_list:
            return proxy_list
        elif not proxy_list:
            raise ListEmptyException
        else:
            raise Exception
