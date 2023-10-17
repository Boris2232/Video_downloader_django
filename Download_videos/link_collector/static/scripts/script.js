function scroll_to_end(){
  // The document is fully loaded
  document.addEventListener("DOMContentLoaded", function() {
    // choosing the last button of resolution
    const resolutionButtons = document.querySelectorAll(".resolution_button button");
    // check if the link is not empty
    if (resolutionButtons.length > 0) {
      const next_step=document.getElementById('next')
      next_step.scrollIntoView({behavior:'smooth'});
    }
  });
}
let luck=false
function start_point() {
        document.getElementById("start").scrollIntoView({ behavior: 'smooth' });
    }

function empty_alert_show() {
      alert("Input link")
}
function age_alert_show() {
  alert("This video is age restricted")
}
function congr(){
    alert('Downloading..')
}