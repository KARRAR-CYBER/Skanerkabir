import time
import os
from random import randint
from colorama import init, Fore
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Initialize colorama
init(autoreset=True)

def main():
    n = 0
    r = ""

    while n <= 100:
        print(r, f"{Fore.LIGHTRED_EX}%{n}")
        n += randint(1, 5)
        r += "="
        time.sleep(0.1)

    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

    print(f"""{Fore.LIGHTRED_EX}
.##....##.########...#######..##....##
.##...##..##.....##.##.....##.###...##
.##..##...##.....##.##.....##.####..##
.#####....########..##.....##.##.##.##
.##..##...##...##...##.....##.##..####
.##...##..##....##..##.....##.##...###
.##....##.##.....##..#######..##....##
    """)

main()

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
pink = "\033[95m"
blue = "\033[94m"

time.sleep(1)
print("")
print(f"            {red}✪ {green}START TIME --->", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"{red}✪ ")

time.sleep(1)
print("")
print("")
print(f"{yellow}―――‣{pink} I AM MR_DITA")
time.sleep(0.4)
print(f"{yellow}―――――‣{pink} MR_DITA REPORT ")
time.sleep(0.3)
print(f"{yellow}―――――――‣{pink} 09130756432")
time.sleep(0.2)
print(blue)
print(" ")
print(" ")

print(Fore.YELLOW + "     𝗟𝗗 𝗧𝗔𝗥𝗚𝗘𝗧 𝗦𝗤𝗟")

print(Fore.LIGHTCYAN_EX + """
|>>>-----------------------------------------<<<|
|>>>--------MR DITA SQL?           ----------<<<|
|>>>—————————————————————————————————————————<<<|
|>>>                                         <<<|
|>>>         [TELEGRAM ID] @MR_DITA          <<<|
|>>>     [CHANNEL] t.me/MR_DITA              <<<|
|>>>—————————————————————————————————————————<<<|
|>>>                                         <<<|
|>>>    [1]  Report SQL Attack               <<<|
|>>>    [2]  Report SQL Attack               <<<|
|>>>    [3]  Report SQL Attack               <<<|
|>>>    [4]  Report SQL Attack               <<<|
|>>>    [5]  Report SQL Attack               <<<|
|>>>    [6]  Report SQL Attack               <<<|
|>>>                                         <<<|
|>>>—————————————————————————————————————————<<<|
|>>>-----------------------------------------<<<|
|>>>-----------------------------------------<<<|

""")
from colorama import Fore,init
init()
print(Fore.LIGHTRED_EX+"  ")
def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        if not soup.title:
            print("This website has no title!")
        else:
            print(f"Website title: {soup.title.string}")

        h1_tags = soup.find_all('h1')
        if not h1_tags:
            print("This website has no <h1> tags!")
        else:
            print(f"Available <h1> tags: {[h1.string for h1 in h1_tags]}")

        links = soup.find_all('a', href=True)
        broken_links = []
        for link in links:
            try:
                link_response = requests.head(link['href'], allow_redirects=True)
                if link_response.status_code != 200:
                    broken_links.append(link['href'])
            except requests.RequestException:
                broken_links.append(link['href'])

        if broken_links:
            print("Broken links:")
            for broken in broken_links:
                print(broken)
        else:
            print("No broken links found!")

    except requests.RequestException as e:
        print(f"Error accessing the website: {e}")

url = input("Please enter the website URL: ")
check_website(url)
