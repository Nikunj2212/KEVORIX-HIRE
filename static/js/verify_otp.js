
const boxes = document.querySelectorAll(".otp-box");
const hidden = document.getElementById("otp");

boxes.forEach((box, index) => {

    box.addEventListener("input", () => {

        box.value = box.value.replace(/[^0-9]/g, "");

        if (box.value && index < boxes.length - 1) {

            boxes[index + 1].focus();

        }

        hidden.value = [...boxes].map(b => b.value).join("");

    });

    box.addEventListener("keydown", (e) => {

        if (
            e.key === "Backspace" &&
            !box.value &&
            index > 0
        ) {

            boxes[index - 1].focus();

        }

    });

});
const timer = document.getElementById("otp-timer");

const resend = document.getElementById("resend-link");

if (timer && resend) {

    let seconds = 300;

    const interval = setInterval(() => {

        let min = Math.floor(seconds / 60);

        let sec = seconds % 60;

        timer.innerText =
            `${String(min).padStart(2,"0")}:${String(sec).padStart(2,"0")}`;

        if (seconds <= 0) {

            clearInterval(interval);

            timer.innerText = "Expired";

            resend.style.pointerEvents = "auto";

            resend.style.opacity = "1";

        }

        seconds--;

    }, 1000);

}