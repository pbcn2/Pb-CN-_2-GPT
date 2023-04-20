
# API-Key:   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

# Free API-Key:   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

import openai
import csv


def askChatGPT(messages, api_key):
    MODEL = "gpt-3.5-turbo"
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1)
    return response['choices'][0]['message']['content']


def save_dict_list_to_csv(dict_list, filename):
    """
    将字典列表保存为CSV文件
    dict_list: 字典列表
    filename: 文件名
    """
    with open(filename, mode='w', newline='') as f:
        fieldnames = list(dict_list[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for my_dict in dict_list:
            writer.writerow(my_dict)


def authentication():
    while True:
        is_guest = input("Are you a guest? (y/n) (or 'q' to quit): ")
        if is_guest.lower() == "y":
            # 访客的情况
            while True:
                api_key = input("Please enter your api key (or 'q' to quit): ")
                if api_key.lower() == "q":
                    return 666
                else:
                    return api_key
        elif is_guest.lower() == "n":
            # 非访客的情况
            while True:
                system_key = input("Please enter the system key (or 'q' to quit): ")
                if system_key.lower() == "q":
                    return 666
                # 在这里添加验证系统密钥的代码
                elif system_key.lower() == "admin":
                    print("Authentication successful.")
                    return 1
                else:
                    print("Invalid system key.")
        elif is_guest.lower() == "q":
            return 666
        else:
            print("Invalid input. Please enter 'y' or 'n' (or 'q' to quit).")


def admin_chat():
    messages = [{"role": "system", "content": "hello"}]
    # api_key =
    while 1:
        try:
            text = input('You: \n-------------\n')
            if text == 'quit':
                break
            d = {"role": "user", "content": text}
            messages.append(d)
            text = askChatGPT(messages, api_key="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")
            d = {"role": "assistant", "content": text}
            print('PbCN_2-GPT (model: GPT-3.5-turbo): \n-----------------------------------\n' + text + '\n')
            messages.append(d)
        except:
            messages.pop()
            print('Error: Please check the network!\n')
    save_dict_list_to_csv(messages, "message_log.csv")


def user_chat(api_key):
    messages = [{"role": "system", "content": "hello"}]
    while 1:
        try:
            text = input('You: \n-------------\n')
            if text == 'quit':
                break
            d = {"role": "user", "content": text}
            messages.append(d)
            text = askChatGPT(messages, api_key)
            d = {"role": "assistant", "content": text}
            print('PbCN_2-GPT (model: GPT-3.5-turbo): \n-----------------------------------\n' + text + '\n')
            messages.append(d)
        except:
            messages.pop()
            print('Error: Please check the network!\n')
    save_dict_list_to_csv(messages, "message_log.csv")


def exit_function():
    print("\n********************************")
    print("# Thanks for using the program")
    print("Copyright © 2023 Nick Chin.")
    print("All rights reserved.")
    print("# Special thanks to:")
    print("- My Family")
    print("- My Friends")
    print("********************************")


def main():
    result = authentication()
    print()
    if result == 666:
        exit_function()
        return
    elif result == 1:
        admin_chat()
        exit_function()
        return
    else:
        user_chat(result)
        exit_function()
        return


main()
input("Press <enter>")