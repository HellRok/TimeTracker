#!/usr/bin/env python3

from tt_class import tt_class
import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['.'])

TT = tt_class()

class Server(object):
  def index(self):
    TT.get_headings()
    t = lookup.get_template("index.mako")
    return t.render(TT=TT)
  index.exposed = True

  def add_heading(self, parent=None, heading=""):
    TT.add_heading(heading, parent)
    TT.get_headings()
    t = lookup.get_template("body.mako")
    return t.render(TT=TT)
  add_heading.exposed = True

  def update_heading(self, rowid, heading=""):
    TT.update_heading(rowid, heading)
    TT.get_headings
    t = lookup.get_template("body.mako")
    return t.render(TT=TT)
  update_heading.exposed = True

  def add_time(self, parent):
    TT.add_time(parent)
    TT.get_headings()
    t = lookup.get_template("body.mako")
    return t.render(TT=TT)
  add_time.exposed = True

  def update_time(self, rowid, start=None, end=None):
    if start:
      start_minutes = int(start.split(":")[0])*60+int(start.split(":")[1])
    else:
      start_minutes = 0
    if end:
      end_minutes = int(end.split(":")[0])*60+int(end.split(":")[1])
    else:
      end_minutes = 0
    TT.update_time(rowid, start_minutes, end_minutes)
    TT.get_headings()
    t = lookup.get_template("body.mako")
    return t.render(TT=TT)
  update_time.exposed = True

  def remove(self, rowid):
    TT.remove(rowid)
    TT.get_headings()
    t = lookup.get_template("body.mako")
    return t.render(TT=TT)
  remove.exposed = True

  def report(self):
    t = lookup.get_template("report.mako")
    return t.render(TT=TT)
  report.exposed = True

cherrypy.quickstart(Server(), '/', 'config')
