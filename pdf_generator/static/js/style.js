function giveStyles() { 
    document.querySelectorAll('.form-group').forEach(form => {
        form.classList.add('convertation-form-group');
    });

    document.querySelectorAll('label').forEach(label => {
        label.classList.add('convertation-label');
    });

    document.getElementsByName('url_upload')[0].classList.add('convertation-form-control');
    document.getElementsByName('url_upload')[0].setAttribute('placeholder', 'https://example.com');

    document.getElementsByName('email_upload')[0].classList.add('convertation-form-control');
    document.getElementsByName('email_upload')[0].setAttribute('placeholder', 'example@email.com');

    document.getElementsByName('email_upload')[0].setAttribute('required', true);
}

giveStyles();