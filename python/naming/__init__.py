# -*- coding: utf-8 -*-
ENV = [u'용기', u'교만', u'시기', u'분노', u'나태', u'탐욕', u'식탐', u'색욕',
       u'사랑', u'증오', u'졸림', u'기쁨', u'환호', u'우울', u'빡침' ]


def pack_name(encoded):
    reversed_encoded = reversed(encoded)
    r = ''
    for i, x in enumerate(reversed_encoded):
        r += x
        r += encoded[i]
    return r


def pick_env(encoded_name):
    user_env = []
    env_num = 5 - int(encoded_name[0], 16) % 3
    for i, x in enumerate(encoded_name[1:]):
        if i > env_num:
            break
        this_env = ENV[int(x, 16)]
        if not this_env in user_env:
            user_env.append(this_env)
    return user_env


def pick_probability(enc, l):
    r = []
    for x in range(1, l + 1):
        c = list(set(enc[:x]))
        if len(c) == 1 and c[0] == '0':
            return pick_probability(enc[x:], l)
        else:
            r.append(int(enc[:x], 16))
            enc = enc[x:]
    a = float(sum(r))
    return map(lambda x: x / a, r)


def parse_name(name):
    encoded_name = pack_name(name.encode('hex'))
    user_env = pick_env(encoded_name)
    prob = pick_probability(encoded_name, len(user_env))
    return zip(user_env, prob)
