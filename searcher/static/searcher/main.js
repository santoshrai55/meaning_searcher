function myrefresh() {
  window.location.reload();
}
setTimeout("myrefresh()", 500); // Specify one refresh per second

function origin() {
  window.moveTo(-2600, 0);
}
origin();
resizeTo(800, 1000);
window.parent;
window.top;
