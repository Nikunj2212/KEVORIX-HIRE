const logoInput = document.getElementById("id_logo");
const coverInput = document.getElementById("id_cover_image");

const logoPreview = document.getElementById("logoPreview");
const coverPreview = document.getElementById("coverPreview");


function previewImage(input, preview){

    if(!input) return;

    input.addEventListener("change",function(){

        const file=this.files[0];

        if(file){

            preview.src=URL.createObjectURL(file);

            preview.style.display="block";

        }

    });

}


previewImage(logoInput,logoPreview);

previewImage(coverInput,coverPreview);