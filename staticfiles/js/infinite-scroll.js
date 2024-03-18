$(window).scroll(function() {
    // Trigger the data load when the user is 100px from the bottom of the document
    if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
        if (!window.isLoadingPosts && window.hasMorePosts) {
            window.isLoadingPosts = true;
            var nextPage = parseInt($('#page-number').val()) + 1;  // Increment the page number

            // Show the loader
            $('#loader').show();

            $.ajax({
                url: '/', 
                type: 'GET',
                data: {
                    'page': nextPage,
                    'x-requested-with': 'XMLHttpRequest',
                },
                success: function(data) {
                    // Hide the loader
                    $('#loader').hide();

                    if (data.html) {
                        $('#posts-container').append(data.html);  // Append the new posts
                        $('#page-number').val(nextPage);  // Update the page number
                        window.isLoadingPosts = false;
                        window.hasMorePosts = data.has_next;  // Check if there are more posts to load
                    }
                    if (!data.has_next) {
                        // Optionally, hide or remove the loader if there are no more posts
                        $('#loader').hide();
                    }
                },
                error: function(xhr, status, error) {
                    // Handle errors
                    console.error("Error while loading posts: ", error);
                    // Optionally, show an error message or handle the error gracefully
                    $('#loader').hide();
                }
            });
        }
    }
});

window.isLoadingPosts = false;
window.hasMorePosts = true;