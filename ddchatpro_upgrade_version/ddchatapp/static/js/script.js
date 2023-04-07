$(function() {
    var form = $('.chat-form');
    var messages = $('.messages');

    form.submit(function(event) {
        event.preventDefault();
        var messageInput = form.find('input[name="message"]');
        var message = messageInput.val();
        messageInput.val('');
        messages.append('<div class="message message-user">' + message + '</div>');
        scrollToBottom();

        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'message': message,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                messages.append('<div class="message message-bot">' + response.response + '</div>');
                scrollToBottom();
            },
            error: function(response) {
                console.log('Error:', response);
            }
        });
    });

    function scrollToBottom() {
        messages.scrollTop(messages[0].scrollHeight);
    }
});

