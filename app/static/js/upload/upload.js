const button = document.getElementById('upload-button');

async function uploadFile(event) {
    event.preventDefault();

    const fileInput = document.getElementById('file');

    const response = await fetch('/upload', {
            method: 'POST',
        body: new FormData(fileInput.form)
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message);
    } else {
        alert(result.error);
    }

    fileInput.form.reset();
}

button.addEventListener('click', uploadFile);