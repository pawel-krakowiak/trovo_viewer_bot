from proxy_config import get_proxy
from pathlib import Path

proxies_file = r"./proxy_lst/proxies01.txt"
proxies_list = get_proxy(proxies_file, is_check=False)

# print(proxies_list)