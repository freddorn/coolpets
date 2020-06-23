let stripe = Stripe('pk_test_51GuVA5FOlkXgVXOiO3haRU5VThlZ8dffF7Y0FozO0CfcuHAmioAdWN94aD23lAty2ngGRWaXkQritCTQ2Gs90Buf001V26dYWz');
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