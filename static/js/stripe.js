let stripe = Stripe('pk_test_51GuVA5FOlkXgVXOiO3haRU5VThlZ8dffF7Y0FozO0CfcuHAmioAdWN94aD23lAty2ngGRWaXkQritCTQ2Gs90Buf001V26dYWz');
let elements = stripe.elements();

let style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');
// Handle real-time validation errors from the card Element.
card.addEventListener('change', function (event) {
    let displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});
// Handle form submission.
let form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
    event.preventDefault();
    stripe.createToken(card).then(function (result) {
        if (result.error) {
            // Inform the user if there was an error.
            let errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // Send the token to your server.
            stripeTokenHandler(result.token);
        }
    });
});
// Submit the form with the token ID.
function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    let form = document.getElementById('payment-form');
    let hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);
    // Submit the form
    form.submit();
}