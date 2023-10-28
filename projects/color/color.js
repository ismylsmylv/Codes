function getRandomColorCode() {
    const getRandomRGBValue = () => Math.floor(Math.random() * 256);
    const r = getRandomRGBValue();
    const g = getRandomRGBValue();
    const b = getRandomRGBValue();
    return `rgb(${r}, ${g}, ${b})`;
  }
  
function assignRandomColorToElements() {
    const colorDisplay = document.getElementById('colorDisplay');
    const options = document.querySelectorAll('.options button');
    const randomColor = getRandomColorCode();
    colorDisplay.textContent = randomColor;
  
    // Assign the random color to one of the options
    const randomIndex = Math.floor(Math.random() * options.length);
    const colorForSelected = getRandomColorCode();
    options[randomIndex].style.backgroundColor = colorForSelected;
    colorDisplay.textContent = colorForSelected; // Update h2 with the new color
  
    // Reset the color for the other options
    for (let i = 0; i < options.length; i++) {
      if (i !== randomIndex) {
        options[i].style.backgroundColor = getRandomColorCode();
      }
    }
  }
  function checkOption(clickedElement) {
    const colorDisplay = document.getElementById('colorDisplay');
    const currentColor = colorDisplay.textContent;
  
    // Get the computed background color of the clicked button
    const computedStyle = window.getComputedStyle(clickedElement);
    const selectedColor = computedStyle.backgroundColor;
  
    if (selectedColor && currentColor === selectedColor) {
      alert('Congratulations! You guessed the correct color!');
      assignRandomColorToElements();
    } else if (selectedColor) {
      alert('Try again. You selected the wrong color.');
    } else {
      alert('Please choose a color before clicking.');
      // Or you can give the user a hint or take any other appropriate action here.
    }
  }
assignRandomColorToElements();