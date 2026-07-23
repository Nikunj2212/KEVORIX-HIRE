document.addEventListener("DOMContentLoaded", () => {

    const input = document.querySelector('input[type="file"]');

    if(!input) return;

    input.addEventListener("change", () => {

        if(input.files.length){

            console.log(input.files[0].name);

        }

    });

});