#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/wxl/wx', 'Handle',
)

app = web.application(urls, globals())
application = app.wsgifunc()
