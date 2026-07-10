document.addEventListener("DOMContentLoaded", function () {

    const doesNotExpire = document.getElementById("id_does_not_expire");
    const expiryDate = document.getElementById("id_expiry_date");

    if (!doesNotExpire || !expiryDate) {
        return;
    }

    function toggleExpiryDate() {

        if (doesNotExpire.checked) {

            expiryDate.value = "";
            expiryDate.disabled = true;
            expiryDate.style.opacity = "0.6";

        } else {

            expiryDate.disabled = false;
            expiryDate.style.opacity = "1";

        }

    }

    doesNotExpire.addEventListener("change", toggleExpiryDate);

    toggleExpiryDate();

});