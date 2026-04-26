from http import HTTPStatus
import dashscope

dashscope.api_key = "your_api_key_here"

def cot_test():
    # 普通提问（容易算错）
    prompt_normal = "一个玩家初始有100点生命值，被攻击两次，每次掉20点血，他还剩多少血？"
    # 零样本CoT提问（加引导词，让模型分步思考）
    prompt_cot = "一个玩家初始有100点生命值，被攻击两次，每次掉20点血，他还剩多少血？Let's think step by step."
    
    # 先跑普通提问
    print("--- 普通提问结果 ---")
    resp1 = dashscope.Generation.call(model='qwen-turbo', prompt=prompt_normal)
    if resp1.status_code == HTTPStatus.OK:
        print(resp1.output.text)
    
    # 再跑CoT提问
    print("\n--- 零样本CoT结果 ---")
    resp2 = dashscope.Generation.call(model='qwen-turbo', prompt=prompt_cot)
    if resp2.status_code == HTTPStatus.OK:
        print(resp2.output.text)

cot_test()

