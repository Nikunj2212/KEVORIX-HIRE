document.addEventListener("DOMContentLoaded", function () {

    const currentWorking = document.getElementById("id_currently_working");
    const endDate = document.getElementById("id_end_date");

    if (!currentWorking || !endDate) {
        return;
    }

    function toggleEndDate() {

        if (currentWorking.checked) {

            endDate.value = "";
            endDate.disabled = true;
            endDate.style.opacity = "0.6";

        } else {

            endDate.disabled = false;
            endDate.style.opacity = "1";

        }

    }

    currentWorking.addEventListener("change", toggleEndDate);

    toggleEndDate();

});