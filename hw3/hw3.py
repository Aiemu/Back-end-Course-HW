import requests
import sys
import json
import re
import os

def get_url(html):
    ret = requests.get(html.url)
    if ret.status_code == 301 or ret.status_code == 302:
        ret = get_url(ret)
    return ret

def analyse():
    cmd_list = sys.argv
    
    input_path = cmd_list[1]
    output_path = cmd_list[2]
    url_list = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
 
    with open(input_path, "r") as fi:
        url_list = fi.readlines()
        for row in url_list:
            dict = {}
            try:
                ret = requests.get(row, headers = headers)
            except TimeoutError:
                print("Error|", row, ":Connection to this page time out")
                continue
                
            if ret.status_code < 200 or ret.status_code >= 400:
                print("Error|", row, ":This page returns", ret.status_code)
                continue
            else:    
                if ret.status_code == 301 or ret.status_code == 302:
                    ret = get_url(ret)

            ret.encoding = "utf-8"
            html = ret.text

            dict["phone"] = re.findall(r"(?<=[^0-9a-zA-Z_])(\d{7,8}|\d{11})(?=[^0-9a-zA-Z_])", html)
            dict["name"] = re.findall(r"(?<=姓名[:：])(.*?)[,;\"，。；“”\n\r]", html)
            dict["name"] = dict["name"] + re.findall(r"(?<=name[:：])(.*?)[,;\"，。；“”\n\r]", html)
            dict["url"] = re.findall(r"\s*(?<=[\s,.;，。；])网址[:：]\s*(https?://.*?)(?=[,;\"，。；“”\s])", html)
            dict["shared"] = re.findall(r"[^\n\r]*链接[^\n\r]*提取码[^\n\r]*", html)

            js = json.dumps(dict, ensure_ascii = False)
            row_list = []
            row_list = row.split("/")
            outpath = output_path + "/" + row_list[len(row_list) - 1]

            with open(outpath, "w", encoding = "utf-8") as fo:
                fo.write(js)

#input.txt outputs
if __name__=="__main__":
    analyse()
