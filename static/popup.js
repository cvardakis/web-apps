// popup.js

// Attach click event listener to all elements with the 'triggerImage' class
var triggerImages = document.getElementsByClassName('triggerImage');
Array.from(triggerImages).forEach(function(triggerImage) {
    triggerImage.addEventListener('click', function() {
        openImagePopup(this.src); // Pass the image source to the popup function
    });
});

function openImagePopup(imageSrc) {
    // Create popup container
    var popup = document.createElement('div');
    popup.id = 'popup';
    popup.style.position = 'fixed';
    popup.style.top = '0';
    popup.style.left = '0';
    popup.style.width = '100%';
    popup.style.height = '100%';
    popup.style.backgroundColor = 'rgba(0, 0, 0, 0.8)'; // semi-transparent black background
    popup.style.display = 'flex';
    popup.style.justifyContent = 'center';
    popup.style.alignItems = 'center';
    popup.style.zIndex = '9999';

    // Create image element
    var image = document.createElement('img');
    image.src = imageSrc;
    image.style.maxWidth = '90%';
    image.style.maxHeight = '90%';

    // Append image to popup container
    popup.appendChild(image);

    // Append popup container to the body
    document.body.appendChild(popup);

    // Close popup when clicking outside the image
    popup.onclick = function(event) {
        if (event.target == this) {
            this.parentNode.removeChild(this); // Remove the popup from the DOM
        }
    };
}
