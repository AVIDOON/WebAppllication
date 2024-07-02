function setToday(fieldId) {
    var today = new Date().toISOString().split('T')[0];
    document.getElementById(fieldId).value = today;
}
function validateForm()
{
    var startDate = document.getElementById(startDate).value;
    var endDate = document.getElementById(endDate).value;
    if(startDate > endDate)
    {
        alert("Please enter a valid date");
    }
}
    // Make AJAX request to Flask backend
    $(document).ready(function() {
        $('#calculationForm').on('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally
            $.ajax({
                type: 'POST',
                url: '/calculate',
                data: $(this).serialize(),
                success: function(response) {
                    // Redirect to details page or display details inline
                    window.location.href = '/details'; // Redirect to details page
                    // Alternatively, display details inline
                    // $('#amountContainer').text('Calculated Amount: ' + response.amount);
                },
                error: function(error) {
                    console.log('Error:', error);
                }
            });
        });
    });
