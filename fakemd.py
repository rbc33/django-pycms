from faker import Faker
from mdgen import MarkdownPostProvider
import requests


def post_fake(PORT):
    fake = Faker()
    fake.add_provider(MarkdownPostProvider)
    fake_post = fake.post(size="medium")  # available sizes: 'small', 'medium', 'large'
    post = {
        "title": fake.text(max_nb_chars=20),
        "excerpt": fake.text(max_nb_chars=200),
        "content": fake_post,
    }
    print(post)

    make_post = requests.post(
        f"http://localhost:{PORT}/posts",
        json=post,
        headers={"Content-type": "application/json"},
    )

    print(f"Status code: {make_post.status_code}")
    print(f"Response: {make_post.text}")


if __name__ == "__main__":
    PORT = 8000
    for _ in range(5):
        post_fake(PORT)
