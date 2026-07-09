document.querySelectorAll(".password-toggle").forEach(toggle => {

    toggle.addEventListener("click", () => {

        const input = document.getElementById(toggle.dataset.target);

        if (input.type === "password") {

            input.type = "text";
            toggle.textContent = "🙈";

        } else {

            input.type = "password";
            toggle.textContent = "👁";

        }

    });

});