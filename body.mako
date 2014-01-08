<%def name="time_block(time, indent=0)">
	<li class="list-group-item" id="${time.rowid}">
		${"&nbsp;"*indent*4}
		<input type="text" class="form-control input-sm time start" value="${TT.pretty_time(time.start)}" placeholder="Start" onblur="update_time(${time.rowid});">
		<input type="text" class="form-control input-sm time end" value="${TT.pretty_time(time.end)}" placeholder="End" onblur="update_time(${time.rowid});">
		<span class="pull-right buttons">
			<a href="/remove/?rowid=${time.rowid}">
				<button class="btn btn-xs btn-danger">
					<span class="glyphicon glyphicon-minus">
				</button>
			</a>
			<em>${TT.pretty_time(time.total_time())}</em>
		<span>
	</li>
</%def>
<%def name="heading_block(heading, indent=0)">
	<li class="list-group-item" id="${heading.rowid}">
		${"&nbsp;"*indent*4}
		<span class="heading-text">
			${heading.heading}
		</span>
		<span class="heading-form">
			<input type="text" class="form-control input-sm" value="${heading.heading}" placeholder="No Heading" onblur="update_heading(${heading.rowid});">
		</span>
		<span class="pull-right buttons">
			<a href="/add_heading/?parent=${heading.rowid}&heading=New%20Heading">
				<button class="btn btn-xs">
					<span class="glyphicon glyphicon-list"></span>
				</button>
			</a>
			<a href="/add_time/?parent=${heading.rowid}">
				<button class="btn btn-xs">
					<span class="glyphicon glyphicon-time"></span>
				</button>
			</a>
			<a href="/remove/?rowid=${heading.rowid}">
				<button class="btn btn-xs btn-danger">
					<span class="glyphicon glyphicon-minus">
				</button>
			</a>
			<strong>${TT.pretty_time(heading.total_time())}</strong>
		</span>
	</li>
	% for time in heading.times:
		${time_block(time=time, indent=indent+1)}
	% endfor
	% for heading in heading.children:
		${heading_block(heading=heading, indent=indent+1)}
	% endfor
</%def>

% for heading in TT.headings:
	${heading_block(heading=heading)}
% endfor
