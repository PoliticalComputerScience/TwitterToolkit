var i = 0;
alert("page has loaded");
$('.tweet').each(function(index){
    if (i == 0) {
        var t = $(this).find('.ProfileTweet-actionList'); //gets action button list
        var h = document.createElement("div");
        t.append(h);
        alert(t.children().length) //should be 5

        var text = $(this).find('.tweet-text').text(); //gets tweet text
        var xhr = new XMLHttpRequest(); //beginning an HTTP request
        xhr.open("GET", "http://127.0.0.1:5000/score?tweet=" + encodeURIComponent(text), true);
        xhr.onreadystatechange = function() { // callback function
            if (xhr.readyState == 4) {
                alert("received data from server");
                alert(xhr.response.json());
            }
        }
        xhr.send(); // sends request
    }
    i++;
});
