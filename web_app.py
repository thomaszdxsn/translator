#! /usr/bin/env python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from collections import Iterable

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen



class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        query = self.get_argument('q')
        api = 'http://fanyi.youdao.com/openapi.do' \
              '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
        response = yield tornado.httpclient.AsyncHTTPClient().fetch(api + query)
        result = json.loads(response.body)
        translation = ",".join(result.get("translation")) if isinstance(result.get("translation"), Iterable) else ""
        try:
            explains = ','.join(result.get('basic').get('explains'))
        except:
            explains = ''

        self.write("""
                            <div style="text-align: center">
                                <div style="font-size: 72px">{}</div>
                                <div style="font-size: 144px">{}</div>
                                <div style="font-size: 24px">{}<div>
                            </div>
                        """.format(self.get_argument('q'), translation, explains))
        self.finish()



if __name__ == '__main__':
    from tornado.options import define, options

    define('port', default=8000, type=int)
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()