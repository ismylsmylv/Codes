// Initialize variables
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let painting = false;

// Set canvas size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Event listeners for drawing
function startPosition(e) {
  painting = true;
  draw(e);
}

function endPosition() {
  painting = false;
  ctx.beginPath();
}

function draw(e) {
  if (!painting) return;

  ctx.lineWidth = 5;
  ctx.lineCap = 'round';
  ctx.strokeStyle = '#c9c9c9';

  ctx.lineTo(e.clientX, e.clientY);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX, e.clientY);
}

// Event listeners for touch devices
canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  startPosition(e.touches[0]);
});

canvas.addEventListener('touchend', () => endPosition());

canvas.addEventListener('touchmove', (e) => {
  e.preventDefault();
  draw(e.touches[0]);
});

// Event listeners for mouse devices
canvas.addEventListener('mousedown', startPosition);
canvas.addEventListener('mouseup', endPosition);
canvas.addEventListener('mousemove', draw);

// Clear canvas
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Event listener for clear button
const clearButton = document.getElementById('clearButton');
clearButton.addEventListener('click', clearCanvas);
