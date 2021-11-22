from app.config.config import ticket_length


def generate_ticket():
    from string import ascii_letters, digits
    import random
    return ''.join(random.sample(ascii_letters + digits, ticket_length))


def get_ticket(user):
    from app.config.config import redis_key_prefix, ticket_expire_time
    from app import redis as rd
    key = redis_key_prefix + 'session::' + user.username
    return rd.get(key)


def renew_ticket(user):
    from app.config.config import redis_key_prefix, ticket_expire_time
    from app import redis as rd
    ticket = generate_ticket()
    key = redis_key_prefix + 'session::' + user.username
    rd.set(key, ticket)
    rd.expire(key, ticket_expire_time)
    return ticket
