$(function() {
    var $loader = $('#loader');
    var page = 2;
    var isLoading = false;
    var sort = new URLSearchParams(window.location.search).get('sort') || 'date';
    var category = new URLSearchParams(window.location.search).get('category');

    $(window).scroll(function() {
        var endOfPage = $(document).height() - $(window).height() - $loader.height();
        
        if ($(window).scrollTop() >= endOfPage && !isLoading) {
            isLoading = true;
            $loader.show();

            var ajaxUrl = `/?page=${page}&sort=${sort}`;
            if (category) {
                ajaxUrl += `&category=${category}`;
            }

            $.ajax({
                url: ajaxUrl,
                type: 'GET',
                success: function(data) {
                    if (data.html) {
                        $('#posts-container').append(data.html);
                        page++;
                        isLoading = false;
                        $loader.hide();
                    } else {
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
