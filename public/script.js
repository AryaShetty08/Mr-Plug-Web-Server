function drawGraph(canvasId, data, color, title, xAxisLabel, yAxisLabel) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext('2d');
  const padding = 60; // Ample padding to avoid overlap with the labels
  const graphHeight = canvas.height - padding * 2;
  const graphWidth = canvas.width - padding * 2;

  ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas for redrawing

  // Draw title centered
  ctx.font = '16px Arial';
  ctx.fillStyle = 'black';
  ctx.textAlign = 'center';
  ctx.fillText(title, canvas.width / 2, padding / 2);

  // Draw X-axis label
  ctx.fillText(xAxisLabel, canvas.width / 2, canvas.height - padding / 4);

  // Draw Y-axis label
  ctx.save(); // Save the current context state
  ctx.translate(padding / 4, canvas.height / 2);
  ctx.rotate(-Math.PI / 2);
  ctx.textAlign = 'center';
  ctx.fillText(yAxisLabel, 0, 0); // Change 'Power (kW)' to the appropriate Y-axis label
  ctx.restore(); // Restore the context to its original state

  // No Y-axis, but we still want to draw horizontal lines for reference
  ctx.lineWidth = 1;
  ctx.strokeStyle = '#ccc';
  const horizontalLines = 5;
  for (let i = 0; i <= horizontalLines; i++) {
    let y = graphHeight / horizontalLines * i + padding;
    ctx.beginPath();
    ctx.moveTo(padding, y);
    ctx.lineTo(canvas.width - padding, y);
    ctx.stroke();
  }

  // Draw the line graph
  ctx.beginPath();
  ctx.lineWidth = 2;
  ctx.strokeStyle = color;
  ctx.moveTo(padding, padding + graphHeight - data[0] * graphHeight); // Start at the first data point

  // Map the data points to the graph based on the graph height
  data.forEach((value, i) => {
    let x = (graphWidth / (data.length - 1)) * i + padding;
    let y = padding + graphHeight - value * graphHeight; // Assuming data is normalized between 0 and 1
    ctx.lineTo(x, y);
  });

  ctx.stroke();
}

// Generate fake data for demonstration
function generateFakeData(numPoints) {
  let data = [0.5]; // Starting point for the graph
  for (let i = 1; i < numPoints; i++) {
    // Generate points that moderately deviate from the previous point
    data.push(data[i - 1] + (Math.random() - 0.5) * 0.1);
    // Ensure values stay within the 0-1 range
    data[i] = Math.min(Math.max(data[i], 0), 1);
  }
  return data;
}

// Update the graphs every 2 seconds with new data
function updateGraphs() {
  const powerData = generateFakeData(50);
  const tempData = generateFakeData(50);
  drawGraph('powerGraph', powerData, 'rgba(255, 0, 0, 0.6)', 'Power Usage', 'Time (min)', 'Power (kW)');
  drawGraph('tempGraph', tempData, 'rgba(0, 0, 255, 0.6)', 'Temperature Change', 'Time (min)', 'Temperature (F)'); // Assuming the temp range is 10°C to 30°C
}

// Populate dropdowns with hours
const populateTimeOptions = () => {
  for (let i = 0; i < 24; i++) {
    let option = document.createElement('option');
    option.value = i;
    option.text = `${i}:00`;
    document.getElementById('outlet1-on').appendChild(option.cloneNode(true));
    document.getElementById('outlet1-off').appendChild(option.cloneNode(true));
    document.getElementById('outlet2-on').appendChild(option.cloneNode(true));
    document.getElementById('outlet2-off').appendChild(option.cloneNode(true));
  }
};

// Toggle adaptive learning
document.getElementById('adaptiveLearningBtn').addEventListener('click', function() {
  this.classList.toggle('active');
  this.textContent = this.classList.contains('active') ? 'Disable Adaptive Learning' : 'Enable Adaptive Learning';
});

// Dummy functionality for Set buttons
document.querySelectorAll('.set-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    alert('Settings applied (not really, but pretend).');
  });
});

// Toggle buttons at the top right corner
document.querySelectorAll('.outlet-button').forEach(button => {
  button.addEventListener('click', () => {
    const isOn = button.textContent.includes('Turn off');
    button.textContent = isOn ? 'Turn on Plug' : 'Turn off Plug';
    button.classList.toggle('active', isOn);
  });
});

populateTimeOptions();
setInterval(updateGraphs, 2000);
updateGraphs();
