# -*- encoding: utf-8 -*-

from pyamf.flex import ArrayCollection

def acpb(data):
    print data
#    return data
    v = [{'col1':u'value c', 'col2':3}, {'col1':u'value d', 'col2':4}]
    ac = ArrayCollection(v)
    print ac
    return ac
