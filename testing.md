# Echo Chamber Testing

<center> 

![Mock Image](readme/mock-image.png)

</center>

Developer: [Logan Carlow](https://github.com/TerraBite147) <br>
[Live webpage](https://echo-chamber-ci-f4fdc2207726.herokuapp.com/)<br>
[Project Repository](https://github.com/TerraBite147/echo-chamber)<br>


## Table of Contents



## Code Validation

- HTML: Click link to see test results [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fecho-chamber-ci-f4fdc2207726.herokuapp.com%2F)
- CSS: Click link to see test results [W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fecho-chamber-ci-f4fdc2207726.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript: [JSHint](https://jshint.com/)
    - comment-like.js no errors warnings for usings $ for jQuery ignored
    - infinite-scroll.js no errors warnings for usings $ for jQuery ignored
    - post-like.js no errors warnings for usings $ for jQuery ignored
- Python: [CI Python Linter](https://pep8ci.herokuapp.com/)
    - forms.py no errors
    - models.py no errors
    - urls.py no errors
    - views.py no errors
    - test_views.py no errors

## Performance Testing

I conducted performance testing using google chrome light house. The results are as follows:

- index.html, _post_list.html , _post_list_partial.html, 
    - Performance: 99
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- about.html
    - Performance: 100
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- _profile.html
    - Performance: 100
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- _post_edit.html
    - Performance: 100
    - Accessibility: 91
    - Best Practices: 100
    - SEO: 100

- _post_detail.html , _post_interactions.html, comment_interactions.html
    - Performance: 100
    - Accessibility: 86
    - Best Practices: 100
    - SEO: 89



## Device compatibility

I tested the website on the following devices:

- Various Desktops
- Various Laptop
- iPhone 8
- Samsung Galaxy S20

The website was responsive on all devices and the functionality was consistent across all devices.

## Browser compatibility

I tested the website on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Safari

The website was responsive on all browsers and the functionality was consistent across all browsers.

## Automated Testing

I used Django's built-in testing framework to test the functionality of the website. The tests can be found in the tests.py file in the main app directory. The tests cover the following:

- Testing the views