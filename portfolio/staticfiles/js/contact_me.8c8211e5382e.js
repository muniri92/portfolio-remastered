$('.form-email').submit(function() {
        var $form       = $(this);
        var submitData  = $form.serialize();
        var $email      = $form.find('input[name="email"]');
        var $name       = $form.find('input[name="name"]');
        var $message    = $form.find('textarea[name="message"]');
        var $submit     = $form.find('input[name="submit"]');
        // var $dataStatus = $form.find('.data-status');

        $email.attr('disabled', 'disabled');
        $name.attr('disabled', 'disabled');
        $message.attr('disabled', 'disabled');
        $submit.attr('disabled', 'disabled');

        // $dataStatus.show().html('<div class="alert alert-info"><strong>Loading...</strong></div>');

        $.ajax({ // Send an offer process with AJAX
            type: 'POST',
            url: '/',
            data: submitData + '&action=add',
            dataType: 'html',
            success: function(msg){
                if (parseInt(msg, 0) !== 0) {
                    var msg_split = msg.split('|');
                    if (msg_split[0] === 'success') {
                        $email.val('').removeAttr('disabled');
                        $name.val('').removeAttr('disabled');
                        $message.val('').removeAttr('disabled');
                        $submit.removeAttr('disabled');
                        // $dataStatus.html(msg_split[1]).fadeIn();
                    } else {
                        $email.removeAttr('disabled');
                        $name.removeAttr('disabled');
                        $message.removeAttr('disabled');
                        $submit.removeAttr('disabled');
                        // $dataStatus.html(msg_split[1]).fadeIn();
                    }
                }
            }
        });

        return false;
    });



// $(function() {

//     $("input,textarea").jqBootstrapValidation({
//         preventSubmit: true,
//         submitError: function($form, event, errors) {
//             // additional error messages or events
//         },
//         submitSuccess: function($form, event) {
//             event.preventDefault(); // prevent default submit behaviour
//             // get values from FORM
//             var name = $("input#name").val();
//             var email = $("input#email").val();
//             var message = $("textarea#message").val();
//             var firstName = name; // For Success/Failure Message
//             var csrf = $("input#csrfmt")
//             // Check for white space in name for Success/Fail message
//             if (firstName.indexOf(' ') >= 0) {
//                 firstName = name.split(' ').slice(0, -1).join(' ');
//             }
//             $.ajax({
//                 url: "/hireme",
//                 type: "POST",
//                 data: {
//                     name: name,
//                     email: email,
//                     message: message,
//                     csrfmiddlewaretoken: csrf
//                 },
//                 cache: false,
//                 success: function() {
//                     // Success message
//                     $('#success').html("<div class='alert alert-success'>");
//                     $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
//                         .append("</button>");
//                     $('#success > .alert-success')
//                         .append("<strong>Your message has been sent. </strong>");
//                     $('#success > .alert-success')
//                         .append('</div>');

//                     //clear all fields
//                     $('#contactForm').trigger("reset");
//                 },
//                 error: function() {
//                     // Fail message
//                     $('#success').html("<div class='alert alert-danger'>");
//                     $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
//                         .append("</button>");
//                     $('#success > .alert-danger').append("<strong>Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!");
//                     $('#success > .alert-danger').append('</div>');
//                     //clear all fields
//                     $('#contactForm').trigger("reset");
//                 },
//             })
//         },
//         filter: function() {
//             return $(this).is(":visible");
//         },
//     });

//     $("a[data-toggle=\"tab\"]").click(function(e) {
//         e.preventDefault();
//         $(this).tab("show");
//     });
// });


// /*When clicking on Full hide fail/success boxes */
// $('#name').focus(function() {
//     $('#success').html('');
// });
