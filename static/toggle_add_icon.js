let addIcons = document.querySelectorAll('.add-icon');

addIcons.forEach(addIcon => {
    addIcon.addEventListener('mouseover', (e) => {
        e.target.setAttribute('src', hoveredSrc);
    });

    addIcon.addEventListener('mouseleave', (e) => {
        e.target.setAttribute('src', unhoveredSrc);
    });
});