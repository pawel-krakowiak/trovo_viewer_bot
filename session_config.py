from streamlink import Streamlink
from fake_useragent import UserAgent


def get_session():
    user_agent = UserAgent()
    session = Streamlink()
    session.set_option(
        "http-headers",
        {
            'User-Agent': user_agent.random,
            "Client-ID": "ewvlchtxgqq88ru9gmfp1gmyt6h2b93"
        }
    )

    return session
