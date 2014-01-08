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
				<a href="/add_heading/?heading=New%20Heading">
					<button class="btn btn-xs">
						<span class="glyphicon glyphicon-list"></span>
					</button>
				</a>
			</div>
		</nav>
		<ul id="TimeTrackerContainer" class="list-group">
			<%include file="body.mako" />
		</ul>
		<script src="/static/TimeTracker.js"></script>
	</body>
</html>
