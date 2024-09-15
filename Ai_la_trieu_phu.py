import random

_PATH = "C:/Users/Dell/Documents/.vscode/Du_An_Cuoi_Hoc_ Ki1"

question_list = "Questions list.txt"
answers_list = "Answers list.txt"
Prize_list = "Prize.txt"

Question = _PATH + '/' + question_list
Answers = _PATH + '/' + answers_list
Prize = _PATH + '/' + Prize_list

with open(Question, 'r', encoding='utf-8') as f:
    question = f.readlines()

with open(Prize, 'r', encoding='utf-8') as f:
    prize = f.readlines()

with open(Answers, 'r', encoding='utf-8') as f:
    answers = f.readlines()

def use_fifty_fifty(correct_answer_index):
    print("Sử dụng tính năng 50-50...")
    # Tạo danh sách các chỉ số lựa chọn
    all_answers = list(range(len(answers)))
    
    # Loại bỏ câu trả lời đúng khỏi danh sách
    all_answers.remove(correct_answer_index)
    
    # Chọn một trong các lựa chọn sai
    wrong_answer = random.choice(all_answers)  # Chọn ngẫu nhiên một lựa chọn sai

    print("Các lựa chọn còn lại:")
    print(f"1: {answers[correct_answer_index].strip()}")  # Câu trả lời đúng
    print(f"2: {answers[wrong_answer].strip()}")          


def use_ask_audience(correct_answer_index):
    print("Hỏi khán giả...")
    main_answer1 = answers[correct_answer_index].strip()
    main_answers = random.randint(40, 100)
    Answer1 = random.randint(0, 100 - main_answers)
    Answer2 = random.randint(0, 100 - (main_answers + Answer1))
    Answer3 = 100 - (main_answers + Answer1 + Answer2)
    a = [main_answer1]
    Random1 = chr(random.randint(65, 68))
    while Random1 in a:
        Random1 = chr(random.randint(65, 68))
    a.append(Random1)

    Random2 = chr(random.randint(65, 68))
    while Random2 in a:
        Random2 = chr(random.randint(65, 68))
    a.append(Random2)

    Random3 = chr(random.randint(65, 68))
    while Random3 in a:
        Random3 = chr(random.randint(65, 68))
    a.append(Random3)

    print(f"{Random1}: {Answer1}%")
    print(f"{Random2}: {Answer2}%")
    print(f"{Random3}: {Answer3}%")
    print(f"{main_answer1}: {main_answers}%")


def main():
    score = 0
    # Xáo trộn danh sách câu hỏi
    question_indices = list(range(len(question)))
    random.shuffle(question_indices)
    used_fifty_fifty = False
    used_ask_audience = False
    Answer = ["A", "B", "C", "D"]

    for i in range(len(question_indices)):
        if i >= 15: 
            print("Cảm ơn bạn đã chơi! Bạn đã trả lời đủ 15 câu hỏi.")
            print("Giải thưởng của bạn là:", prize[15])
            break

        current_question = question_indices[i]
        
        while True:  # Vòng lặp để đảm bảo người chơi chọn một tùy chọn hợp lệ
            print(f"\nCâu hỏi {i + 1}: {question[current_question].strip()}")
            print("Chọn một trong các chức năng trợ giúp:")
            if not used_fifty_fifty:
                print("1. 50-50")
            if not used_ask_audience:
                print("2. Hỏi khán giả")
            print("3. Trả lời câu hỏi")
            
            user_choice = input("Nhập lựa chọn của bạn (1-3): ")

            if user_choice == "1" and not used_fifty_fifty:
                use_fifty_fifty(current_question)
                used_fifty_fifty = True
                user_answer = input("Câu trả lời của bạn: ")
                while user_answer.upper() not in Answer:
                    user_answer = input("Câu trả lời của bạn: ")
                if user_answer.strip().lower() == answers[current_question].strip().lower():
                    print(f"Chúc mừng! Bạn đã trả lời đúng. Giải thưởng là: {prize[i].strip()}")
                    score += 1
                    A = input("Bạn có muốn dừng cuộc chơi không? (yes or no): ")
                    if A.lower() == "yes":
                        print("Giải thưởng của bạn là:", prize[i].strip())
                        return score  # Kết thúc trò chơi
                else:
                    print(f"Rất tiếc, câu trả lời của bạn không đúng. Đáp án đúng là: {answers[current_question].strip()}")
                    if i >= 1:
                        print("Bạn nhận đc", prize[0])
                    else:
                        print("Bạn không nhận được giải thưởng lêu lêu")
                    return score  # Kết thúc trò chơi
                break  # Thoát khỏi vòng lặp nếu đã trả lời câu hỏi

            elif user_choice == "2" and not used_ask_audience:
                use_ask_audience(current_question)
                used_ask_audience = True
                user_answer = input("Câu trả lời của bạn: ")
                while user_answer.upper() not in Answer:
                    user_answer = input("Câu trả lời của bạn: ")
                if user_answer.strip().lower() == answers[current_question].strip().lower():
                    print(f"Chúc mừng! Bạn đã trả lời đúng. Giải thưởng là: {prize[i].strip()}")
                    score += 1
                    A = input("Bạn có muốn dừng cuộc chơi không? (yes or no): ")
                    if A.lower() == "yes":
                        print("Giải thưởng của bạn là:", prize[i].strip())
                        return score  # Kết thúc trò chơi
                else:
                    print(f"Rất tiếc, câu trả lời của bạn không đúng. Đáp án đúng là: {answers[current_question].strip()}")
                    if i >= 1:
                        print("Bạn nhận đc", prize[0])
                    else:
                        print("Bạn không nhận được giải thưởng lêu lêu")
                    return score  # Kết thúc trò chơi
                break  # Thoát khỏi vòng lặp nếu đã trả lời câu hỏi
            elif user_choice == "3":
                user_answer = input("Câu trả lời của bạn: ")
                while user_answer.upper() not in Answer:
                    user_answer = input("Câu trả lời của bạn: ")
                if user_answer.strip().lower() == answers[current_question].strip().lower():
                    print(f"Chúc mừng! Bạn đã trả lời đúng. Giải thưởng là: {prize[i].strip()}")
                    score += 1
                    A = input("Bạn có muốn dừng cuộc chơi không? (yes or no): ")
                    if A.lower() == "yes":
                        print("Giải thưởng của bạn là:", prize[i].strip())
                        return score  # Kết thúc trò chơi
                else:
                    print(f"Rất tiếc, câu trả lời của bạn không đúng. Đáp án đúng là: {answers[current_question].strip()}")
                    if i >= 1:
                        print("Bạn nhận đc", prize[0])
                    else:
                        print("Bạn không nhận được giải thưởng lêu lêu")
                    return score  # Kết thúc trò chơi
                break  # Thoát khỏi vòng lặp nếu đã trả lời câu hỏi
            else:
                print("Lựa chọn không hợp lệ hoặc đã sử dụng. Vui lòng thử lại.")  # Thông báo lỗi
    return score

final_score = main()
print(f"Bạn đã trả lời đúng {final_score} câu hỏi.")
print("Cảm ơn bạn đã chơi trò chơi!")