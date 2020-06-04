const s_pub = ('STRIPE_PUBLISHABLE');


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
        sessionId: Data.sessionId,
    });

    if (error) {
        alert('Something went wrong with the payment, please try again.');
    }
}