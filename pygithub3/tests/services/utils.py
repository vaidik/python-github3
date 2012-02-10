#!/usr/bin/env python
# -*- encoding: utf-8 -*-

base_url = 'https://api.github.com/'

def _(request):
    return "%s%s" % (base_url, request)
