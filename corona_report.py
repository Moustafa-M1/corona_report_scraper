#!"C:\Python36-32\python.exe"

import requests
from bs4 import BeautifulSoup


def corona():
    country = input("country: ")
    country = country.lower()
    webpage_response = requests.get("https://www.worldometers.info/coronavirus")
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    td = soup.find_all("td")
    text = ""
    for i in td:
        text = text + "|" + i.get_text().replace(" ", "").lower()

    out = text.split("|")
    target = out.index(country)
    world = out.index("world")
    report = {country: [], "world": [out[world+2], out[world+4]]}

    for index, value in enumerate(out):
        if target < index < target + 11:
            report[country].append(value)

    for x, n in enumerate(report[country]):
        if n == '':
            report[country][x] = '0'

    total_cases = soup.find_all(attrs={'class': 'maincounter-number'})
    text2 = ""
    for i in total_cases:
        text2 = text2 + "|" + i.get_text().replace(" ", "").replace("\n", "")

    out2 = text2.split("|")

    print("\n     {:*^50}  ".format(country.upper()))
    print(" Total cases:     {:<15} New cases:  {}\n"
          " Total deaths:    {:<15} New deaths: {}\n"
          " Total recovered: {:<15}\n"
          " Active cases:    {:<15}\n"
          " Critical cases:  {:<15}\n".format(report[country][0], report[country][1], report[country][2],
                                            report[country][3], report[country][4],
                                            report[country][6], report[country][7]))
    print("     {:*^50}     ".format("Around world cases"))
    print(" Total cases:     {:<15} New cases:  {}\n"
          " Total deaths:    {:<15} New deaths: {}\n"
          " Total recovered: {:<15}".format(out2[1], report["world"][0], out2[2], report["world"][1], out2[3]))


corona()
