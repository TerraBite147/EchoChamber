# Echo Chamber
Echo Chamber is a vibrant community-driven platform, where users can freely express their thoughts, share insightful posts, and engage in lively discussions. It's a place where text-based communication takes center stage, allowing members to delve deep into topics that matter to them.


<center> 

![Mock Image](readme/mock-image.png)

</center>

Developer: [Logan Carlow](https://github.com/TerraBite147) <br>
[Live webpage](https://echo-chamber-ci-f4fdc2207726.herokuapp.com/)<br>
[Project Repository](https://github.com/TerraBite147/echo-chamber)<br>


![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)

# Table of Contents
1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements Expectations](#user-requirements-expectations)
    - [User Stories](#user-stories)
3. [Database Schema](#database-schema)
    - [Database Schema Overview](#database-schema-overview)
4. [Visual Design](#visual-design)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Layout](#layout)
    - [Before users log in](#before-users-log-in)   




# Project Goals

### User Goals:
- Share Ideas: Users want to share their thoughts, opinions, and ideas with like-minded individuals.
- Discover Content: Users aim to discover new and interesting content posted by others within the community.
- Engage with Community: Users seek opportunities to engage with other members through comments, likes, and discussions.
- Build Relationships: Users may want to connect with others who share similar interests or viewpoints.
- Stay Informed: Users want to stay informed about trending topics, discussions, and community events.
### Site Owner Goals:
- User Engagement: The site owner aims to foster a vibrant and active community where users engage with each other's content regularly.
- User Retention: The site owner wants to encourage users to return to the platform frequently by providing valuable content and a positive user experience.
- Community Growth: The site owner seeks to attract new users and grow the community over time by promoting the platform and expanding its reach.
- Feedback Collection: The site owner aims to collect feedback from users to understand their needs, preferences, and suggestions for improving the platform.

# User Experience

### Target Audience:
- Community Enthusiasts: Individuals who are passionate about participating in online communities, sharing ideas, and engaging in discussions.
- Knowledge Seekers: Users who are curious and eager to explore diverse perspectives, learn new things, and expand their knowledge.
- Opinion Leaders: People who enjoy expressing their opinions, insights, and viewpoints on various topics and influencing others in the community.
- Social Networkers: Individuals who value social connections and enjoy interacting with like-minded individuals who share their interests and values.
- Content Creators: Users who produce original content, such as articles, blog posts, and seek a platform to showcase their creations to a receptive audience.
### User Requirements Expectations:
- Intuitive User Interface: Users expect a clean, user-friendly interface that is easy to navigate, allowing them to browse content, interact with others, and access features effortlessly.
- Content Discovery: Users require robust content discovery features, categories, tags, to help them find relevant and interesting content quickly.
- Engagement Tools: Users expect features for engagement, such as commenting and liking, to facilitate interaction and community building.
- Responsive Design: Users access the platform from various devices, so they expect a responsive design that adapts seamlessly to different screen sizes and resolutions for a consistent experience.
- Community Guidelines: Users value clear community guidelines and moderation policies to ensure a safe, respectful, and inclusive environment conducive to open dialogue and constructive discourse.
- Feedback Mechanism: Users appreciate the ability to provide feedback, report issues, and suggest improvements to help shape the platform and enhance their experience over time.

By understanding the target audience and their requirements and expectations, the Echo Chamber platform can be designed and developed to meet their needs effectively, fostering a positive and engaging user experience.

## User Stories
User stories and tasks were put into Three 'epics' to establish a well-defined work structure. You can access the details of these milestones by clicking [here](https://github.com/TerraBite147/echo-chamber/milestones), which will take you to the milestone overview.

### Epic 1: User Authentication
This epic focuses on user account management, including registration, login/logout.

- [User Story: Account Creation (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/2)
- [Login from Landing Page (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/16)
- [Password Reset (WON'T HAVE)](https://github.com/TerraBite147/echo-chamber/issues/17)
- [Profile Page (SHOULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/15)

### Epic 2: Post Interaction
This epic focuses on the interaction between users and posts, including creating, editing, and deleting posts as well as liking and commenting on posts.

- [User Story: View list of Posts (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/12)
- [User Story: View Post Details (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/14)
- [User Story: Create Post (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/3)
- [User Story: Edit Post (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/18)
- [User Story: Delete Post (SHOULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/7)
- [User Story: Like Post (SHOULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/5)
- [User Story: Comment on Post (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/4)
- [User Story: Edit Comment (COULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/8)
- [User Story: Delete Comment (COULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/19)
- [User Story: Like Comment (COULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/20)
- [User Story: User Story: Infinite Scrolling for Posts (SHOULD HAVE)](https://github.com/TerraBite147/echo-chamber/issues/13)

### Epic 3: Admin Panel
This epic focuses on the admin panel, including user management, post management, and comment management.

- [User Story: Admin Panel (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/21)
- [User Story: User Management (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/22)
- [User Story: Post Management (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/23)
- [User Story: Comment Management (MUST HAVE)](https://github.com/TerraBite147/echo-chamber/issues/24)

## Database Schema

When creating the database schema, I used dbdiagram.io to create a visual representation of the database schema. You can view the database schema below.

![Database Schema](readme/database.png)
## Database Schema Overview


This section provides an overview of the database schema used in the application, detailing the tables and their relationships.

### Tables

#### User
- **id**: Primary Key, Integer
- **username**: String
- **email**: String
- Additional fields as defined by Django's built-in User model.

#### Category
- **id**: Primary Key, Integer
- **name**: String, Unique
- **description**: Text

#### Post
- **id**: Primary Key, Integer
- **title**: String
- **slug**: String, Unique
- **author_id**: Foreign Key to User
- **content**: Text
- **posted_at**: DateTime
- **category_id**: Foreign Key to Category (nullable)
- **status**: Integer (0 for Draft, 1 for Published)
- **excerpt**: Text
- **updated_on**: DateTime

#### PostLike
- **id**: Primary Key, Integer
- **post_id**: Foreign Key to Post
- **user_id**: Foreign Key to User
- **created_at**: DateTime
- Unique constraint on (`post_id`, `user_id`)

#### Comment
- **id**: Primary Key, Integer
- **post_id**: Foreign Key to Post
- **author_id**: Foreign Key to User
- **content**: Text
- **created_at**: DateTime

#### CommentLike
- **id**: Primary Key, Integer
- **comment_id**: Foreign Key to Comment
- **user_id**: Foreign Key to User
- **created_at**: DateTime
- Unique constraint on (`comment_id`, `user_id`)

#### Notification
- **id**: Primary Key, Integer
- **user_id**: Foreign Key to User
- **message**: String
- **is_read**: Boolean
- **created_at**: DateTime
- **target_url**: String, Nullable

### Relationships

- A `Post` is associated with one `User` (author) and optionally one `Category`.
- A `PostLike` associates a `User` with a `Post` they like.
- A `Comment` is associated with one `User` (author) and one `Post`.
- A `CommentLike` associates a `User` with a `Comment` they like.
- A `Notification` is associated with one `User`.

This schema effectively organizes the data for Echo Chamber, ensuring robust data management and efficient data retrieval for various features like posts, comments, likes, and notifications.


## Visual Design

The Visual Design section provides an overview of the design elements used in the application, including color scheme, typography, and layout.

### Color Scheme

The colour scheme for Echo Chamber is sleek and modern, with a combination of dark and light shades to create a visually appealing interface. The primary colors used in the design are as 

<center>

![Colour Scheme](readme/colour-scheme.png)

</center>

### Fonts

The typography for Echo Chamber is clean and easy to read, with a focus on readability and legibility. The primary fonts used in the design are Roboto and Lato, which are widely used for web design due to their versatility and readability.

### Layout

The layout of Echo Chamber is designed to be user-friendly and intuitive, with a clean and organized structure that guides users through the platform seamlessly. The design features a responsive layout that adapts to different screen sizes and resolutions, ensuring a consistent user experience across devices.

### **Before users log in**
They are greeted with a landing page that takes them straight to a list of posts. Once logged in, users can access their profile page, create new posts, view post details, like posts, comment on posts, and interact with other users through the platform's features.

- **Header**: The header features the site logo, navigation menu, and login and registration links.

![Header](readme/header.png)

- **Landing Page**: The landing page features a list of posts, allowing users to browse and discover content easily with options to filter by category and sort by date or popularity.

![Landing Page](readme/landing.png)

- **About Page**: The about page provides information about the platform, and community guidelines, fostering a positive and inclusive environment for users.

![About Page](readme/about.png)

- **Login Page**: The login page allows users to log in to their account securely, providing a smooth and hassle-free login experience.

![Login](readme/login.png)

- **Sign up Page**: The Sign Up page enables new users to create an account quickly and easily, with fields for username, email, and password.

![Sign Up](readme/sign-up.png)

- **Post Details Page**: The post details page displays the full content of a post, along with comments, likes, liking or commenting will redirect the user to the log in page.

![Post Details](readme/post-details.png)

### **After users log in**
They can access additional features such as creating new posts, liking posts, commenting on posts, and viewing notifications. Users can also access their profile page to view their posts, comments, draft posts, and notifications.

- **header**: The header displays the site logo, navigation menu, user profile button, and notification icon when a new notification is available.

![header-login](/readme/header-login.png)

- **Profile Page**: The profile page showcases the user's posts, comments, draft posts and notifications. Users can expand the dropdowns to view details on the post, comments and edit draft posts.

![Profile Page](readme/profile.png)

- **Create Post Page**: The create post page allows users to compose new posts with a title, content, category, and excerpt, providing a seamless post creation experience. 

- **Edit Post Page**: The edit post page enables users to edit their existing posts, with fields for title, content, category, and excerpt, allowing users to update their posts easily.

-  **Post Details Page**: The post details page displays the full content of a post, along with comments, likes, and options to like or comment on the post and options to edit or delete the post if the user is the author.

![Post Details](readme/post-details-login.png)

- **Sign out**: The sign-out button allows users to log out of their account securely, ensuring data privacy and account security.

![Sign Out](readme/sign-out.png)

By providing a seamless user experience with intuitive navigation, clear visual hierarchy, and engaging design elements, Echo Chamber aims to create a vibrant and interactive platform where users can freely express their thoughts, share ideas, and engage with the community effectively.

## Technologies Used

### Languages
- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and Libraries
- Django
- Bootstrap
- Crispy Forms

### Database
- PostgreSQL

### Tools and Platforms
- Git
- GitHub
- Gitpod
- Heroku
- dbdiagram.io
- fontawesome
- Google Fonts
- ChatGPT

### Libraries and Packages

- asgiref: Synchronous and asynchronous Python compatibility library, used as a foundation for ASGI applications like Django.
- click: A Python package for creating beautiful command line interfaces in a composable way.
- crispy-bootstrap5: Django utility that lets you easily build Bootstrap 5 forms with Django Crispy Forms.
- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- django-crispy-forms: A Django app that provides a DRY way to define forms' layout and rendering with Bootstrap styling.
- django-summernote: A Django app that adds the Summernote WYSIWYG editor to text fields.
- gunicorn: A Python WSGI HTTP Server for UNIX, designed to serve fast clients or large amounts of requests.
- oauthlib: A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.
- pathspec: Utility library for pattern matching of file paths. So for example, Git's .gitignore.
- psycopg2: The most popular PostgreSQL adapter for Python, allowing Python code to interact with PostgreSQL databases.
- python3-openid: A Python3 port of the python-openid library for OpenID support.
- requests-oauthlib: An OAuth library for Python's Requests, providing easy access to protected resources.
- sqlparse: A non-validating SQL parser for Python, providing parsing for SQL statements.
- whitenoise: Allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3, or any other external service.


## Methodology

Echo Chamber was developed using the Agile methodology, which emphasizes iterative development, collaboration, and flexibility in responding to change. The project was divided into sprints, with each sprint focusing on specific features and user stories. The development process involved continuous testing, and refinement to ensure that the platform meets requirements effectively.

### Agile Development Process

To streamline the development process, GitHub Issues were used to track tasks, user stories, and bugs, providing a centralized location for managing project-related activities. Each issue was assigned to a specific milestone, allowing for better organization and tracking of progress.

### User Stories and Epics

User stories were used to define the requirements and expectations of users, guiding the development process and ensuring that the platform meets user needs effectively. User stories were grouped into epics based on common themes and features, allowing for better planning and prioritization of tasks.

### Iterative Development

The development process was iterative, with regular testing to identify and address issues early in the development cycle. Continuous integration and deployment (CI/CD) were used to automate testing and deployment processes, ensuring that changes were deployed quickly and efficiently.

We utilized MoSCoW prioritization to categorize user stories into Must Have, Should Have, Could Have, and Won't Have categories, allowing for better prioritization and focus on essential features.


## Features

### User Authentication

- **Account Creation**: Users can create an account by providing a username, email, and password.
- **Login**: Users can log in to their account securely using their username and password.
- **Profile Page**: Users can view their profile page, which displays their posts, comments, draft posts, and notifications.
- **Notification**: Users receive notifications for new likes and comments on their posts, allowing them to stay informed about user interactions.

### Post Interaction

- **View List of Posts**: Users can view a list of posts on the landing page, with options to filter by category and sort by date or popularity.
- **View Post Details**: Users can view the full content of a post, along with comments, likes, and options to like or comment on the post.
- **Create Post**: Users can create new posts by providing a title, content, category, and excerpt.
- **Edit Post**: Users can edit their existing posts, with fields for title, content, category, and excerpt.
- **Delete Post**: Users can delete their posts if they are the author of the post.
- **Like Post**: Users can like posts to show their appreciation for the content.
- **Comment on Post**: Users can comment on posts to share their thoughts and engage with other users.
- **Edit Comment**: Users can edit their comments to update their content.
- **Delete Comment**: Users can delete their comments if they are the author of the comment.
- **Like Comment**: Users can like comments to show their appreciation for the content.

### Admin Panel

- **Admin Panel**: Admin users can access the admin panel to manage users, posts, and comments.
- **User Management**: Admin users can manage user accounts, including viewing user details, updating user information, and deleting user accounts.
- **Post Management**: Admin users can manage posts, including viewing post details, updating post information, and deleting posts.
- **Comment Management**: Admin users can manage comments, including viewing comment details, updating comment information, and deleting comments.


### Future Features

- **Search Functionality**: Implement a search feature to allow users to search for posts based on keywords or categories.
- **User Profiles**: Enhance user profiles with additional information, such as user bio, profile picture, and social media links.
- **User Interactions**: Implement additional user interactions, such as following users, direct messaging, and user mentions.
- **Content Recommendations**: Provide content recommendations based on user preferences, interests, and engagement history.
- **Password Reset**: Implement a password reset feature to allow users to reset their password securely.
- **Media Uploads**: Allow users to upload images, videos, and other media types to enhance their posts.
- **Messaging System**: Implement a messaging system to facilitate private conversations between users.


## Testing

Testing was an integral part of the development process for Echo Chamber, ensuring that the platform functions as intended and meets user requirements effectively. The testing process involved manual testing, and automated testing.

See testing documentation [here](