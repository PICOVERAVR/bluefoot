
window.onload = function() {
    console.log("Page Loaded");
    pdf0Scroll = 0;

    // var loadingTask = pdfjsLib.getDocument('http://www.africau.edu/images/default/sample.pdf');
    // loadingTask.promise.then(function(pdf) {
    //     console.log(pdf.view);
    // });

    var socket = io.connect('http://127.0.0.1:5000');
    socket.on('connect', function() {
        socket.emit("chungus-ready", 'Chungus: User has connected.');
    });

    // Listen for chungus init from Flask App
        // initializes iframe size(s)
    socket.on('chungus-init', function(iframes) {
        var iframe;
        var iframeDiv;
        iframes.forEach(element => {
            iframe = document.getElementById(element);
            // iframeDiv = document.getElementById('div-' + element);
            // console.log(iframe.scrolling);
            // console.log('fscroll ' + iframe.scrollHeight);
            // console.log('fclient ' + iframe.clientHeight);
            // console.log('dscroll ' + iframeDiv.scrollHeight);
            // console.log('dclient ' + iframeDiv.clientHeight);
            // console.log('ftop ' + iframe.scrollTop);
            // console.log('dtop ' + iframeDiv.scrollTop);
            // iframe.style.height = (iframe.scrollHeight * 2) + 'px';
        });
    });

    // Listen for pdf scroll from Flask App
    socket.on('pdf-scroll-event', function(msg) {
        // console.log(msg);
        if (msg[0] === 'Down') {
            pdfScroll(msg[1], 0)
        }
        else if (msg[0] === 'Up') {
            pdfScroll(msg[1], 1)
        }
    });
}

function pdfScroll(frame_name, dir) {
    var iframe = document.getElementById(frame_name);
    var iframeDiv = document.getElementById('div-' + frame_name);
    if (iframeDiv == null || iframe == null) return;
    // console.log(pdf0Scroll);
    
    var scrollTarget = iframeDiv.scrollTop;
    (dir ? scrollTarget -= 30 : scrollTarget += 30);
    if (scrollTarget < 0) scrollTarget = 0;
    iframeDiv.scrollTo({
        top: scrollTarget,
        // behavior: 'smooth'
    });

    // If we didn't scroll enough (hit bottom of div), increase height and scroll again
    if (iframeDiv.scrollTop < (scrollTarget) && !dir) {
        console.log(iframeDiv.scrollTop + '/' + scrollTarget);
        iframe.style.height = (iframe.offsetHeight + 500) + 'px';
        iframeDiv.scrollTo({
            top: scrollTarget,
            behavior: 'smooth'
        });
    }

    // console.log(iframe.scrolling);
    // console.log('fscroll ' + iframe.scrollHeight);
    // console.log('fclient ' + iframe.clientHeight);
    // console.log('dscroll ' + iframeDiv.scrollHeight);
    // console.log('dclient ' + iframeDiv.clientHeight);
    // console.log('ftop ' + iframe.scrollTop);
    // console.log('dtop ' + iframeDiv.scrollTop);
}
