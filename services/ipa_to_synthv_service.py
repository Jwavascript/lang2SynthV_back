import csv
import os

# CSV 파일 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, "../data", "synsVipa.csv")

# CSV 데이터 로드
def load_csv_data(file_path):
    ipa_to_synthv = {}
    ipa_symbols = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ipa = row["ipa"].strip()
            synthv = f'{row["synthv"].strip()} ({row["language"].strip()})'
            if ipa:
                if ipa not in ipa_to_synthv:
                    ipa_to_synthv[ipa] = []
                ipa_to_synthv[ipa].append(synthv)
                ipa_symbols.append(ipa)
    ipa_symbols.sort(key=lambda x: -len(x))  # 긴 기호 우선
    return ipa_to_synthv, ipa_symbols

# 데이터 로드
ipa_data, ipa_symbols = load_csv_data(CSV_FILE_PATH)

def split_ipa_symbols(text: str):
    """
    입력 텍스트를 IPA 기호로 분리.
    """
    result = []
    while text:
        matched = False
        for symbol in ipa_symbols:
            if text.startswith(symbol):
                result.append(symbol)
                text = text[len(symbol):]
                matched = True
                break
        if not matched:
            result.append(text[0])
            text = text[1:]
    return result

def ipa_to_synthv(text: str):
    """
    IPA 기호 → SynthV 변환.
    """
    split_symbols = split_ipa_symbols(text)
    results = []

    for symbol in split_symbols:
        if symbol in ipa_data:
            results.append({"ipa": symbol, "synthv": ipa_data[symbol]})
        else:
            results.append({"ipa": symbol, "synthv": ["Not found"]})
    return results
