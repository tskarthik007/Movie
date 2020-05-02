var api_key = "15d2ea6d0dc1d476efbca3eba2b9bbfb";
var baseimg = "http://image.tmdb.org/t/p/w185";


var count=0;
var getPoster = function(arr){
    // this gets rid of the warning about using return false
	  arr.forEach(element => {
	  element=element.toString();

	  film=element;
	  console.log(film);
	  $.getJSON("https://api.themoviedb.org/3/search/movie?query=" +
	  escape(film)  +
		"&api_key=" +
		api_key     +
		"&callback=?",
	  function(json) {
	  // console.log(json);
	  // console.log(json.results[0].poster_path);
		  if (json.total_results) {
			  $('#poster'+count).html('<img id="thePoster" src=' + baseimg + json.results[0].poster_path + ' />'+'<p>'+element+'</p>');
			  count=count+1;
		  } 
		}
	  );
	});


	}