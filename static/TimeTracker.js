function update_heading(id) {
	var heading = document.getElementById(id).getElementsByClassName("form-control")[0].value;
	document.getElementById(id).getElementsByClassName("heading-text")[0].innerHTML = heading;
	$.ajax("/update_heading/?heading="+heading+"&rowid="+id);
};

function update_time(id) {
	var start_time = document.getElementById(id).getElementsByClassName("start")[0].value;
	var end_time = document.getElementById(id).getElementsByClassName("end")[0].value;
	var url = "/update_time/?rowid="+id;
	if (start_time) {
		url += "&start="+ start_time;
	};
	if (end_time) {
		url += "&end="+ end_time;
	};
	console.log(url);
	$.ajax(url).done(function(data){update_body(data);});
};

function add_heading(parent_id, heading) {
	var url = "/add_heading/?";
	if (parent_id) {
		url += "parent=" + parent_id +"&";
	};
	url += "heading="+ heading;
	$.ajax(url).done(function(data){update_body(data);});
};

function add_time(parent_id) {
	$.ajax("/add_time/?parent="+ parent_id).done(function(data){update_body(data);});
};

function remove_row(rowid) {
	$.ajax("/remove/?rowid="+ rowid).done(function(data){update_body(data);});
};

function update_body(response) {
	document.getElementById("TimeTrackerContainer").innerHTML = response;
};
