var video = document.querySelector("#videoElement");
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
 
if (navigator.getUserMedia) {       
    navigator.getUserMedia({video: true}, handleVideo, videoError);
}
 
function handleVideo(stream) {
    video.src = window.URL.createObjectURL(stream);
}
 
function videoError(e) {
   alert("Please allow camera access on your browser to activate camera!");
}

// Trigger photo take
document.getElementById("snap-btn").addEventListener("click", function() {
	context.drawImage(video, 0, 0, 350, 280);
});