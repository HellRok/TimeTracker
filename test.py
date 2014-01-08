#!/usr/bin/env python3

from tt_class import tt_class

t = tt_class()

t.add_heading("Blah")

t.get_headings()
for h in t.headings:
	print(h.heading, len(h.children))

print(t.headings[0].times[0].pretty_start())
