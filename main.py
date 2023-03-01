import connect_db
from seeds import seed_groups, seed_students, seed_teachers, seed_disciplines, seed_grades


if __name__ == '__main__':
    seed_teachers()
    seed_groups()
    seed_students()
    seed_disciplines()
    seed_grades()

