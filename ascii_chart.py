#!/usr/bin/env python3
"""
ASCII Chart Generator - 터미널 스타일 차트 생성기
"""

def bar_chart(data, title="", max_width=50):
    """수평 막대 차트 생성"""
    if not data:
        return ""

    max_val = max(data.values())
    max_label_len = max(len(str(k)) for k in data.keys())

    lines = []
    if title:
        lines.append(f"\n  {title}")
        lines.append("  " + "─" * (max_width + max_label_len + 10))

    for label, value in data.items():
        bar_len = int((value / max_val) * max_width) if max_val > 0 else 0
        bar = "█" * bar_len + "░" * (max_width - bar_len)
        lines.append(f"  {label:>{max_label_len}} │ {bar} {value:,.0f}")

    lines.append("  " + "─" * (max_width + max_label_len + 10))
    return "\n".join(lines)


def line_chart(data, title="", width=60, height=15):
    """라인 차트 생성 (ASCII 스파크라인)"""
    if not data:
        return ""

    values = list(data.values()) if isinstance(data, dict) else data
    labels = list(data.keys()) if isinstance(data, dict) else list(range(len(data)))

    min_val = min(values)
    max_val = max(values)
    value_range = max_val - min_val if max_val != min_val else 1

    # 차트 그리드 생성
    chart = [[' ' for _ in range(width)] for _ in range(height)]

    # 데이터 포인트 그리기
    for i, val in enumerate(values):
        x = int((i / (len(values) - 1)) * (width - 1)) if len(values) > 1 else 0
        y = height - 1 - int(((val - min_val) / value_range) * (height - 1))
        y = max(0, min(height - 1, y))
        chart[y][x] = '●'

        # 포인트 연결
        if i > 0:
            prev_x = int(((i-1) / (len(values) - 1)) * (width - 1)) if len(values) > 1 else 0
            prev_val = values[i-1]
            prev_y = height - 1 - int(((prev_val - min_val) / value_range) * (height - 1))
            prev_y = max(0, min(height - 1, prev_y))

            # 간단한 선 연결
            for x_pos in range(min(prev_x, x) + 1, max(prev_x, x)):
                ratio = (x_pos - prev_x) / (x - prev_x) if x != prev_x else 0
                y_pos = int(prev_y + ratio * (y - prev_y))
                y_pos = max(0, min(height - 1, y_pos))
                if chart[y_pos][x_pos] == ' ':
                    chart[y_pos][x_pos] = '·'

    lines = []
    if title:
        lines.append(f"\n  {title}")
    lines.append(f"  {max_val:>8,.1f} ┤")

    for i, row in enumerate(chart):
        if i == 0:
            lines.append(f"           │{''.join(row)}")
        elif i == height - 1:
            lines.append(f"  {min_val:>8,.1f} ┤{''.join(row)}")
        else:
            lines.append(f"           │{''.join(row)}")

    lines.append("           └" + "─" * width)

    return "\n".join(lines)


def sparkline(data, title=""):
    """미니 스파크라인"""
    blocks = " ▁▂▃▄▅▆▇█"
    values = list(data.values()) if isinstance(data, dict) else data

    if not values:
        return ""

    min_val = min(values)
    max_val = max(values)
    value_range = max_val - min_val if max_val != min_val else 1

    spark = ""
    for val in values:
        idx = int(((val - min_val) / value_range) * 8)
        idx = max(0, min(8, idx))
        spark += blocks[idx]

    result = f"  {title}: {spark}" if title else f"  {spark}"
    result += f"  (min: {min_val:,.1f}, max: {max_val:,.1f})"
    return result


def table(headers, rows, title=""):
    """ASCII 테이블 생성"""
    if not headers or not rows:
        return ""

    # 열 너비 계산
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    lines = []
    if title:
        lines.append(f"\n  {title}")

    # 상단 테두리
    border = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐"
    lines.append("  " + border)

    # 헤더
    header_row = "│" + "│".join(f" {h:^{col_widths[i]}} " for i, h in enumerate(headers)) + "│"
    lines.append("  " + header_row)

    # 구분선
    separator = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤"
    lines.append("  " + separator)

    # 데이터 행
    for row in rows:
        row_str = "│" + "│".join(f" {str(cell):>{col_widths[i]}} " for i, cell in enumerate(row)) + "│"
        lines.append("  " + row_str)

    # 하단 테두리
    bottom = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘"
    lines.append("  " + bottom)

    return "\n".join(lines)


def progress_bar(current, total, width=40, label="Progress"):
    """진행률 바"""
    percent = current / total if total > 0 else 0
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    return f"  {label}: [{bar}] {percent*100:.1f}% ({current}/{total})"


# 데모
if __name__ == "__main__":
    print("\n" + "="*70)
    print("  ASCII CHART GENERATOR - DEMO")
    print("="*70)

    # 막대 차트 예시
    sales_data = {
        "Jan": 12500,
        "Feb": 18200,
        "Mar": 15800,
        "Apr": 22100,
        "May": 19500,
        "Jun": 25300,
    }
    print(bar_chart(sales_data, title="📊 Monthly Sales (2024)"))

    # 라인 차트 예시
    stock_data = {
        "Mon": 145.2,
        "Tue": 148.5,
        "Wed": 142.8,
        "Thu": 151.3,
        "Fri": 149.7,
        "Sat": 155.2,
        "Sun": 158.9,
    }
    print(line_chart(stock_data, title="📈 Stock Price (Weekly)", width=50, height=10))

    # 스파크라인 예시
    temp_data = [22, 24, 23, 26, 28, 27, 25, 24, 23, 22, 21, 23, 25, 27, 29, 28]
    print("\n" + sparkline(temp_data, title="🌡️  Temperature"))

    # 테이블 예시
    headers = ["Asset", "Price", "Change", "Volume"]
    rows = [
        ["BTC", "42,150", "+2.3%", "12.5B"],
        ["ETH", "2,280", "-0.8%", "5.2B"],
        ["SOL", "98.50", "+5.1%", "1.8B"],
        ["XRP", "0.62", "+1.2%", "892M"],
    ]
    print(table(headers, rows, title="💹 Crypto Market"))

    # 진행률 바 예시
    print("\n")
    print(progress_bar(75, 100, label="Download"))
    print(progress_bar(42, 100, label="Upload  "))
    print(progress_bar(100, 100, label="Complete"))

    print("\n" + "="*70 + "\n")
