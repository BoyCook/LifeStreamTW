
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

var Router = Backbone.Router.extend({
    initialized: true,
    routes: {
        "blog/:title": "blog",
        "tweet/:title": "tweet"
    },
    blog: function(title) {
        console.log('Blog [%s]', title);
    },
    tweet: function(title) {
        console.log('Tweet [%s]', title);
    }    
});


// $(document).ready(function () {
//     var loaded = function() {
//         new Router();
//         Backbone.history.start();
//     };
//     app = new SPA(window.location.hostname, window.location.port);
//     app.setup(loaded);
//     $('#filterBox').keyup(function (e) {
//         if (!(e.keyCode >= 37 && e.keyCode <= 40)) {
//             app.filter($('#filterBox').val());
//         }
//     });    
//     $('input:radio[name=searchType]').change(function() {
//         var list = $('input:radio[name=searchType]:checked').val();
//         $('#filterBox').val(app.filteredLists[list].text);
//         app.switchList(list);            
//     });   
// });
