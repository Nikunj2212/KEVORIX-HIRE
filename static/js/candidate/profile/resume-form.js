document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("id_resume");

    if (!input) return;

    input.addEventListener("change", function () {

        if (this.files.length > 0) {

            console.log("Selected:", this.files[0].name);

        }

    });

});