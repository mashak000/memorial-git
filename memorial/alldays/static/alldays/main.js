// defolt values
const parent = $("#modalimage").attr("src");

// main preloader
window.addEventListener('load', function () {
    const preloader = document.querySelector('#preloader');
    const btn = document.querySelector('#start');
    document.body.style.overflow = 'hidden'; // prevent scrolling through page while preloader is open
    btn.addEventListener('click', function () { 
        const fadeEffect = setInterval(() => {
            if (!preloader.style.opacity) {
            preloader.style.opacity = 0.5;
            }
            if (preloader.style.opacity > 0) {
            preloader.style.opacity -= 0.05;
            } else {
            clearInterval(fadeEffect);
            }
        }, 20);
        preloader.style.display = 'none';
        document.body.style.overflow = ''; // enable scrolling
    });
});

// make link open only on double click
function prevent(event){
    event.preventDefault();
}



// drag images freely
function dragElement() {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    let target = event.target;
    dragMouseDown();

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }
    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        target.style.top = (target.offsetTop - pos2) + "px";
        target.style.left = (target.offsetLeft - pos1) + "px";
    }
    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
    }
}


// modal handle
const closeBtn = document.querySelector('[data-close]');

closeBtn.addEventListener('click', () => {
    const modal = closeBtn.closest('.mmodal')
    closeModal(modal);
})

overlay.addEventListener('click', () =>{
    const modal = document.querySelector('.mmodal.active');
    closeModal(modal);
})

function openModal(modal) {
    if (modal === null) return 
    modal.classList.add('active');
    overlay.classList.add('active');
}

function closeModal(modal) {
    if (modal === null) return 
    modal.classList.remove('active');
    overlay.classList.remove('active');
    infoDiv.classList.remove('active');
    infoBtn.classList.remove('active');
}

// info slider
const infoBtn = document.querySelector('.info-trigger');
const infoDiv = document.querySelector('.info');

infoBtn.addEventListener('click', () => {
    infoDiv.classList.toggle('active');
    infoBtn.classList.toggle('active');
})