function update_heading(id) {
	var heading = document.getElementById(id).getElementsByClassName("form-control")[0].value;
	document.getElementById(id).getElementsByClassName("heading-text")[0].innerHTML = heading;
	$.ajax("/update_heading/?heading="+heading+"&rowid="+id);
};

function update_time(id) {
	var start_time = document.getElementById(id).getElementsByClassName("start")[0].value;
	var end_time = document.getElementById(id).getElementsByClassName("end")[0].value;
	console.log("/update_time/?rowid="+id+"&start="+start_time+"&end="+end_time);
	$.ajax("/update_time/?rowid="+id+"&start="+start_time+"&end="+end_time);
};
