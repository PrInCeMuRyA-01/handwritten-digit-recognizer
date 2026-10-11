const canvas = document.getElementById('paintCanvas');
const ctx = canvas.getContext('2d');
const clearBtn = document.getElementById('clearBtn');
const predictBtn = document.getElementById('predictBtn');
const predictedDigitEl = document.getElementById('predictedDigit');
const confidenceValEl = document.getElementById('confidenceVal');

let isDrawing = false;

function initCanvas() {
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 18;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
}

initCanvas();

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
});

canvas.addEventListener('mousemove', (e) => {
    if (isDrawing) {
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
    }
});

canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseleave', () => isDrawing = false);

clearBtn.addEventListener('click', () => {
    initCanvas();
    predictedDigitEl.textContent = '-';
    confidenceValEl.textContent = '-';
});

predictBtn.addEventListener('click', async () => {
    const imageData = canvas.toDataURL('image/png');

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: imageData })
        });

        const result = await response.json();

        if (response.ok) {
            predictedDigitEl.textContent = result.digit;
            confidenceValEl.textContent = result.confidence;
        } else {
            alert('Error making prediction: ' + result.error);
        }
    } catch (err) {
        console.error(err);
        alert('Failed to connect to server.');
    }
});