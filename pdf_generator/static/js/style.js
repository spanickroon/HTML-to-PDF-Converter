function giveStyles() { 
    document.querySelectorAll('.form-group').forEach(form => {
        form.classList.add('convertation-form-group');
    });

    document.querySelectorAll('label').forEach(label => {
        label.classList.add('convertation-label');
    });

    document.querySelector('.form-control').classList.add('convertation-form-control');
    document.querySelector('.form-control').setAttribute('placeholder', 'https://example.com');
}

giveStyles();