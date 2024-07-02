// your_app/static/your_app/js/custom.js
document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.querySelector('.add-row a');
    if (addButton) {
        addButton.addEventListener('click', function() {
            const inlineRows = document.querySelectorAll('.inline-related');
            inlineRows.forEach(function(row, index) {
                const descriptionField = row.querySelector('input[name$="-description"]');
                if (descriptionField) {
                    descriptionField.name = descriptionField.name.replace(/-description\d*$/, `-description${index + 1}`);
                }
            });
        });
    }
});
