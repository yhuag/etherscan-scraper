#!/usr/bin/env python
# encoding: utf-8

import lxml.etree
import lxml.html
import requests

ROOT = "https://ropsten.etherscan.io/"
TAR_ADDRESS = "0x5ff2c17ada131e5D9fa0f927395Abe35657e4768"

TOTAL_PAGE = 21


def getGasPrice(url):
    r = requests.get(url)
    root = lxml.html.fromstring(r.content)
    price_text = root.xpath('//div[20]//text()[2]')[0]
    return price_text


def main():
    allTxHash = []
    allGasPrice = []

    for pageIndex in range(TOTAL_PAGE):
        r = requests.get("https://ropsten.etherscan.io/txs?a="+ TAR_ADDRESS +"&p="+str(pageIndex))
        root = lxml.html.fromstring(r.content)
        tx_hash_list = root.xpath('//td[1]//text()')

        allTxHash = allTxHash + tx_hash_list

        for tx_hash in tx_hash_list:
            gasPrice = getGasPrice("https://ropsten.etherscan.io/tx/"+tx_hash)
            allGasPrice.append(gasPrice)
            print(gasPrice + ", " + tx_hash)

if __name__ == "__main__":
    main()