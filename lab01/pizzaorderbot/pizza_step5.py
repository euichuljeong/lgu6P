# pizza_step5.py

def main() :
    menus = {
            '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
            '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'], ######## 추가
            '사이드' : ['치즈 오븐 스파게티', '리조또', '치킨 윙'],
            '음료' : ['콜라', '스프라이트', '오렌지 쥬스']
        }
    prices = {
            '피자': [29000, 32000, 32000],
            '토핑': [500, 500, 800, 300, 800], ######## 추가
            '사이드': [9900, 8900, 8900],
            '음료' : [1000, 1000, 1000]
        }
    order = {'피자': [], '토핑': [], '사이드':[], '음료':[] }

    categories = ['피자', '토핑', '사이드', '음료']

    category_index = 0
    current_category = categories[ category_index ]

    while True:
        print(f"\n{current_category}를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.")

        print("\n현재 장바구니:", order)

        for idx, item in enumerate(menus[current_category]):
                print(f"{idx+1}, {item} ({prices[current_category][idx]}원) ")

        choice = input("번호를 선택하고 Enter를 누르세요.(다음단계: n, 이전단계: p, 주문완료: f): ")

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(menus[current_category]):
                order[current_category].append(menus[current_category][index] )
                print(f"선택된 메뉴: {menus[current_category][index]}")
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")
        elif choice == 'f':
            break
        elif choice == 'n':
            if category_index < len(categories) - 1:
                category_index += 1
                current_category = categories[category_index]
        elif choice == 'p':
            if category_index > 0:
                category_index -= 1
                current_category = categories[category_index]
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
    # print('\n주문 내역:')
    # print(order)
    total_price = 0
    print("\n-----------")
    print("주문 내역")
    print("-----------")
    for category in categories:
        print(f"{category}: { ','.join(order[category] ) }" )
        for item in order[category]:
            item_idx = menus[category].index(item)
            total_price += prices[category][item_idx]

    print(f"총 금액: {total_price:,}원")
main()
        