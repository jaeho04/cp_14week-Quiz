menus = ["냉면", "볶음밥", "피자", "짜장면"]
def select_menu():
  try:
    menu_num = int(input("메뉴 번호를 입력하세요 (1~4): "))

    if 1 <= menu_num <= 4:
      print(f"선택하신 메뉴는 {menus[menu_num - 1]}입니다.")
    else:
      raise ValueError("메뉴 번호가 유효하지 않습니다.")
  except ValueError as e:
    print(f"오류: {e}")
    print("숫자를 다시 입력하세요.")
  except IndexError as e:
    print(f"오류: {e}")
    print("메뉴 번호 범위를 벗어났습니다. 다시 입력하세요.")

while True:
  select_menu()

  again = input("다시 주문하시겠습니까? (예/아니요): ")
  if again.lower() != "예":
    break

print("프로그램 종료")