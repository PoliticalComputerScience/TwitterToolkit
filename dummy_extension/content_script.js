function score_tweets() {
    var i = 0;
    //alert("page has loaded");
    $('.tweet').each(function(index){

        var t = $(this).find('.ProfileTweet-actionList'); //gets action button list
        $.get(chrome.extension.getURL('/button.html'), function(data) {
            if (t.children().length == 4) {
                t.append(data);
            }
        });
        var text = $(this).find('.tweet-text').html(); //gets tweet text
        var xhr = new XMLHttpRequest(); //beginning an HTTP request
        xhr.open("GET", "http://127.0.0.1:5000/score?tweet=" + encodeURIComponent(text), true);
        xhr.onreadystatechange = function () {//onreadystatechange = function() { // callback function
            if (xhr.readyState == 4 && xhr.status == 200) {
                try {
                alert("received data from server");
                alert(xhr.responseText);
                var str = xhr.responseText.replace(/'/g, '"');
                var obj = JSON.parse(str);
                alert(obj.domain);
            } catch (err) {
                alert(err);
            }
            }
        }
        xhr.send(); // sends request
        i++;

    });

}
score_tweets();
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    score_tweets();
 });

 function DOMModificationHandler(){
     $(this).unbind('DOMSubtreeModified.event1');
     setTimeout(function(){
         score_tweets();
         $('#timeline').bind('DOMSubtreeModified.event1',
                                    DOMModificationHandler);
     },10);
 }
 $('#timeline').bind('DOMSubtreeModified.event1',
                            DOMModificationHandler);
