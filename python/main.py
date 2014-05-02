# -*- coding: utf-8 -*-
from sys import argv
from naming import parse_name


if __name__ == '__main__':
    if len(argv) < 2:
        print '이름을 입력해주세요.'
    else:
        print argv[1]
        for e, p in parse_name(argv[1]):
            print '%s - %.2f' % (e, p * 100)
