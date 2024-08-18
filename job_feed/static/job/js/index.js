window.addEventListener('DOMContentLoaded', ()=> {
    var menuBtn = document.querySelector('#menubutton')
    var dropdown = document.querySelector('#dropdown')
    
    menuBtn.addEventListener('click', () => {
        /* if(dropdown.classList.contains('hidden')){
            dropdown.classList.remove('hidden');
            dropdown.classList.add('flex');
        }else{
            dropdown.classList.remove('flex')
            dropdown.classList.add('hidden')
        } */
        dropdown.classList.toggle('hidden')
        dropdown.classList.toggle('flex')
    })
    
})

let defaultTransform = 0;
function goNext() {
    defaultTransform = defaultTransform - 500;
    var slider = document.getElementById("slider");
    if (Math.abs(defaultTransform) >= slider.scrollWidth / 1.7) defaultTransform = 0;
    slider.style.transform = "translateX(" + defaultTransform + "px)";
}
next.addEventListener("click", goNext);
function goPrev() {
    var slider = document.getElementById("slider");
    if (Math.abs(defaultTransform) === 0) defaultTransform = 0;
    else defaultTransform = defaultTransform + 500;
    slider.style.transform = "translateX(" + defaultTransform + "px)";
}
prev.addEventListener("click", goPrev);


/////
