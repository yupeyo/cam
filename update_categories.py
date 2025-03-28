
#instances_train2017_ko 만드는 코드드
import json

def update_categories(input_json, output_json):
    # JSON 파일 열기
    with open(input_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 클래스 이름을 한글로 변경
    for category in data['categories']:
        if category['name'] == "person":
            category['name'] = "사람"
        elif category['name'] == "bicycle":
            category['name'] = "자전거"
        elif category['name'] == "car":
            category['name'] = "자동차"

    # 수정된 JSON 파일 저장
    with open(output_json, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"한글로 수정된 JSON 파일이 '{output_json}'에 저장되었습니다!")

# 실행
update_categories(
    input_json="dataset/instances_train2017.json",  # 원본 JSON 파일 경로
    output_json="dataset/instances_train2017_ko.json"  # 수정된 JSON 파일 저장 경로
)
