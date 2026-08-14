from openpyxl import load_workbook
import json
from pathlib import Path

# =========================
# 設定
# =========================

# この sync.py と同じフォルダにExcelとrules.jsonを置く想定
EXCEL_FILE = "桶文字対応表 from MAKU.xlsx"
SHEET_NAME = "対応表"
JSON_FILE = "rules.json"

# Excelの列
BEFORE_COLUMN = 2  # B列
AFTER_COLUMN = 3   # C列

# データ開始行
START_ROW = 3


# =========================
# Excel → rules.json
# =========================

def main():
    excel_path = Path(__file__).parent / EXCEL_FILE
    json_path = Path(__file__).parent / JSON_FILE

    if not excel_path.exists():
        print(f"Excelファイルが見つかりません: {excel_path}")
        return

    wb = load_workbook(excel_path, data_only=True)

    if SHEET_NAME not in wb.sheetnames:
        print(f"シート「{SHEET_NAME}」が見つかりません。")
        print(f"利用可能なシート: {', '.join(wb.sheetnames)}")
        return

    ws = wb[SHEET_NAME]

    rules = {}

    for row in range(START_ROW, ws.max_row + 1):
        before = ws.cell(row=row, column=BEFORE_COLUMN).value
        after = ws.cell(row=row, column=AFTER_COLUMN).value

        # B列またはC列が空欄ならスキップ
        if before is None or after is None:
            continue

        before = str(before)
        after = str(after)

        rules[before] = after

    # JSONを書き出す
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            rules,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("================================")
    print("rules.json を更新しました！")
    print(f"登録件数: {len(rules)}")
    print(f"出力先: {json_path}")
    print("================================")


if __name__ == "__main__":
    main()
