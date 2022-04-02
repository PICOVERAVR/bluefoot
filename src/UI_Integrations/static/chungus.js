
var pdf0Scroll = 0;

window.onload = function() {
    console.log("Page Loaded");
    pdf0Scroll = 0;
}

function pdfScrollDown() {
    console.log("Entered scroll-down");
    var iframeDiv = document.getElementById("div-frame-0");
    if (iframeDiv == null) return;
    // console.log(pdf0Scroll);
    pdf0Scroll += 30;
    document.getElementById('div-frame-0').scrollTo({
        top: pdf0Scroll,
        behavior: 'smooth'
    });
}

function pdfScrollUp(currentScroll) {
    console.log("Entered scroll-down");
    var iframeDiv = document.getElementById("div-frame-0");
    if (iframeDiv == null) return;
    // console.log(pdf0Scroll);
    pdf0Scroll -= 30;
    if (pdf0Scroll < 0) pdf0Scroll = 0;
    document.getElementById('div-frame-0').scrollTo({
        top: pdf0Scroll,
        behavior: 'smooth'
    });
}