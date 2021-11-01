from app.config.config import ticket_length


def generate_ticket():
    from string import ascii_letters, digits
    import random
    return ''.join(random.sample(ascii_letters + digits, ticket_length))
