LINE = "=" * 40


class Quiz:
    """퀴즈 한 문제를 표현한다. 정답은 1~4 중 하나의 번호로 관리한다."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        """문제와 선택지를 출력한다."""
        print(self.question)
        print()
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")
        print()

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답인지 확인한다."""
        return user_answer == self.answer


def default_quizzes():
    """기본 퀴즈 (주제: 파이썬 기초)."""
    return [
        Quiz("Python에서 문자열 자료형의 이름은?", ["int", "str", "bool", "list"], 2),
        Quiz("값이 바뀔 수 있는 순서 있는 자료형은?", ["tuple", "str", "list", "int"], 3),
        Quiz(
            "키(key)와 값(value)을 짝지어 저장하는 자료형은?",
            ["list", "dict", "bool", "str"],
            2,
        ),
        Quiz(
            "클래스에서 객체가 만들어질 때 자동으로 호출되는 메서드는?",
            ["__str__", "__call__", "__init__", "__del__"],
            3,
        ),
        Quiz(
            "조건이 참인 동안 계속 반복하는 문법은?",
            ["if", "while", "def", "import"],
            2,
        ),
    ]


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
    quizzes = default_quizzes()
    print(f"📂 기본 퀴즈 {len(quizzes)}개를 준비했습니다.")
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
