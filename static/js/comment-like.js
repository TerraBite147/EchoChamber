// Comment like logic
function likeComment(commentId) {
    console.log("Attempting to like/unlike comment with ID:", commentId);  // Log which comment is being liked/unliked

    $.ajax({
        url: '/like_comment/' + commentId + '/',
        type: 'get',
        success: function (response) {
            console.log("Liked/Unliked comment with ID:", commentId);  // Log successful like/unlike
            console.log("Server response:", response);  // Log the response from the server

            // Update the like count based on the response
            $("#comment-like-count-" + commentId).text(response.likes_count);
        },
        error: function (error) {
            console.log("Error liking/unliking comment with ID:", commentId);  // Log error with specific comment ID
            console.log("Error details:", error);  // Log the error details
        }
    });
}
