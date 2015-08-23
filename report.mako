<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Time Tracker</title>
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <link href="/static/TimeTracker.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-default" role="navigation">
      <div class="navbar-header">
        <span class="navbar-brand">Time Tracker</span>
      </div>
    </nav>

    <ul>
      % for heading in TT.headings:
        <li>${heading.heading}</li>
        <ul>
          <li>Total: ${TT.pretty_time(heading.total_time())}</li>
          <li>Break: ${TT.pretty_time(heading.get_break_time())}</li>
          <li>Start: ${TT.pretty_time(heading.get_all_times()[0].start)}</li>
          <li>End: ${TT.pretty_time(heading.get_all_times()[-1].end)}</li>
        </ul>
      % endfor
    </ul>
  </body>
</html>

