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
async function startCheckout() {
    const { error } = await stripe.redirectToCheckout({
        sessionId: s_id
    });

    if (error) {
        alert('Something went wrong with the payment, please try again.');
    }
}