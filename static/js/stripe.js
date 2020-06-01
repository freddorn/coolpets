var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
const s_pub = returnStripePublishableKey();

// // All code below provided by https://stripe.com/docs/payments/cards/collecting/web

let stripe = Stripe(s_pub);
let elements = stripe.elements();

$('#submit-payment-btn').click(function () {
    startCheckout();
});

/**
 * Activates stripe v3 checkout page
 */
async function startCheckout() {
    const { error } = await stripe.redirectToCheckout({
        sessionId: s_id
    });

    if (error) {
        alert('Something went wrong with the payment, please try again.');
    }
}