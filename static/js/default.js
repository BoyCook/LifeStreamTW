var app = undefined;

var Router = Backbone.Router.extend({
    initialized: true,
    routes: {
    	"home": 		"home",
    	"blog": 		"blog",
        "blog/:title": 	"blog",
        "tweet": 		"tweet",
        "tweet/:id":	"tweet",
        "github":		"github"
    },
    home: function() {
    	app.navigate('home');
    },        
    blog: function() {
    	app.navigate('blog');
    },    
    tweet: function() {
        app.navigate('tweet');
    },
    github: function() {
    	app.navigate('github');
    },        
});

function SPA() {

}

SPA.prototype.showBlogs = function() {
		
};

SPA.prototype.showBlog = function(id) {
		
};

SPA.prototype.showTweets = function() {
		
};

SPA.prototype.showTweet = function(id) {
		
};

SPA.prototype.navigate = function(name) {
	/*alert(name);*/
	/*document.all.hideShow.style.visibility = 'hidden'; */
	this.hideAll();
	document.getElementById(name).classList.remove('hide');
	document.getElementById(name).classList.add('show');	
};

SPA.prototype.hideAll = function() {
	var modules = document.getElementsByClassName('module');
	for (var i=0,len=modules.length; i<len; i++) {
		modules[i].classList.remove('show');
		modules[i].classList.add('hide');
	}
};

SPA.prototype.setDateAgo = function() {
	var elements = document.getElementsByClassName('time-ago');
	var now = new Date();
	for (var i=0,len=elements.length; i<len; i++) {
		var element = elements[i];
		var original = element.innerHTML;
		var updated = new DateAgo(now, new Date(original)).get()
		element.innerHTML = updated;
	}
};

$(document).ready(function () {
	app = new SPA();
	new Router();
	Backbone.history.start();
	app.navigate('home');
	app.setDateAgo();            
});
