"""정오표·안티패턴 Markdown 표의 형식을 점검한다.

- 표마다 모든 행의 열 수가 머리 행과 같은가 (칸 안의 \\| 는 구분자로 세지 않음)
- 표 행에 〃 표기가 없는가
- K·AP 번호가 겹치지 않고 오름차순인가

사용: python check_tables.py <파일> [<파일> ...]
문제가 없으면 종료 코드 0, 있으면 1.
"""
import re
import sys


def cells(line):
    # 이스케이프된 파이프를 지운 뒤 구분자를 센다
    return line.replace("\\|", "").count("|")


def check(path):
    problems = []
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    header_cols = None
    ids = []
    for no, line in enumerate(lines, 1):
        if not line.startswith("|"):
            header_cols = None
            continue
        n = cells(line)
        if header_cols is None:
            header_cols = n
        elif n != header_cols:
            problems.append(f"{path}:{no}: 열 수 {n - 1}개, 머리 행은 {header_cols - 1}개")
        if "〃" in line:
            problems.append(f"{path}:{no}: 〃 표기 대신 실제 출처를 쓴다")
        m = re.match(r"^\|\s*(K|AP)(\d+)\s*\|", line)
        if m:
            ids.append((no, m.group(1), int(m.group(2))))

    seen = {}
    last = {}
    for no, prefix, num in ids:
        key = (prefix, num)
        if key in seen:
            problems.append(f"{path}:{no}: {prefix}{num} 번호가 {seen[key]}행과 겹친다")
        seen.setdefault(key, no)
        if prefix in last and num < last[prefix]:
            problems.append(f"{path}:{no}: {prefix}{num}이 {prefix}{last[prefix]} 뒤에 있다")
        last[prefix] = num
    return problems


def main(paths):
    # Windows 콘솔 기본 인코딩(cp949)에서도 한국어가 깨지지 않게 한다
    sys.stdout.reconfigure(encoding="utf-8")
    problems = [p for path in paths for p in check(path)]
    for p in problems:
        print(p)
    if not problems:
        print("OK: " + ", ".join(paths))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
