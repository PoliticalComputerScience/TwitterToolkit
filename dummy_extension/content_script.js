function score_tweets() {
    var i = 0;
    alert("page has loaded");
    $('.tweet').each(function(index){
        if (i == 0) {
            var t = $(this).find('.ProfileTweet-actionList'); //gets action button list
            var h = document.createElement("div");
            /*$.get(chrome.extension.getURL('/button.html'), function(data) {
                t.append(data);
    // Or if you're using jQuery 1.8+:
    // $($.parseHTML(data)).appendTo('body');
});*/
            t.append(h);
            alert(t.children().length) //should be 5

            var text = $(this).find('.tweet-text').html(); //gets tweet text
            var xhr = new XMLHttpRequest(); //beginning an HTTP request
            xhr.open("GET", "http://127.0.0.1:5000/score?tweet=" + encodeURIComponent(text), true);
            xhr.onreadystatechange = function() { // callback function
                if (xhr.readyState == 4) {
                    alert("received data from server");
                    alert(xhr.responseText)//JSON.parse(xhr.responseText));
                }
            }
            xhr.send(); // sends request
        }
        i++;
    });

}
score_tweets();
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    score_tweets();
 });
