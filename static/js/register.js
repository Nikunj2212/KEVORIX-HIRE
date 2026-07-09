
// =====================================
// PASSWORD SHOW / HIDE
// =====================================

const passwordToggles = document.querySelectorAll(".password-toggle");

passwordToggles.forEach(toggle => {

    toggle.addEventListener("click", () => {

        const target = document.getElementById(toggle.dataset.target);

        if (!target) return;

        if (target.type === "password") {

            target.type = "text";
            toggle.textContent = "🙈";

        } else {

            target.type = "password";
            toggle.textContent = "👁";

        }

    });

});


// =====================================
// PASSWORD STRENGTH
// =====================================
// =====================================
// PASSWORD STRENGTH
// =====================================

const passwordInput = document.getElementById("password");

const strengthFill = document.getElementById("strength-fill");

const strengthText = document.getElementById("strength-text");

if (passwordInput && strengthFill && strengthText) {

    passwordInput.addEventListener("input", () => {

        const password = passwordInput.value;

        let score = 0;

        if (password.length >= 8) score++;

        if (/[A-Z]/.test(password)) score++;

        if (/[a-z]/.test(password)) score++;

        if (/[0-9]/.test(password)) score++;

        if (/[^A-Za-z0-9]/.test(password)) score++;

        if (password.length === 0) {

            strengthFill.style.width = "0%";

            strengthText.textContent = "Password Strength";

            return;

        }

        if (score <= 2) {

            strengthFill.style.width = "33%";

            strengthFill.style.background = "#ef4444";

            strengthText.textContent = "Weak Password";

            strengthText.style.color = "#ef4444";

        }

        else if (score <= 4) {

            strengthFill.style.width = "66%";

            strengthFill.style.background = "#f59e0b";

            strengthText.textContent = "Medium Password";

            strengthText.style.color = "#f59e0b";

        }

        else {

            strengthFill.style.width = "100%";

            strengthFill.style.background = "#10b981";

            strengthText.textContent = "Strong Password";

            strengthText.style.color = "#10b981";

        }

    });

}

// =====================================
// CONFIRM PASSWORD MATCH
// =====================================

const confirmPassword = document.getElementById("confirmPassword");

if (passwordInput && confirmPassword) {

    const matchText = document.createElement("small");

    matchText.className = "password-match";

    confirmPassword.parentElement.after(matchText);

    const checkMatch = () => {

        if (confirmPassword.value === "") {

            matchText.textContent = "";

            return;

        }

        if (passwordInput.value === confirmPassword.value) {

            matchText.textContent = "Passwords Match";
            matchText.style.color = "#10b981";

        } else {

            matchText.textContent = "Passwords Do Not Match";
            matchText.style.color = "#ef4444";

        }

    };

    passwordInput.addEventListener("input", checkMatch);

    confirmPassword.addEventListener("input", checkMatch);

}