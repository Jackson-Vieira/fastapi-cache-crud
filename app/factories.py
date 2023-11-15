from models import Pessoa
from faker import Faker

faker = Faker()


def create_fake_person():
    return Pessoa(
        apelido=faker.user_name(),
        nome=faker.name(),
        nascimento=faker.date_of_birth().strftime("%Y-%m-%d"),
        stack=[
            faker.random_element(["Python", "Java", "JavaScript"]) for _ in range(3)
        ],
    )
