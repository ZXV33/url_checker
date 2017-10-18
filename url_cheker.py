#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
import sys
import time

# CSV読み込み
try:
    csvfile = open(sys.argv[1], newline='')
except:
    print("CSVファイルを指定してください")
    exit(1)


# proxy connetion setting
proxy_ip = '${your ip}'
proxy_port = ${your port}
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1) 
profile.set_preference('network.proxy.share_proxy_settings', True) 
profile.set_preference('network.proxy.socks_remote_dns', True) 
profile.set_preference('network.proxy.http.use-cache', False) 
profile.set_preference('network.proxy.http', proxy_ip) 
profile.set_preference('network.proxy.http_port', proxy_port) 
profile.set_preference('network.proxy.ssl', proxy_ip) 
profile.set_preference('network.proxy.ssl_port', proxy_port) 
profile.set_preference('network.proxy.ftp', proxy_ip) 
profile.set_preference('network.proxy.ftp_port', proxy_port) 
profile.set_preference('network.proxy.socks', proxy_ip) 
profile.set_preference('network.proxy.socks_port', proxy_port) 
profile.update_preferences()

    
# URLへのアクセスと証跡の取得

driver = webdriver.Firefox(firefox_profile=profile)

parsecsv = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in parsecsv:
    try:
        driver.get(row[0])
        time.sleep(5)
        driver.save_screenshot(row[1])
    except:
        print("error:"+row[0])
