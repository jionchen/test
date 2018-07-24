#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def time(t):
	print('TIME:', t)
	m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
	return print(m.groups())
def number(t):
	print('NUMBER:',t)
	m = re.match(r'^(\d{3})-(\d{3,8})$', t)
	return print(m.group(1), m.group(2))


z=input(">>>>>")
if  re.search(r'\:',z):
	time(z)
else:
	number(z)


