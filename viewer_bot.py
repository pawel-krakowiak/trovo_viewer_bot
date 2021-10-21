from pathlib import Path
from threading import Thread

from proxy_config import get_proxy
from session_config import get_session

class TrovoViewerBot(object):
    def __init__(self, proxy_list, stream_url):
        self.proxy_list = proxy_list
        self.proxy_amount = len(self.proxy_list)
        self.session = get_session()
        self.stream_url = "https://www.twitch.tv/pawngrubber"
        self.processes = []
        self.max_threads = 1000

    def get_url(self):
        url = ""
        try:
            stream = self.session.streams(self.stream_url)
            try:
                url = stream['audio_only'].url
            except:
                url = stream['worst'].url
            finally:
                print(f"Stream URL: {url[:]}")
        except Exception as e: print(e)
        finally: return url


proxy_file = Path("./proxy_lst/proxies01.txt")
proxy_list = get_proxy(proxy_file, is_check=False)

stream01 = TrovoViewerBot(proxy_list, stream_url="")
print(stream01.get_url())


