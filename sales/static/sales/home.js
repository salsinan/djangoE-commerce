const reportBtn = document.getElementById('report-btn');
const img = document.getElementById('img');
const modalBody = document.getElementById('modal-body');

if (img) {
    reportBtn.classList.remove('not-visible');
    reportBtn.addEventListener('click', ()=>{
        img.setAttribute('class', 'w-100')
        modalBody.prepend(img)
    });
}