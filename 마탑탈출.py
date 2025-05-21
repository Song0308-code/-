from typing import Set
import sys
import time

class Player:
    

    MAX_HP = 100
    MAX_MP = 50

    def __init__(self):
        self.hp: int = Player.MAX_HP
        self.mp: int = Player.MAX_MP
        self.items: Set[str] = set()          # 아이템 저장용
        self.weapon: str | None = None        # 무기 저장
        # story flags
        self.knows_truth: bool = False        # set after drinking the truth potion
        self.seen_researcher: bool = False    # met researcher first time

#게임 구성용 ADT
    def change_hp(self, delta: int) -> None:
        self.hp = max(0, min(Player.MAX_HP, self.hp + delta))
        print(f"[체력] {delta:+} → {self.hp}")
        if self.hp == 0:
            print("\n◆ 당신은 쓰러졌습니다… (배드엔딩) ◆")

    def change_mp(self, delta: int) -> None:
        self.mp = max(0, self.mp + delta)
        print(f"[정신력] {delta:+} → {self.mp}")
        
            

    def has(self, item: str) -> bool:
        return item in self.items

    def add(self, *item_names: str) -> None:
        for it in item_names:
            self.items.add(it)

#----------------class 외의 함수---------
def combat_weapon(p: Player) -> str:
    if p.weapon == "dagger":
        return "단검"
    elif p.weapon == "bow":
        return "활"
    else:
        return "지팡이"


def end_game(p: Player):
    print("\n게임이 종료되었습니다. 플레이해주셔서 감사합니다!")
    sys.exit()


# ------------- 게임 루프 -------------

def main():
    p = Player()
    turn = 1

    while True:
        if p.hp == 0:
            end_game(p)

        # ----- 턴별 분기 -----
        if turn == 1:
            print("\n── 1턴 : 감옥에서 깨어나다 ──")
            print("눈을 떠보니 당신은 감옥 안에 갇혀 있습니다. 머릿속에는 당신이 어떤 사람인지 어떠한 정보도 남아있는 않는 상태로, 다행히도 손발은 어딘가에 묶여 있지 않은채 자유롭습니다.")
            print("  1. 감옥 안을 조사한다")
            print("  2. 살려달라고 소리를 지른다")
            print("  3. 가만히 있는다")
            choice = int(input(">> "))
            if choice == 1:
                print("열쇠 꾸러미를 발견했습니다! 어딘가에 쓸 수 있겠네요.")
                time.sleep(2)
                p.add("key_ring")
                turn = 2
            elif choice == 2:
                print("경비에게 들켜 폭행당했습니다! 그러나 경비가 열쇠를 흘리고 갔습니다…(체력 -10)")
                time.sleep(2)
                p.change_hp(-10)
                p.add("key")
                turn = 2
            else:
                print("…아무 일도 일어나지 않았습니다.")#1턴 반복
                

        elif turn == 2:
            print("\n── 2턴 : 탈출 시도 ──")
            print("어찌됐든 당신은 탈출을 시도해보기로 합니다.")
            print("  1. 문을 연다")
            print("  2. 경비 여부를 확인한다")
            print("  3. 포기하고 앉아있다")
            choice = int(input(">> "))
            if choice == 1 and (p.has("key") or p.has("key_ring")):
                print("문이 열렸습니다! 하지만 당신의 소리를 들은 듯 합니다. 당신은 있는 힘껏 그들에게서 도망칩니다(체력 -10)")
                time.sleep(2)
                p.change_hp(-10)
                turn = 3
            elif choice == 2 and (p.has("key") or p.has("key_ring")):
                print("경비들이 시야에 보이지 않습니다. 어쩐지 경비를 살피는 자신이 익숙한 느낌이 듭니다.")
                print("문을 열고 조심스럽게 나갑니다. 혹시.. 이번 탈출이 처음이 아닌걸까요?(정신력 -10)")
                time.sleep(2)
                p.change_mp(-10)
                turn = 3
            elif choice == 3:
                print("시간만 흐를 뿐…")
                # stay in turn 2
            else:
                print("그럴 수 없습니다.")
                # stay

        elif turn == 3:
            print("\n── 3턴 : 복도 ──")
            print("당신은 감옥에서 나와 조심히 복도로 이동합니다. 복도는 어둡고 스산합니다.")
            print("살금살금 걸어가던 도중 생명체의 인기척이 느껴집니다!")
            print("이대로 잡힐 수 없는 당신은 주위에 보이는 방중 한곳에 들어가기로합니다. 어느곳에 들어가겠습니까?")
            print("  1. 빨간색 문")
            print("  2. 파란색 문")
            print("  3. 검정색 문")
            choice = int(input(">> "))
            if choice == 1:
                print("활기가 솟구칩니다! (체력 +10)")
                p.change_hp(10)
            elif choice == 2:
                print("잠시 휴식을 취합니다. (체력 +5)")
                p.change_hp(5)
            else:
                print("케로베로스를 만났습니다. 왜인지 케르베로스가 친근함을 표시합니다. \n그는 왜 당신에게 친근함을 표했을까요?(정신력 -10)")
                p.change_mp(-10)
            time.sleep(2)
            turn = 4

        elif turn == 4:
            print("\n── 4턴 : 낡은 방 ──")
            print("한참을 헤매다 당신은 낡은 방에 진입합니다. 방안은 한참동안 사람의 손을 타지 않았는지 먼지가 날립니다.")
            print("이 낡은 방에서 무엇인가를 찾을 수 있을 것 같던 당신은 방을 살펴보기로 합니다.")
            print("  1. 일지를 읽는다")
            print("  2. 메모를 본다")
            print("  3. 알 수 없는 물약을 마신다")
            choice = int(input(">> "))
            if choice == 1:
                print("\"실헙체 SM-25의 탈출 시도 12번째.\n본인 스스로 기억을 잃었음에도 반복적으로 비슷한 경로로 탈출을 시도하고있음.\n'기억'이 제거된후에도 이와같은 행동 패턴을 보이는 것은 주목할만하다.\"") #히든 엔딩 암시
                print("알수 없는 일지지만 왜인지 머리가 아파옵니다.(정신력 -10)")
                
                p.change_mp(-10)
            elif choice == 2:
                print("\"도대체 언제까지 이짓을 계속해야 하는가. 그는 몇번을 반복해도 끝까지 나아가려 한다.\n이번에는 부디.. 끝까지 가기를 바란다. 이 메모가 그에게 닿을지는 모르겠지만...\"")
                print("누군가의 깊은 고뇌가 느껴집니다. 알 수 없지만 머리가 아파옵니다.(정신력 -10)")
                p.change_mp(-10)
            else:
                print("속이 울렁거리고 머리가 깨질듯이 아파옵니다. 당신은 한참 그자리에서 주저 앉았습니다. (체력 -10)")
                p.change_hp(-10)
            time.sleep(2)
            turn = 5

        elif turn == 5:
            print("\n── 5턴 : 무기고 발견 ──")
            print("  1. 단검")
            print("  2. 활")
            print("  3. 지팡이")
            choice = int(input(">> "))
            weapons = ["dagger", "bow", "staff"]
            p.weapon = weapons[choice - 1]
            p.add("weapon")
            print(f"{['단검','활','지팡이'][choice-1]}를 얻었습니다! 체력 +5")
            p.change_hp(5)
            time.sleep(2)
            turn = 6

        elif turn == 6:
            print("\n── 6턴 : 수상한 인물 ──")
            print("당신은 하얀 가운을 입을 사람을 발견했습니다. 아마도 이곳의 연구원인 듯 합니다.")
            print("이곳에 왜 연구원이 있을까요?")
            print("  1. 말을 건다")
            print("  2. 숨는다")
            print("  3. 먼저공격한다")
            choice = int(input(">> "))
            if choice == 1:
                p.seen_researcher = True
                print("\"아니 어떻게 당신이 이곳까지...\"")
                
                print("당신을 구석진 곳으로 데려가 종이 한장과 물을 건내어줍니다.")
                
                print("\"제가 해드릴 수 있는건 없고.. 이거라도 가져가세요. 그리고 이번에는 꼭... 성공하시길..\"")
                
                print("당신이 뭐라고 대답하기도 전에 연구원은 사라졌습니다. 당신은 묘한 기분으로 걸음을 다시 재촉합니다.")
                
                print("어쩐지 연구원이 익숙한 기분입니다.(정신력 -10)(종이 획득)")
                
                p.change_mp(-10)
                p.add("paper")
            elif choice == 3:
                print("연구원을 공격했습니다. 마음이 불편합니다. 그래도.. 탈출을 위하여 어쩔 수 없겠죠?")
                p.change_mp(-5)
            else:
                print("연구원이 사라질 때까지 숨었습니다… 아무 일도 일어나지 않았습니다.")
            time.sleep(2)
            turn = 7

        elif turn == 7:
            print("\n── 7턴 : 퍼즐을 맞닥뜨리다  ──")
            print("앞으로 더 나아가려면 비밀번호를 입력해야 나아갈 수 있는 문을 발견합니다.")
            print("  1. 쓸만한 도구가 있는지 주머니를 뒤져 본다.")
            print("  2. 문을 부순다")
            choice = int(input(">> "))
            if choice == 1 and p.has("paper"):
                print("당신은 문득 아까 연구원이 줬던 종이가 생각나 살펴봅니다.")
                print("종이에 적혀있는 비밀번호를 입력했더니 조용히 문이 열렸습니다.")
            
            else:
                print("사용할 만한 도구는 없는 것 같습니다. 어쩔 수 없이 당신은 문을 무력으로 부수는것을 선택합니다.")
                print("문을 힘으로 부숩니다! 체력 -20")
                p.change_hp(-20)
            time.sleep(2)
            turn = 8

        elif turn == 8:
            print("\n── 8턴 : 경비병과 마주침 ──")
            print("  1. 싸운다")
            print("  2. 회피한다")
            choice = int(input(">> ")) #무기사용 부분
            print(f"{combat_weapon(p)}(으)로 간단히 제압했습니다. 체력 -5") if choice == 1 else print("교묘히 피해 달아났습니다. 체력 -5")   #무기 활용 구문 고치기 필요
            p.change_hp(-5)
            time.sleep(2)
            turn = 9

        elif turn == 9:
            print("\n── 9턴 : 연구원과 재회 ──")
            print("당신은 아까 마주쳤던 연구원을 다시 만나게 됩니다.")
            print("  1. 대화한다")
            print("  2. 무시하고 지나친다")
            choice = int(input(">> "))
            if choice == 1:
                p.seen_researcher = True
                print("당신을 마주한 연구원이 다시한번 놀랍니다.")
                print("\"여기까지 오셨다면, 이번에는 보여드려도 괜찮겠군요\"")
                
                print("연구원이 무엇인가를 다짐했다는 듯 당신을 데리고 자신의 연구실로 향합니다. 의문을 가득 담은채로 당신은 연구원을 따라갑니다.")
                time.sleep(2)
                turn = 10
            else:
                print("그는 적대적으로 보이진 않지만, 아직 이 안에서 경계심을 풀 수는 없습니다.\n당신은 그냥 조용히 지나가기로 합니다.")
                time.sleep(2)
                turn = 10.5  # 10턴 패스

        elif turn == 10: #9턴에서 연구원과 대화한 경우에만 작용(히든엔딩)
            print("\n── 10턴 : 기억을 찾아서 ──")
            print("연구원이 당신에게 서류 더미를 건네줍니다. 당신의 정보를 시작하여, 수차례 진행된 실험 결과들")
            print("그리고 당신의 탈출 기록들... 영문을 모른채 당황하는 당신에게 연구원이 투명한 색깔의 물약을 전해줍니다")
            print("\"이 약을 먹으면 모든 것을 알 수 있을 것이에요. 선택은 당신의 몫입니다. 어떻게 하실건가요?\"")
            print("  1. 약을 마신다")
            print("  2. 마시지 않는다")
            choice = int(input(">> "))
            if choice == 1:
                print("잊고 있던 그 동안의 모든 일들이 머릿속으로 펼쳐집니다.")
                print("당신은 수년간 이 탑에서 마탑의 주인에게서 실험을 당한 실험체이며, 탈출을 여러번 시도했다는 것.")
                print("그리고 애초에 실험의 성공을 원했던 마탑의 주인은 당신의 탈출을 흥미롭게 지켜보고 있던 것.")
                print("이로서 당신은 케르베로스의 친근함과 일지의 내용과 연구원의 행동까지 모든 것이 이해가 가기 시작됩니다.")
                print("(정신력 -10)")
                p.change_mp(-10)
                time.sleep(2)
                print("그리고는 연구원이 주사기 하나를 건내준다.")
                print("\"기회는 단 한번 뿐이에요. 이 주사기로 마탑의 주인을 끝내주세요..!\"")
                print("(주사기 획득)")
                p.knows_truth = True
                p.add("syringe")
            else:
                print("…연구원은 씁쓸히 고개를 끄덕입니다.")
            time.sleep(2)
            turn = 11

        elif turn == 10.5: #연구원 대화 놓쳤을때 오는 턴
            print("\n── 10턴 : 허전한 전진 ──")
            print("뭔가 놓친 것 같은 기분이 듭니다…")
            time.sleep(2)
            turn = 11

        elif turn == 11:
            print("\n── 11턴 : 최종 층 ──")
            if p.knows_truth :
                print("마탑의 주인이 당신을 반깁니다. 실험은 성공이라며 동맹을 제안합니다.")
            else:
                print("거대한 존재가 길을 막습니다! 힘겨운 전투 끝에 마탑의 주인을 처치하는데 성공했습니다. (체력 -70)")
                p.change_hp(-70)
            turn = 12

        elif turn == 12:
            print("\n── 12턴 : 당신의 선택 ──")
            if p.hp == 0:
                
                print("◆ 배드엔딩: 탈진 ◆")
                print("마탑의 주인을 처치하는데는 성공했지만 결국 탈출에는 성공하지 못했다..")
                end_game(p)

            if p.knows_truth :
                print("  1. 동맹을 맺는다")
                print("  2. 주사기로 끝낸다")
                choice = int(input(">> "))
                if choice == 1:
                    print("◆── 히든엔딩1 ──◆")
                    print("당신은 마탑의 주인의 동맹을 받아드렸습니다. 마탑 주인의 호탕한 웃음소리가 울려퍼집니다.\n")
                    print("앞으로 당신은 새로운 길에 들어설 것입니다. 뭐.. 당신만 만족한다면 상관 없지 않을까요?")
                    
                else:
                    print("◆── 히든엔딩2 ──◆")
                    print("당신은 마탑 주인의 악행을 자기 손으로 끊는 것이 맞다 생각하며\n모든 힘을 다해 주사기를 꽂아 넣습니다.")
                    print("마탑주인은 고통스러워하며 서서히 가루로 변해갑니다. 이로서 그의 악행은 끝났습니다.")
                    print("당신은 개운한 마음과 함께 새출발을 합니다.")
                    
            else:
                if p.seen_researcher:
                    print("◆ 해피?엔딩: 찝찝한 탈출 ◆")
                else:
                    print("◆ 노말엔딩: 탈출 성공◆")
            time.sleep(4)
            end_game(p)


main()
