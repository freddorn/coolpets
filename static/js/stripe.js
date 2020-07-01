var stripe = Stripe('pk_test_51GuVA5FOlkXgVXOiO3haRU5VThlZ8dffF7Y0FozO0CfcuHAmioAdWN94aD23lAty2ngGRWaXkQritCTQ2Gs90Buf001V26dYWz');

var elements = stripe.elements();
var cardElement = elements.create('card');
cardElement.mount('#card-element');
