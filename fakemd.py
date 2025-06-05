from faker import Faker
from mdgen import MarkdownPostProvider
import requests


def post_fake(PORT):
    # fake = Faker()
    # fake.add_provider(MarkdownPostProvider)
    # fake_post = fake.post(size="medium")  # available sizes: 'small', 'medium', 'large'
    fake_post = """# My Game of Life

        <iframe 
        src="https://rbc33.github.io/html-life/" 
        width="820" 
        height="620" 
        frameborder="0"
        style="border: 2px solid #4a5568; border-radius: 8px;">
        </iframe>

        ## Controles:
        - **P**: Pausar/Reanudar
        - **R**: Patrón aleatorio
        - **+/-**: Cambiar velocidad"""
    # post = {
    #     "title": fake.text(max_nb_chars=20),
    #     "excerpt": fake.text(max_nb_chars=200),
    #     "content": fake_post,
    # }
    post = {
        "title": "the game of life",
        "excerpt": """lets see it the game works!! click to discover!""",
        "content": fake_post,
    }
    print(post)

    make_post = requests.post(
        f"http://localhost:{PORT}/posts",
        # f"http://192.168.0.100:{PORT}/posts",
        json=post,
        headers={"Content-type": "application/json"},
    )

    print(f"Status code: {make_post.status_code}")
    print(f"Response: {make_post.text}")


if __name__ == "__main__":
    PORT = 8000
    for _ in range(1):
        post_fake(PORT)
