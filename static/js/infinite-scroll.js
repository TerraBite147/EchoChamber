$(function() {
    var $loader = $('#loader'); // The loader element
    var page = 2; // Start from the second page
    var isLoading = false; // To prevent multiple loads

    // Detect when the user scrolls near the bottom of the content
    $(window).scroll(function() {
        var endOfPage = $(document).height() - $(window).height() - $loader.height();
        
        if ($(window).scrollTop() >= endOfPage && !isLoading) {
            isLoading = true;
            $loader.show();

            $.ajax({
                url: '/?page=' + page,
                type: 'GET',
                success: function(data) {
                    // Append the new posts to the content
                    if (data.html) {
                        $('.row.justify-content-center').last().append(data.html);
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
