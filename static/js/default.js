
function doNavigate(name) {
	/*alert(name);*/
	/*document.all.hideShow.style.visibility = 'hidden'; */
	hideAll();
	document.getElementById(name).classList.remove('hide');
	document.getElementById(name).classList.add('show');
}

function hideAll() {
	var modules = document.getElementsByClassName('module');
	for (var i=0,len=modules.length; i<len; i++) {
		modules[i].classList.remove('show');
		modules[i].classList.add('hide');
	}
}

function setDateAgo() {
	var elements = document.getElementsByClassName('time-ago');
	var now = new Date();
	for (var i=0,len=elements.length; i<len; i++) {
		var element = elements[i];
		var original = element.innerHTML;
		var updated = new DateAgo(now, new Date(original)).get()
		element.innerHTML = updated;
	}
}
