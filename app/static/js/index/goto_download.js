const downloadButton = document.querySelector('.goto-download-button');
const downloadCodeInput = document.querySelector('#download_code');

downloadButton.addEventListener('click', async (event) => {
    event.preventDefault();
    // alert(downloadCodeInput.value.trim());
    const download_code = downloadCodeInput.value.trim();
    
    window.location.href = `/download?download_code=${encodeURIComponent(download_code)}`;

});
