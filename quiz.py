LINE = "=" * 40


def read_number(prompt, minimum, maximum):
    """범위 안의 숫자가 입력될 때까지 다시 입력받는다."""
    while True:
        text = input(prompt).strip()
        if not text:
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue
        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
            continue
        if not minimum <= number <= maximum:
            print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
            continue
        return number


def show_menu():
    print()
    print(LINE)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print(LINE)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print(LINE)


def main():
    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)
        if choice == 1:
            print("퀴즈를 시작합니다!")
        elif choice == 2:
            print("퀴즈를 추가합니다!")
        elif choice == 3:
            print("퀴즈 목록을 보여줍니다!")
        elif choice == 4:
            print("점수 확인")
        else:
            print("👋 게임을 종료합니다!")
            break


if __name__ == "__main__":
    main()
