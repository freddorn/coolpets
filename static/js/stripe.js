console.log("Sanity check!");

const s_pub = ('STRIPE_PUBLISHABLE');



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
        alert('Something went wrong with your payment, please try again.');
    }
}