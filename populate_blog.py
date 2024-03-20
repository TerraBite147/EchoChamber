import os
import django
from faker import Faker
import random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echo_chamber.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Post, PostLike, Comment, CommentLike, Notification

fake = Faker()


def add_category():
    cat = Category.objects.create(
        name=fake.word().capitalize(),
        description=fake.text(max_nb_chars=200)
    )
    cat.save()
    return cat


def add_post(user, category):
    end_date = datetime(2024, 3, 6)
    post_date = fake.date_time_between(start_date="-3y", end_date=end_date)

    post = Post.objects.create(
        title=fake.sentence(),
        slug=fake.slug(),
        author=user,
        content=fake.text(max_nb_chars=1000),
        posted_at=post_date,
        category=category,
        status=random.choice([0, 1]),
        excerpt=fake.text(max_nb_chars=200),
        updated_on=post_date  # Use the same date or generate another within the range
    )
    post.save()
    return post


def add_comment(user, post):
    comment = Comment.objects.create(
        post=post,
        author=user,
        content=fake.paragraph(),
        created_at=fake.date_time_this_year()
    )
    comment.save()
    return comment


def add_post_like(user, post):
    post_like, created = PostLike.objects.get_or_create(
        user=user,
        post=post
    )
    if created:
        post_like.save()


def add_comment_like(user, comment):
    if not comment.likes.filter(id=user.id).exists():
        comment.likes.add(user)


def populate(N=10):  # N is the number of posts to create
    users = list(User.objects.all())
    categories = list(Category.objects.all())

    if not categories:
        for _ in range(5):  # Create 5 categories if none exist
            categories.append(add_category())

    for _ in range(N):
        user = random.choice(users)
        category = random.choice(categories)
        post = add_post(user, category)

        for _ in range(random.randint(1, 5)):  # 1 to 5 comments per post
            comment_user = random.choice(users)
            comment = add_comment(comment_user, post)

            for _ in range(random.randint(0, 3)):  # 0 to 3 likes per comment
                commenter = random.choice(users)
                add_comment_like(commenter, comment)

            if random.choice([True, False]):  # Randomly decide if the post is liked
                liker = random.choice(users)
                add_post_like(liker, post)

if __name__ == '__main__':
    print("Populating the blog...")
    populate(50)  # Adjust the number as needed
    print("Population complete.")
