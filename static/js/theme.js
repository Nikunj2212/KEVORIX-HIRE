const themeToggle = document.querySelector(".theme-toggle");

const html = document.documentElement;

if (!localStorage.getItem("theme")) {

    localStorage.setItem("theme", "dark");

}

const savedTheme = localStorage.getItem("theme");

html.setAttribute("data-theme", savedTheme);

if (themeToggle) {

    themeToggle.textContent =
        savedTheme === "dark" ? "🌙" : "☀️";

    themeToggle.addEventListener("click", () => {

        const currentTheme = html.getAttribute("data-theme");

        if (currentTheme === "dark") {

            html.setAttribute("data-theme", "light");

            localStorage.setItem("theme", "light");

            themeToggle.textContent = "☀️";

        }

        else {

            html.setAttribute("data-theme", "dark");

            localStorage.setItem("theme", "dark");

            themeToggle.textContent = "🌙";

        }

    });

}