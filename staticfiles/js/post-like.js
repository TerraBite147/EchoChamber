// post like logic
function likePost(postSlug) {
    $.ajax({
        url: '/post/' + postSlug + '/like',
        type: 'get',
        success: function(response) {
            // Update the like count based on the response
            $("#like-count-" + postSlug).text(response.likes_count);
        }
    });
}