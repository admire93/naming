# -*- coding: utf-8 -*-
from naming import pack_name, parse_name, pick_env, pick_probability

def test_reversed():
    expected = '0e8a4ba0c9e58eada99adae85e9c0ab4a8e0'
    name = '강효준'.encode('hex')
    assert expected == pack_name(name)


def test_pick_env():
    encoded = '0e8a4ba0c9e58eada99adae85e9c0ab4a8e0'
    l = pick_env(encoded)
    assert u'빡침' in l
    assert u'사랑' in l
    assert u'졸림' in l
    assert u'나태' in l
    assert u'기쁨' in l
    assert 5 == len(l)


def test_pick_probability():
    encoded = '0e8a4ba0c9e58eada99adae85e9c0ab4a8e0'
    ev = pick_env(encoded)
    prob = pick_probability(encoded, len(ev))
    expected_prob = [
        '0e8a4ba',
        '0c9e58e',
        'ada99ad',
        'ae85e9c',
        '0ab4a8e',
        '0',
    ]
    exp = map(lambda x: int(x, 16), expected_prob)
    a = float(sum(exp))
    exp = map(lambda x: x / a, exp)
    for p, e in zip(prob, exp):
        assert e == p
