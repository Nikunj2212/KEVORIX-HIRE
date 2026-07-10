document.addEventListener("DOMContentLoaded", function () {

    const currentStudy = document.querySelector("#id_currently_studying");
    const endDate = document.querySelector("#id_end_date");

    function toggleEndDate() {

        if (!currentStudy || !endDate) return;

        if (currentStudy.checked) {

            endDate.value = "";
            endDate.disabled = true;

        } else {

            endDate.disabled = false;

        }

    }

    if (currentStudy) {

        currentStudy.addEventListener("change", toggleEndDate);

        toggleEndDate();

    }

});