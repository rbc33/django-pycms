from faker import Faker
from mdgen import MarkdownPostProvider
import requests

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
    "http://localhost:8081/posts",
    json=post,
    headers={"Content-type": "application/json"},
)

print(f"Status code: {make_post.status_code}")
print(f"Response: {make_post.text}")
