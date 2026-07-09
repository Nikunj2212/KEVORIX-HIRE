const greeting = document.getElementById("greeting");

if(greeting){

    const hour = new Date().getHours();

    if(hour >= 6 && hour < 12){

        greeting.textContent="Good Morning ☀️";

    }

    else if(hour >=12 && hour <17){

        greeting.textContent="Good Afternoon 🌤️";

    }

    else if(hour >=17 && hour <21){

        greeting.textContent="Good Evening 🌇";

    }

    else{

        greeting.textContent="Good Night 🌙";

    }

}

// =====================================
// THEME TOGGLE
// =====================================

const themeToggle = document.getElementById("theme-toggle");

const html = document.documentElement;

// Load Saved Theme
const savedTheme = localStorage.getItem("theme") || "light";

html.setAttribute("data-theme", savedTheme);

// Set Icon
const updateThemeIcon = () => {

    if(html.getAttribute("data-theme") === "dark"){

        themeToggle.innerHTML =
        '<i class="bi bi-sun-fill"></i>';

    }

    else{

        themeToggle.innerHTML =
        '<i class="bi bi-moon-stars-fill"></i>';

    }

};

updateThemeIcon();

// Toggle Theme

themeToggle.addEventListener("click",()=>{

    const currentTheme =
    html.getAttribute("data-theme");

    const newTheme =
    currentTheme === "light"
    ? "dark"
    : "light";

    html.setAttribute(
        "data-theme",
        newTheme
    );

    localStorage.setItem(
        "theme",
        newTheme
    );

    updateThemeIcon();

});
// =====================================
// NOTIFICATION DROPDOWN
// =====================================

const notificationBtn =
document.getElementById("notification-btn");

const notificationDropdown =
document.getElementById("notification-dropdown");

if(notificationBtn){

    notificationBtn.addEventListener("click",(e)=>{

        e.stopPropagation();

        notificationDropdown.classList.toggle("show");

    });

    document.addEventListener("click",(e)=>{

        if(!notificationDropdown.contains(e.target)){

            notificationDropdown.classList.remove("show");

        }

    });

}
// =====================================
// PROFILE DROPDOWN
// =====================================

const profileBtn = document.getElementById("profile-btn");

const profileDropdown = document.getElementById("profile-dropdown");

if (profileBtn && profileDropdown) {

    profileBtn.addEventListener("click", function (e) {

        e.stopPropagation();

        profileDropdown.classList.toggle("show");

    });

    document.addEventListener("click", function (e) {

        if (!profileDropdown.contains(e.target) &&
            !profileBtn.contains(e.target)) {

            profileDropdown.classList.remove("show");

        }

    });

}