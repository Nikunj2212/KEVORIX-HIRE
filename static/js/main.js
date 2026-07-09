// =====================================
// NAVBAR SCROLL EFFECT
// =====================================

const navbar = document.querySelector(".navbar");

if (navbar) {

    window.addEventListener("scroll", () => {

        if (window.scrollY > 40) {

            navbar.classList.add("navbar-scrolled");

        }

        else {

            navbar.classList.remove("navbar-scrolled");

        }

    });

}// =====================================
// COUNTER ANIMATION
// =====================================

const counters = document.querySelectorAll(".counter");

const counterObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            const counter = entry.target;
            const target = +counter.dataset.target;

            let current = 0;

            const increment = target / 150;

            const updateCounter = () => {

                current += increment;

                if (current < target) {

                    if (target >= 1000) {

                        counter.innerText = Math.floor(current).toLocaleString();

                    } else {

                        counter.innerText = Math.floor(current);

                    }

                    requestAnimationFrame(updateCounter);

                }

                else {

                    if (target === 50000) {

                        counter.innerText = "50K+";

                    }

                    else if (target === 12000) {

                        counter.innerText = "12K+";

                    }

                    else if (target === 800) {

                        counter.innerText = "800+";

                    }

                    else if (target === 96) {

                        counter.innerText = "96%";

                    }

                }

            };

            updateCounter();

            counterObserver.unobserve(counter);

        }

    });

}, {

    threshold: 0.5

});

counters.forEach(counter => {

    counterObserver.observe(counter);

});
//=====================================
// PREMIUM REVEAL
//=====================================

const revealElements = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

},{
    threshold:.18
});

revealElements.forEach(item=>{

    revealObserver.observe(item);

});
//=====================================
// FAQ ACCORDION
//=====================================

const faqItems = document.querySelectorAll(".faq-item");

// Initial State
faqItems.forEach(item => {

    const icon = item.querySelector(".faq-icon");

    if (item.classList.contains("active")) {

        icon.textContent = "−";

    } else {

        item.classList.remove("active");
        icon.textContent = "+";

    }

});

faqItems.forEach(item => {

    const question = item.querySelector(".faq-question");

    if (!question) return;

    question.addEventListener("click", () => {

        const isActive = item.classList.contains("active");

        faqItems.forEach(faq => {

            faq.classList.remove("active");

            const icon = faq.querySelector(".faq-icon");

            if (icon) {

                icon.textContent = "+";

            }

        });

        if (!isActive) {

            item.classList.add("active");

            const icon = item.querySelector(".faq-icon");

            if (icon) {

                icon.textContent = "−";

            }

        }

    });

});//=====================================
// SCROLL PROGRESS BAR
//=====================================

const progressBar = document.querySelector(".scroll-progress-bar");

window.addEventListener("scroll", () => {

    const scrollTop = window.scrollY;

    const documentHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;

    const progress = (scrollTop / documentHeight) * 100;

    if(progressBar){

    progressBar.style.width = progress + "%";

    }

});
//=====================================
// SMOOTH SCROLL + ACTIVE NAVBAR
//=====================================

const navLinks = document.querySelectorAll(".nav-menu a");
const sections = document.querySelectorAll("section[id]");

// Smooth Scroll
navLinks.forEach(link => {

    link.addEventListener("click", function(e){

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if(target){

            window.scrollTo({

                top: target.offsetTop - 90,

                behavior: "smooth"

            });

        }

    });

});

// Active Menu While Scrolling
window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 120;

        const sectionHeight = section.offsetHeight;

        if(window.scrollY >= sectionTop){

            current = section.getAttribute("id");

        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if(link.getAttribute("href") === "#" + current){

            link.classList.add("active");

        }

    });

});