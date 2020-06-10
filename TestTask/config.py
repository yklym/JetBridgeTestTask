default_avatar = "https://cdn.icon-icons.com/icons2/1879/PNG/512/iconfinder-3-avatar-2754579_120516.png"

default_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
                      "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
                      "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in " \
                      "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat" \
                      "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "

curr_domain = "https://localhost:8080/"


def hash_url_string(s):
    return str(abs(hash(s)))[:7]
