document.getElementById('showStorefrontBtn').addEventListener('click', function() {
    // Show the storefront prompt
    var prompt = document.getElementById('storefrontPrompt');
    prompt.style.display = 'block';

    // Load HTML content dynamically using Fetch API
    fetch(`/get_new_store_details`)
        .then(response => response.text())
        .then(htmlContent => {
            prompt.innerHTML = htmlContent;

            // Add event listener for form submission
            document.getElementById('storefrontForm').addEventListener('submit', function(event) {
                event.preventDefault();

                // Use Fetch API to make an AJAX request
                fetch(`/add_new_store/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    },
                    body: new URLSearchParams(new FormData(event.target)),
                })
                .then(response => response.json())
                .then(data => {
                    // Check if the response contains a success message
                    if (data.message === "Sign Up Successful") {
                        // Display the success message
                        var successMessageContainer = document.getElementById('successMessageContainer');
                        successMessageContainer.innerHTML = '<p style="color: green;">Thank you</p>';
                        document.getElementById('storefrontForm').reset();

                        // Hide the success message after 3 seconds
                        setTimeout(function() {
                            successMessageContainer.innerHTML = '';
                        }, 3000);
                    } else {
                        // Handle other response scenarios if needed
                    }
                })
                .catch(error => {
                    // Handle errors
                });
            });
        })
        .catch(error => {
            console.error('Error loading storefront details:', error);
        });
});
