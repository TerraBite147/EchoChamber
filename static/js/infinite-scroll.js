$(document).ready(function() {
  let pageNumber = 2;
  let isLoading = false;
  let $loader = $('#loader');
  let $postContainer = $('.row').first(); // Assuming the first row is where posts are appended.

  function nearBottomOfPage() {
      return $(window).scrollTop() > $(document).height() - $(window).height() - 100;
  }

  $(window).scroll(function() {
      if (nearBottomOfPage() && !isLoading) {
          isLoading = true;
          $loader.show();

          $.ajax({
              url: `?page=${pageNumber}`, // Update this URL to the endpoint where you fetch more posts.
              type: 'GET',
              success: function(data) {
                  // Append the new posts to the post container.
                  $postContainer.append(data);
                  pageNumber++;
                  isLoading = false;
                  $loader.hide();
              },
              error: function() {
                  isLoading = false;
                  $loader.hide();
                  // Handle errors (e.g., show a message to the user).
              }
          });
      }
  });
});
