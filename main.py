from faker import Faker
fake = Faker()


class BusinessCard():
    def __init__(self, first_name = "", last_name = "", company = "", position = "", email ="", phone_number=""):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"Wizytowka {self.first_name:20} {self.last_name:20} {self.company:30} {self.position:30} {self.email:30} {self.phone_number:20} "

    def __str__(self):
        return self.__repr__()

    def contact(self):
        print(f"Skontaktuj sie z: {self.first_name} {self.last_name} {self.company} {self.position} {self.email}")

    @property
    def name_len(self):
        return len(self.first_name), len(self.last_name)


wizytowki = []
for i in range(5):
    wizytowki.append(BusinessCard(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.email(), phone_number=fake.phone_number()))

print(wizytowki)

for w in sorted(wizytowki, key=lambda w: w.first_name):
    print(w)

print()

for w in sorted(wizytowki, key=lambda w: w.last_name):
    print(w)

print()

for w in sorted(wizytowki, key=lambda w: w.email):
    print(w)

wizytowki[0].contact()
print(wizytowki[0].name_len)

class BaseContact():
    def __init__(self, first_name = "", last_name = "", email ="", phone_number=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonie do {self.first_name} {self.last_name}")

    @property
    def label_lenght(self):
        return len(self.first_name), len(self.last_name)

wizytowki = []
for i in range(5):
    wizytowki.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), phone_number=fake.phone_number()))

wizytowki[1].contact()
print(wizytowki[1].label_lenght)


class BusinessContact(BaseContact):
    def __init__(self, company="", position="", company_phone="", *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.company = company
        self.position = position
        self.company_phone = company_phone

    def contact(self):
        print(f"Wybieram numer (sluzbowy) {self.company_phone} i dzwonie do {self.first_name} {self.last_name}")

    @property
    def label_lenght(self):
        return len(self.first_name), len(self.last_name)

wizytowki = []
for i in range(5):
    wizytowki.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.email(), phone_number=fake.phone_number(), company_phone=fake.phone_number()))

wizytowki[1].contact()
print(wizytowki[1].label_lenght)


def create(card_type, count):
    wizytowki = []
    if card_type == BaseContact:
        for i in range(count):
            wizytowki.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(),
                                         phone_number=fake.phone_number()))

    elif card_type == BusinessContact:
        for i in range(count):
            wizytowki.append(
                BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(),
                                position=fake.job(), email=fake.email(), phone_number=fake.phone_number(),
                                company_phone=fake.phone_number()))
    return wizytowki


w = create(BaseContact, 5)

for card in w:
    card.contact()

print()

b = create(BusinessContact, 5)

for card in b:
    card.contact()