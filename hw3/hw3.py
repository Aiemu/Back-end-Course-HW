import requests
import json
import re

def analyse():
    cmd = input("")

    cmd_list = cmd.split()
    
    input_path = cmd_list[0]
    output_path = cmd_list[1]
    url_list = []

    try:
        with open(input_path, "r") as fi:
            url_list = fi.readlines()
            for row in url_list:
                dict = {}
                ret = requests.get(row)
                ret.encoding = 'utf-8'
                html = ret.text
                dict["phone"] = re.findall(r"(?<=[^\w])(\d{7,8}|\d{11})(?=[^\w])", html)
                dict["name"] = re.findall(r"[(姓名)(name)][:：](.*?)[,.;\"，。；“”]", html)
                dict["url"] = re.findall(r"\s*(?<=[\s,.;，。；])网址[:：]\s*(https?://.*?)(?=[,;\"，。；“”\s])", html)
                dict["shared"] = re.findall(r"[^\n\r]*链接[^\n\r]*提取码[^\n\r]*", html)
                js = json.dumps(dict)
                with open(output_path, "w", encoding = "utf-8") as fo:
                    fo.write(js)

    except IOError:
        print("Error: Input file not exist!")
        return

analyse()