import re


config_path = 'config.ini'
patterns = [
    r'key": "(?P<id>[\w\@|.]+[^\"])',
    r'key = (?P<key>[\w\-]+)',
    r'password = (?P<pass>[\w]+)'
]


def parse(config_path) -> str:
    with open(config_path) as config:
        text = config.read()
        for pattern in patterns:
            res = re.findall(pattern, text, flags=re.M)
            final_text = re.sub(res[0], '*******', text)
        return final_text


if __name__ == "__main__":
    print(parse(config_path))



