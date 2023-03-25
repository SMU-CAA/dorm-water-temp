import re

import requests
from bs4 import BeautifulSoup

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return get_temp()


def get_temp():
    url = "http://hqzx.shmtu.edu.cn/cellphone/getHotWater"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, "lxml")

    ul_node = soup.select("ul")[0]

    result_data = {}
    for temp_node in ul_node.select("li > a > div"):
        water_temperature = temp_node.select("div")[0].text
        water_level = temp_node.select("div .stage")[0].text
        building_number = temp_node.select("span")[0].text
        water_temperature = (
            float(re.findall(r"\d+\.?\d*", water_temperature)[0]))
        water_level = (float(re.findall(r"\d+\.?\d*", water_level)[0]))
        building_number = (int(re.findall(r"\d+", building_number)[0]))
        result_data[building_number] = {
            "temp": water_temperature,
            "level": water_level
        }

    return result_data


if __name__ == '__main__':
    print(get_temp())
