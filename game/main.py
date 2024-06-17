import random


def choose_options() -> tuple[str, str]:
    options = ["piedra", "papel", "tijera"]
    user_option = input("piedra, papel o tigera => ").lower()
    if not user_option in options:
        return None, None
    pc_option = random.choice(options)
    return user_option, pc_option


def game_rules(user_option: str, pc_option: str) -> str:
    if user_option == pc_option:
        return "draw"
    if user_option == "piedra" and pc_option == "tijera":
        return "user"
    if user_option == "papel" and pc_option == "piedra":
        return "user"
    if user_option == "tijera" and pc_option == "papel":
        return "user"
    return "pc"


def run():
    rounds = 0
    pc_wins = 0
    user_wins = 0
    while True:
        print("*" * 10)
        print(f"ROUND {rounds}")
        print("*" * 10)

        print("User Wins ", user_wins)
        print("Pc Wins ", pc_wins)

        rounds += 1

        user_op, pc_op = choose_options()
        print(user_op, pc_op)
        winner = game_rules(user_op, pc_op)

        if winner == "user":
            user_wins += 1
            print("Round User")
        elif winner == "pc":
            print("Round Pc")
            pc_wins += 1

        if user_wins >= 2:
            print("Win User")
            break
        if pc_wins >= 2:
            print("Pc Win")
            break


if __name__ == "__main__":
    run()
