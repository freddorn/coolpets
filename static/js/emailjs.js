let sendMail = function (form) {


    emailjs.send("gmail", "coolpets", {

        "from_name": form.name.value,

        "from_email": form.emailaddress.value,

        "message": form.enquiry.value

    })

        .then(

            function (response) {

                console.log("SUCCES", response);

                alert("Your message has been sent successfully");

                document.getElementById('form').reset();

            },

            function (error) {

                console.log("FAILED", error);

                alert("Message was not sent");

                document.getElementById('form').reset();

            });

    return false;

};





async function init() {

    await sendMail();

}



init();