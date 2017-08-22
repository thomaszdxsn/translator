#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import requests
import json


api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='


def get_trans(word):
    query_api = api + word
    result = requests.get(query_api).content
    result = json.loads(result)
    return result



@click.command()
@click.argument("word")
def cli(word):
    """please enter a word used to translate"""
    result = get_trans(word)
    translation = ",".join(result.get("translation"))
    try:
        explains = ','.join(result.get('basic').get('explains'))
    except:
        explains = ''
    print "查询:", result.get("query")
    print "结果:", translation
    print "解释:", explains