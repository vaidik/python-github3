#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Model(object):

    dates = ()
    maps = {}
    collection_maps = {}

    def __init__(self, attrs):
        """ """
        self.attrs = attrs

    def __getattr__(self, name):
        try:
            return self.attrs[name]
        except KeyError:
            raise AttributeError

    @classmethod
    def loads(self, raw_resource):
        def parse_date(string_date):
            from datetime import datetime
            try:
                date = datetime.strptime(string_date, '%Y-%m-%dT%H:%M:%SZ')
            except TypeError:
                date = None
            return date

        def parse_map(model, raw_resource):
            if hasattr(raw_resource, 'items'):
                return model.loads(raw_resource)

        def parse_collection_map(model, raw_resources):
            # Dict of resources (Ex: Gist file)
            if hasattr(raw_resources, 'items'):
                dict_map = {}
                for key, raw_resource in raw_resources.items():
                    dict_map[key] = model.loads(raw_resource)
                return dict_map
            # list of resources
            elif hasattr(raw_resources, '__iter__'):
                return [model.loads(raw_resource)
                        for raw_resource in raw_resources]
        raw_resource.update(
            {attr: parse_date(raw_resource[attr])
             for attr in self.dates if attr in raw_resource})
        raw_resource.update(
            {attr: parse_map(model, raw_resource[attr])
             for attr, model in self.maps.items()
             if attr in raw_resource})
        raw_resource.update(
            {attr: parse_collection_map(model, raw_resource[attr])
             for attr, model in self.collection_maps.items()
             if attr in raw_resource})

        return self(raw_resource)
