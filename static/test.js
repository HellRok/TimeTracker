test( "TimeTracker class", function() {
	equal( TT.element, document.getElementById("TimeTrackerContainer"), "Sets element to the TTContainer");
	equal( TT.children.length, 0, "Initializes with 0 children");
});

test( "TT#create_day", function() {
	TT.create_day();
	equal( TT.children.length, 1, "Creates a child element");
	TT.children[0].create();
	equal( TT.element.getElementsByTagName("li").length, 1, "Creates 1 li");
	equal( TT.element.getElementsByTagName("button").length, 3, "Creates 3 buttons");
	equal( TT.element.getElementsByTagName("span").length, 4, "Creates 4 spans");
	equal( TT.element.getElementsByTagName("strong").length, 1, "Creates 1 strong");
});
