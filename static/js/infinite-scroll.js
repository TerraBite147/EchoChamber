$(function() {
    var $loader = $('#loader'); // The loader element
    var page = 2; // Start from the second page
    var isLoading = false; // To prevent multiple loads
    var sort = new URLSearchParams(window.location.search).get('sort') || 'date'; // Get the current sort parameter or default to 'date'

    // Detect when the user scrolls near the bottom of the content
    $(window).scroll(function() {
        var endOfPage = $(document).height() - $(window).height() - $loader.height();
        
        if ($(window).scrollTop() >= endOfPage && !isLoading) {
            isLoading = true;
            $loader.show();

            $.ajax({
                url: '/?page=' + page + '&sort=' + sort,  // Include the sort parameter
                type: 'GET',
                success: function(data) {
                    // Append the new posts to the content
                    if (data.html) {
                        $('#posts-container').append(data.html);
                        page++;
                        isLoading = false;
                        $loader.hide();
                    } else {
                        // No more posts to load
                        $loader.hide();
                    }
                },
                error: function() {
                    isLoading = false;
                    $loader.hide();
                    console.log('No more pages to load.');
                }
            });
        }
    });
});
