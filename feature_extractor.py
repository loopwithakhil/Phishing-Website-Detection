import re
from urllib.parse import urlparse

def extract_features(url):

    features = []

    ip_pattern = r'(\d+\.){3}\d+'
    features.append(1 if re.search(ip_pattern, url) else -1)

    features.append(1 if len(url) >= 54 else -1)

    shorteners = [
        'bit.ly',
        'tinyurl.com',
        'goo.gl',
        't.co'
    ]

    features.append(
        1 if any(s in url for s in shorteners)
        else -1
    )

    features.append(1 if '@' in url else -1)

    features.append(
        1 if url.rfind('//') > 7
        else -1
    )

    domain = urlparse(url).netloc

    features.append(
        1 if '-' in domain
        else -1
    )

    features.append(
        1 if domain.count('.') > 2
        else -1
    )

    features.append(
        1 if url.startswith("https")
        else -1
    )

    features.append(
        1 if "https" in domain
        else -1
    )

    features.append(
        1 if "mailto:" in url
        else -1
    )

    features.append(
        1 if domain not in url
        else -1
    )

    return features