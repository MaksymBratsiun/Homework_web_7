import connect_db
from seeds import seed_groups, seed_students


if __name__ == '__main__':
    seed_groups()
    seed_students()
