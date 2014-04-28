# -*- coding: utf-8 -*-
from sys import argv
from random import sample


env = [u'용기', u'교만', u'시기', u'분노', u'나태', u'탐욕', u'식탐', u'색욕',
       u'사랑', u'증오', u'졸림', u'기쁨', u'환호', u'우울', u'빡침' ]


if __name__ == '__main__':
    if len(argv) < 2:
        print '이름을 입력해주세요.'
    else:
        encoded_name = argv[1].encode('hex')
        env_num = (int(encoded_name[0], 16) % 4) + 3
        name_len = len(encoded_name[0:])
        n = name_len // env_num
        s = [int(encoded_name[x:(x + 2)], 16) for x in xrange(0, name_len / n)]
        sum_ = sum(s)
        p = map(lambda x: (x / float(sum_)) * 100, s)
        user_env = sample(env, env_num)
        for x in zip(user_env, p):
            print '%s - %.2f' % x
