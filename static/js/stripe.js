const s_pub = ('pk_test_Bg9povZBdi6gNH7dcYIoVmAm00lXpzmA8k');


// // All code below provided by https://stripe.com/docs/payments/cards/collecting/web

let stripe = Stripe(s_pub);
let elements = stripe.elements();

$('#submit-payment-btn').click(function () {
    startCheckout();
});

/**
 * Activates stripe v3 checkout page
 */
stripe.redirectToCheckout({
  // Make the id field from the Checkout Session creation API response
  // available to this file, so you can provide it as parameter here
  // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
  sessionId: 's_id'
}).then(function (result) {
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `result.error.message`.
});