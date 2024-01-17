// script.js

function drawCircle(x, y, radius, color) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.lineWidth = 2;
  ctx.strokeStyle = "#000";
  ctx.stroke();
}

function checkOverlap(circle1, circle2) {
  var distanceBetweenCenters = Math.sqrt((circle2.x - circle1.x) ** 2 + (circle2.y - circle1.y) ** 2);
  var combinedRadii = circle1.radius + circle2.radius;
  return distanceBetweenCenters < combinedRadii;
}

function generateRandomCoordinates(largeRadius, smallRadius) {
  var x = centerX + (Math.random() - 0.5) * (largeRadius - smallRadius) * 2;
  var y = centerY + (Math.random() - 0.5) * (largeRadius - smallRadius) * 2;
  return { x, y };
}

// Get the canvas element
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

// Set properties for the large circle
var centerX = canvas.width / 2;
var centerY = canvas.height / 2;
var largeCircleRadius = 200;
var largeCircleColor = "#3498db";

// Draw the large circle
// drawCircle(centerX, centerY, largeCircleRadius, largeCircleColor);

// Set properties for the small circles
var smallCircleRadius = 10;

var numberOfSmallCircles = 2; // You can change this to any number

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function isTwoOrLikely(number) {
  if (numberOfSmallCircles < 4) {
    return true
  } 
  // Set a base probability threshold
  var baseThreshold = 0.7;

  // Adjust the threshold based on the input number
  var adjustedThreshold = baseThreshold / Math.sqrt(number);

  // Generate a random number between 0 and 1
  var randomValue = Math.random();

  // Check if the random value is below the adjusted threshold
  return randomValue < adjustedThreshold;
}
var smallCircleColor = "#e74c3c";
function simulate() {
  var circles = [];
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw and check for overlap for each small circle
  for (var i = 0; i < numberOfSmallCircles; i++) {
    
    var randomCoordinates = generateRandomCoordinates(largeCircleRadius, smallCircleRadius);
    var circle = {
      x: randomCoordinates.x,
      y: randomCoordinates.y,
      radius: smallCircleRadius
    };

    // Draw the small circle
    drawCircle(circle.x, circle.y, circle.radius, smallCircleColor);

    // Check for overlap with previous circles
    for (var j = 0; j < i; j++) {
      var previousCircle = {
        x: circles[j].x,
        y: circles[j].y,
        radius: circles[j].radius
      };

      if (checkOverlap(circle, previousCircle)) {
        
        if (isTwoOrLikely(numberOfSmallCircles)) {
          numberOfSmallCircles++
          console.log(numberOfSmallCircles)
        }
        smallCircleColor = getRandomColor();
        // break
      }
    }

    // Store the current circle for future checks
    circles.push(circle);
  }
}

setInterval(simulate, 400)
