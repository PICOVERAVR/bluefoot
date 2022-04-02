
var pdf0Scroll = 0;

window.onload = function() {
    console.log("Page Loaded");
    pdf0Scroll = 0;
    var socket = io.connect('http://127.0.0.1:5000');
    socket.on('connect', function() {
        socket.send('User has connected.');
    });

    // Listen for message from Flask App
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

function pdfScroll(div_frame_name, dir) {
    // console.log("Entered scroll");
    var iframeDiv = document.getElementById(div_frame_name);
    if (iframeDiv == null) return;
    // console.log(pdf0Scroll);
    
    (dir ? pdf0Scroll -= 30 : pdf0Scroll += 30);
    if (pdf0Scroll < 0) pdf0Scroll = 0;
    iframeDiv.scrollTo({
        top: pdf0Scroll,
        behavior: 'smooth'
    });
}
