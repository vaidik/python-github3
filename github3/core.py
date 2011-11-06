#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

class Paginate:
    """ Paginate resource iterator

    :param resource: URL resource
    :param requester: Bound method to request. See `GithubCore.get`
    """

    def __init__(self, resource, requester):
        self.resource = resource
        self.requester = requester
        self.page = 1

    def _last_page(self, link):
        """ Get and cached last page from link header """
        if not getattr(self, 'last', False):
            from github3.packages.link_header import parse_link_value
            from urlparse import urlparse, parse_qs
            for link, rels in parse_link_value(link).items():
                if rels.get('rel') == 'last':
                    query = urlparse(link).query
                    self.last = int(parse_qs(query).get('page').pop())

        return self.last

    def __iter__(self):
        return self

    def initial(self):
        """ First request. Force requester to paginate returning link header """
        link, content = self.requester(self.resource, paginate=True, page=1)
        self.last = self._last_page(link) if link else 1
        return content

    def next(self):
        if self.page == 1:
            content = self.initial()
            self.page += 1
            return content
        else:
            if self.page > self.last:
                raise StopIteration
            else:
                content = self.requester(self.resource, page=self.page)
                self.page += 1
                return content

class Modelizer(object):
    """ Converter json into model and vice versa """

    def __init__(self, model):
        self.model = model
        self.attrs = {}

    def _parse_date(self, string_date):
        from datetime import datetime
        try:
            date = datetime.strptime(string_date, '%Y-%m-%dT%H:%M:%SZ')
        except TypeError:
            date = None

        return date

    def _parse_map(self, model, raw_resource):
        if model == 'self':
            model = self.model

        return Modelizer(model).loads(raw_resource)

    def _parse_collection_map(self, model, raw_resources):
        # Dict of resources (Ex: Gist file)
        if getattr(raw_resources, 'items', False):
            dict_map = {}
            for key, raw_resource in raw_resources.items():
                dict_map[key] = Modelizer(model).loads(raw_resource)
            return dict_map
        # list of resources
        else:
            return [Modelizer(model).loads(raw_resource)
                    for raw_resource in raw_resources]

    def loads(self, raw_resource):
        attrs = {}
        idl = self.model.idl()
        attrs.update(
            {attr: raw_resource[attr] for attr in idl.get('strs',())
             if raw_resource.get(attr)})
        attrs.update(
            {attr: raw_resource[attr] for attr in idl.get('ints',())
             if raw_resource.get(attr)})
        attrs.update(
            {attr: self._parse_date(raw_resource[attr])
             for attr in idl.get('dates',()) if raw_resource.get(attr)})
        attrs.update(
            {attr: raw_resource[attr] for attr in idl.get('bools',())
             if raw_resource.get(attr)})
        attrs.update(
            {attr: self._parse_map(model, raw_resource[attr])
             for attr, model in idl.get('maps',{}).items()
             if raw_resource.get(attr)})
        attrs.update(
            {attr: self._parse_collection_map(model, raw_resource[attr])
             for attr, model in idl.get('collection_maps',{}).items()
             if raw_resource.get(attr)})

        return self.model(attrs)

    def dumps(self):
        # return JSON
        pass
