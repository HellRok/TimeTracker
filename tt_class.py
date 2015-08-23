from math import floor
import sqlite3
DB = sqlite3.connect("TT.sqlite", check_same_thread=False)
cursor = DB.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS TimeTracker (
  parent INTEGER,
  heading TEXT,
  is_time BOOLEAN,
  start_time INTEGER,
  end_time INTEGER
);''')
DB.commit()

class tt_class():
  def __init__(self):
    self.get_headings()

  def get_headings(self):
    self.headings = []
    cursor.execute("SELECT ROWID, parent, heading FROM TimeTracker WHERE parent IS NULL ORDER BY rowid DESC;")
    results = cursor.fetchall()
    for result in results:
      self.headings.append(heading_class(result[0], result[2]))

  def add_heading(self, heading, parent=None):
    cursor.execute("INSERT INTO TimeTracker VALUES (?,?,NULL,NULL,NULL);", (parent, heading))
    DB.commit()

  def update_heading(self, rowid, heading):
    cursor.execute("UPDATE TimeTracker SET heading = ? WHERE rowid = ?;", (heading, rowid))
    DB.commit()

  def add_time(self, parent):
    cursor.execute("INSERT INTO TimeTracker VALUES (?,NULL,1,NULL,NULL);", (parent,))
    DB.commit()

  def update_time(self, rowid, start, end):
    print(start, end, rowid)
    cursor.execute("UPDATE TimeTracker SET start_time = ? WHERE rowid = ?;", (start, rowid))
    cursor.execute("UPDATE TimeTracker SET end_time = ? WHERE rowid = ?;", (end, rowid))
    DB.commit()

  def remove(self, rowid):
    cursor.execute("DELETE FROM TimeTracker WHERE rowid = ?;", (rowid,))
    DB.commit()

  def pretty_time(self, time):
    if not time:
      return ""
    else:
      hours = floor(time/60)
      minutes = time%60
      return str(hours)+":"+str(minutes).zfill(2)

class heading_class():
  def __init__(self, rowid, heading):
    self.rowid = rowid
    self.heading = heading
    self.children = self.get_headings()
    self.times = self.get_times()

  def get_headings(self):
    cursor.execute("SELECT ROWID, parent, heading FROM TimeTracker WHERE parent = ? AND is_time IS NULL;", (self.rowid,))
    results = cursor.fetchall()
    to_return = []
    for result in results:
      to_return.append(heading_class(result[0], result[2]))
    return to_return

  def get_times(self):
    cursor.execute("SELECT ROWID, start_time, end_time FROM TimeTracker WHERE is_time = 1 AND parent = ?;", (self.rowid,))
    results = cursor.fetchall()
    to_return = []
    for result in results:
      to_return.append(time_class(result[0], result[1], result[2]))
    return to_return

  def get_all_times(self):
    ids = [time.rowid for time in self.get_times()]
    for heading in self.get_headings():
      ids += [time.rowid for time in heading.get_all_times()]

    ids = [str(id) for id in ids]
    to_return = []

    if ids:
      query = "SELECT ROWID, start_time, end_time FROM TimeTracker WHERE rowid = " + (" OR rowid = ".join(ids)) + " ORDER BY start_time;"
      print(query)
      cursor.execute(query)
      results = cursor.fetchall()

      for result in results:
        to_return.append(time_class(result[0], result[1], result[2]))

    return to_return

  def get_break_time(self):
    break_time = 0
    times = self.get_all_times()

    old_time = 0
    for time in times:
      if old_time != 0:
        break_time += time.start - old_time
      old_time = time.end

    return break_time

  def total_time(self):
    total = 0
    for t in self.times:
      total += t.total_time()
    for h in self.children:
      total += h.total_time()
    return total

class time_class():
  def __init__(self, rowid, start_time=0, end_time=0):
    self.rowid = rowid
    self.start = start_time
    self.end = end_time

  def update(self, start_time=None, end_time=None):
    cursor.execute("UPDATE TimeTracker SET start_time = ?, end_time = ? WHERE ROWID = ?;", (start_time, end_time, self.rowid))
    DB.commit()

  def total_time(self):
    if not self.start or not self.end:
      return 0
    else:
      return self.end - self.start
