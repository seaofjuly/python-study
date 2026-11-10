"""Mini NPU Simulator

MAC(Multiply-Accumulate) 연산으로 입력 패턴이 Cross(십자가)인지 X인지 판정하는
콘솔 프로그램입니다. 외부 라이브러리 없이 표준 라이브러리(json, time, re, os)만 사용합니다.
"""

import json
import os
import re
import sys
import time

# ----------------------------------------
# 상수
# ----------------------------------------
EPSILON = 1e-9          # 점수 비교 허용오차: |A-B| < EPSILON 이면 동점
EPSILON_TEXT = "1e-9"   # 화면 출력용
REPEAT = 10             # 성능 측정 반복 횟수
LABEL_CROSS = "Cross"   # 표준 라벨
LABEL_X = "X"
LABEL_UNDECIDED = "UNDECIDED"
PERF_SIZES = [3, 5, 13, 25]

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
PATTERN_KEY_RULE = re.compile(r"^size_(\d+)_(\d+)$")
FILTER_KEY_RULE = re.compile(r"^size_(\d+)$")

# 여러 형태의 라벨을 표준 라벨(Cross/X)로 바꾸는 표
LABEL_MAP = {
    "+": LABEL_CROSS,
    "cross": LABEL_CROSS,
    "x": LABEL_X,
}


# ----------------------------------------
# 출력 도우미
# ----------------------------------------
def print_section(title):
    print()
    print("#" + "-" * 39)
    print(f"# {title}")
    print("#" + "-" * 39)


# ----------------------------------------
# 1. 데이터 구조: n×n 2차원 배열
# ----------------------------------------
def make_matrix(n, value=0.0):
    """n×n 크기의 2차원 배열을 만든다."""
    return [[value for _ in range(n)] for _ in range(n)]


def get_value(matrix, row, col):
    """특정 위치의 값을 읽는다."""
    return matrix[row][col]


def set_value(matrix, row, col, value):
    """특정 위치에 값을 저장한다."""
    matrix[row][col] = value


def check_matrix(matrix, n):
    """matrix가 숫자로 이루어진 n×n 배열인지 검사한다. 문제가 없으면 None, 있으면 사유 문자열."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return "2차원 배열 형식이 아님"
    cols = {len(row) for row in matrix}
    if len(matrix) != n or cols != {n}:
        if len(cols) == 1:
            shape = f"{len(matrix)}×{cols.pop()}"
        else:
            shape = f"{len(matrix)}행, 열 개수 제각각"
        return f"크기 불일치 (입력 {shape}, 기대 {n}×{n})"
    for row in matrix:
        for value in row:
            # bool은 int의 하위 타입이라 따로 제외한다.
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                return f"숫자가 아닌 값 포함 ({value!r})"
    return None


# ----------------------------------------
# 2. 라벨 정규화
# ----------------------------------------
def normalize_label(raw):
    """'+', 'cross', 'x' 등을 표준 라벨 Cross / X 로 바꾼다. 모르면 None."""
    if not isinstance(raw, str):
        return None
    return LABEL_MAP.get(raw.strip().lower())


# ----------------------------------------
# 3. MAC 연산
# ----------------------------------------
def mac(pattern, filt):
    """같은 위치끼리 곱하고(Multiply) 모두 더한다(Accumulate). 2차원 버전."""
    n = len(pattern)
    total = 0.0
    for i in range(n):
        for j in range(n):
            total += pattern[i][j] * filt[i][j]
    return total


def flatten(matrix):
    """[보너스] 2차원 배열을 길이 N²의 1차원 배열로 펼친다."""
    flat = []
    for row in matrix:
        for value in row:
            flat.append(value)
    return flat


def mac_flat(pattern_flat, filter_flat):
    """[보너스] 1차원 배열 버전 MAC. 인덱스 하나로만 접근한다."""
    total = 0.0
    for k in range(len(pattern_flat)):
        total += pattern_flat[k] * filter_flat[k]
    return total


# ----------------------------------------
# 4. 점수 비교 정책 (epsilon)
# ----------------------------------------
def judge(score_a, score_b, label_a="A", label_b="B"):
    """두 점수를 비교해 더 큰 쪽 라벨을 돌려준다. 차이가 EPSILON 미만이면 동점."""
    if abs(score_a - score_b) < EPSILON:
        return LABEL_UNDECIDED
    return label_a if score_a > score_b else label_b


# ----------------------------------------
# 5. 성능 측정
# ----------------------------------------
def measure_ms(func, *args, repeat=REPEAT):
    """func(*args)를 repeat번 실행한 평균 시간(ms). 입출력은 측정에 포함하지 않는다."""
    func(*args)  # 워밍업: 첫 호출의 준비 비용이 평균에 섞이지 않게 한 번 먼저 실행한다.
    total = 0.0
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        total += time.perf_counter() - start
    return total / repeat * 1000


# ----------------------------------------
# 6. [보너스] 패턴 생성기
# ----------------------------------------
def generate_cross(n):
    """n×n 십자가 패턴: 가운데 행과 가운데 열이 1."""
    matrix = make_matrix(n)
    mid = n // 2
    for k in range(n):
        set_value(matrix, mid, k, 1.0)
        set_value(matrix, k, mid, 1.0)
    return matrix


def generate_x(n):
    """n×n X 패턴: 두 대각선이 1."""
    matrix = make_matrix(n)
    for k in range(n):
        set_value(matrix, k, k, 1.0)
        set_value(matrix, k, n - 1 - k, 1.0)
    return matrix


def print_performance_table(sizes):
    """크기별 평균 시간(ms)과 연산 횟수(N²) 표. 보너스로 1차원 최적화 결과도 비교한다."""
    print(f"{'크기':<8}{'평균 시간(ms)':>14}{'연산 횟수':>10}")
    print("-" * 36)
    results = []
    for n in sizes:
        pattern = generate_cross(n)
        filt = generate_cross(n)
        ms_2d = measure_ms(mac, pattern, filt)
        p_flat, f_flat = flatten(pattern), flatten(filt)
        ms_1d = measure_ms(mac_flat, p_flat, f_flat)
        results.append((n, ms_2d, ms_1d))
        print(f"{f'{n}×{n}':<8}{ms_2d:>14.4f}{n * n:>10}")

    print()
    print(f"[보너스] 2차원 vs 1차원 배열 비교 (동일 입력, {REPEAT}회 평균)")
    print(f"{'크기':<8}{'2D(ms)':>10}{'1D(ms)':>10}{'1D/2D':>8}")
    print("-" * 36)
    for n, ms_2d, ms_1d in results:
        ratio = ms_1d / ms_2d if ms_2d > 0 else 0
        print(f"{f'{n}×{n}':<8}{ms_2d:>10.4f}{ms_1d:>10.4f}{ratio:>8.2f}")


# ----------------------------------------
# 모드 1: 사용자 입력 (3×3)
# ----------------------------------------
def read_matrix(title, n=3):
    """n줄을 공백 구분으로 입력받는다. 형식이 틀리면 그 행렬을 처음부터 다시 입력받는다."""
    while True:
        print(f"{title} ({n}줄 입력, 공백 구분)")
        matrix = []
        ok = True
        for _ in range(n):
            parts = input().split()
            if len(parts) != n:
                ok = False
                break
            try:
                matrix.append([float(p) for p in parts])
            except ValueError:
                ok = False
                break
        if ok:
            return matrix
        print(f"⚠️ 입력 형식 오류: 각 줄에 {n}개의 숫자를 공백으로 구분해 입력하세요. 다시 입력해 주세요.")
        print()


def print_matrix(matrix):
    for row in matrix:
        print("  " + " ".join(f"{v:g}" for v in row))


def run_user_mode():
    print_section("[1] 필터 입력")
    filter_a = read_matrix("필터 A")
    print()
    filter_b = read_matrix("필터 B")

    print()
    print("✓ 필터 저장 완료")
    print("필터 A:")
    print_matrix(filter_a)
    print("필터 B:")
    print_matrix(filter_b)

    print_section("[2] 패턴 입력")
    pattern = read_matrix("패턴")

    print_section("[3] MAC 결과")
    score_a = mac(pattern, filter_a)
    score_b = mac(pattern, filter_b)
    elapsed = (measure_ms(mac, pattern, filter_a) + measure_ms(mac, pattern, filter_b)) / 2
    result = judge(score_a, score_b, "A", "B")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/{REPEAT}회): {elapsed:.4f} ms")
    if result == LABEL_UNDECIDED:
        print(f"판정: 판정 불가 (|A-B| < {EPSILON_TEXT})")
    else:
        print(f"판정: {result}")

    print_section(f"[4] 성능 분석 (평균/{REPEAT}회)")
    print_performance_table([3])


# ----------------------------------------
# 모드 2: data.json 분석
# ----------------------------------------
def load_json(path):
    """data.json을 읽는다. 파일이 없거나 깨졌으면 안내 후 None."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ 데이터 파일을 찾을 수 없습니다: {path}")
    except json.JSONDecodeError as e:
        print(f"⚠️ data.json 형식이 올바르지 않습니다: {e}")
    except OSError as e:
        print(f"⚠️ 파일을 읽는 중 오류가 발생했습니다: {e}")
    return None


def load_filters(raw_filters):
    """filters 항목을 {N: {'Cross': 배열, 'X': 배열}} 로 정리한다. 키 라벨도 정규화한다."""
    filters = {}
    if not isinstance(raw_filters, dict):
        print("⚠️ filters 항목이 없거나 형식이 올바르지 않습니다.")
        return filters

    for size_key, group in raw_filters.items():
        match = FILTER_KEY_RULE.match(size_key)
        if not match:
            print(f"✗ {size_key}: 키 형식 오류 (size_N 형태여야 합니다)")
            continue
        n = int(match.group(1))
        if not isinstance(group, dict):
            print(f"✗ {size_key}: 필터 묶음 형식 오류")
            continue

        loaded = {}
        problems = []
        for raw_label, matrix in group.items():
            label = normalize_label(raw_label)
            if label is None:
                problems.append(f"알 수 없는 라벨 '{raw_label}'")
            elif check_matrix(matrix, n):
                problems.append(f"{label} 필터 오류: {check_matrix(matrix, n)}")
            else:
                loaded[label] = matrix

        filters[n] = loaded
        if LABEL_CROSS in loaded and LABEL_X in loaded:
            print(f"✓ {size_key:<8} 필터 로드 완료 (Cross, X)")
        else:
            missing = [lb for lb in (LABEL_CROSS, LABEL_X) if lb not in loaded]
            problems.append(f"누락: {', '.join(missing)}")
        for p in problems:
            print(f"  ⚠️ {size_key}: {p}")
    return filters


def pattern_sort_key(key):
    """size_5_1, size_5_2, size_13_1 ... 순서로 정렬하기 위한 키."""
    match = PATTERN_KEY_RULE.match(key)
    if match:
        return (0, int(match.group(1)), int(match.group(2)), key)
    return (1, 0, 0, key)


def analyze_pattern(key, item, filters):
    """패턴 하나를 검증·판정한다. (통과 여부, 실패 사유)를 돌려준다. 예외를 밖으로 내보내지 않는다."""
    print(f"--- {key} ---")

    match = PATTERN_KEY_RULE.match(key)
    if not match:
        return fail("키 형식 오류 (size_N_idx 형태가 아님)")
    n = int(match.group(1))

    if not isinstance(item, dict) or "input" not in item or "expected" not in item:
        return fail("스키마 오류 (input 또는 expected 누락)")

    expected = normalize_label(item["expected"])
    if expected is None:
        return fail(f"알 수 없는 expected 라벨 '{item['expected']}'")

    group = filters.get(n, {})
    if LABEL_CROSS not in group or LABEL_X not in group:
        return fail(f"size_{n} 필터가 없음")

    pattern = item["input"]
    problem = check_matrix(pattern, n)
    if problem:
        return fail(f"패턴 {problem}")

    cross_score = mac(pattern, group[LABEL_CROSS])
    x_score = mac(pattern, group[LABEL_X])
    result = judge(cross_score, x_score, LABEL_CROSS, LABEL_X)

    print(f"Cross 점수: {cross_score}")
    print(f"X 점수: {x_score}")
    if result == expected:
        print(f"판정: {result} | expected: {expected} | PASS")
        return True, ""
    if result == LABEL_UNDECIDED:
        print(f"판정: {result} | expected: {expected} | FAIL (동점 규칙)")
        return False, "동점(UNDECIDED) 처리 규칙에 따라 FAIL"
    print(f"판정: {result} | expected: {expected} | FAIL")
    return False, f"판정 {result} ≠ expected {expected}"


def fail(reason):
    print(f"FAIL: {reason}")
    return False, reason


def run_json_mode(path=DATA_PATH):
    print(f"📂 분석 파일: {os.path.basename(path)}")
    data = load_json(path)
    if not isinstance(data, dict):
        if data is not None:
            print("⚠️ data.json 최상위는 객체({...})여야 합니다.")
        return

    print_section("[1] 필터 로드")
    filters = load_filters(data.get("filters"))

    print_section("[2] 패턴 분석 (라벨 정규화 적용)")
    patterns = data.get("patterns")
    if not isinstance(patterns, dict):
        print("⚠️ patterns 항목이 없거나 형식이 올바르지 않습니다.")
        patterns = {}

    total = passed = 0
    failures = []
    for key in sorted(patterns, key=pattern_sort_key):
        try:
            ok, reason = analyze_pattern(key, patterns[key], filters)
        except Exception as e:  # 어떤 데이터가 와도 프로그램이 멈추지 않게 한다.
            ok, reason = fail(f"예상하지 못한 오류 ({e})")
        total += 1
        if ok:
            passed += 1
        else:
            failures.append((key, reason))

    print_section(f"[3] 성능 분석 (평균/{REPEAT}회)")
    print_performance_table(PERF_SIZES)

    print_section("[4] 결과 요약")
    print(f"총 테스트: {total}개")
    print(f"통과: {passed}개")
    print(f"실패: {len(failures)}개")
    if failures:
        print()
        print("실패 케이스:")
        for key, reason in failures:
            print(f"- {key}: {reason}")


# ----------------------------------------
# 시작
# ----------------------------------------
def select_mode():
    while True:
        print()
        print("[모드 선택]")
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")
        choice = input("선택: ").strip()
        if choice in ("1", "2"):
            return choice
        print("⚠️ 잘못된 입력입니다. 1 또는 2를 입력하세요.")


def main():
    print("=== Mini NPU Simulator ===")
    try:
        if select_mode() == "1":
            run_user_mode()
        else:
            # python main.py 다른파일.json 처럼 경로를 주면 그 파일을 분석한다.
            run_json_mode(sys.argv[1] if len(sys.argv) > 1 else DATA_PATH)
    except (KeyboardInterrupt, EOFError):
        print()
        print("입력이 중단되어 프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
