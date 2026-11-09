LINE = "=" * 40
SUB_LINE = "-" * 40


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


class QuizGame:
    """게임 전체(메뉴, 풀기, 추가, 목록, 점수)를 관리한다."""

    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score = None  # 최고 점수(100점 만점), 아직 안 풀었으면 None
        self.best_correct = 0
        self.best_total = 0

    # ---------- 입력 처리 ----------
    def read_number(self, prompt, minimum, maximum):
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

    def read_text(self, prompt):
        """빈 문자열이 아닌 텍스트가 입력될 때까지 다시 입력받는다."""
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("⚠️ 입력이 비어 있습니다. 다시 입력하세요.")

    # ---------- 화면 ----------
    def show_menu(self):
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

    # ---------- 기능 ----------
    def play(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")
        correct = 0
        for index, quiz in enumerate(self.quizzes, start=1):
            print()
            print(SUB_LINE)
            print(f"[문제 {index}]")
            quiz.show()
            user_answer = self.read_number("정답 입력: ", 1, 4)
            if quiz.is_correct(user_answer):
                correct += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        score = correct * 100 // total
        print()
        print(LINE)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.best_correct = correct
            self.best_total = total
            print("🎉 새로운 최고 점수입니다!")
        print(LINE)

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = self.read_text("문제를 입력하세요: ")
        choices = [self.read_text(f"선택지 {i}: ") for i in range(1, 5)]
        answer = self.read_number("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("\n✅ 퀴즈가 추가되었습니다!")

    def show_list(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print(SUB_LINE)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print(SUB_LINE)

    def show_score(self):
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요.")
            return
        print(
            f"\n🏆 최고 점수: {self.best_score}점 "
            f"({self.best_total}문제 중 {self.best_correct}문제 정답)"
        )

    # ---------- 실행 ----------
    def run(self):
        print(f"📂 기본 퀴즈 {len(self.quizzes)}개를 준비했습니다.")
        while True:
            self.show_menu()
            choice = self.read_number("선택: ", 1, 5)
            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            else:
                print("👋 게임을 종료합니다!")
                break


def main():
    QuizGame().run()


if __name__ == "__main__":
    main()
