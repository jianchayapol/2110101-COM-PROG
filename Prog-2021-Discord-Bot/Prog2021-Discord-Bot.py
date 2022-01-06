import discord
import math
import random
import json

with open('config.json') as json_file:
    TOKEN = json.load(json_file)['DISCORD_TOKEN']
client = discord.Client()

random.seed(1111)
exam_info = []
all_questions = ['HW1 ถึง HW7 อันไหนยากสุด', 'คิดว่าจะได้เกรดอะไร', 'TA/อาจารย์ คนไหนอธิบายได้เข้าใจง่ายที่สุด', 'การบ้านไหนที่ชอบที่สุด', 'TA คนไหนตอบคุณเยอะสุด']
all_questions.sort()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    msg = message.content
    uid = message.author.id
    if msg.startswith('.sign_in'):
        sign_in(uid, msg.split()[1], exam_info)
        await message.author.send(get_welcome_and_rules_msg())
        await message.author.send(get_question(uid, exam_info, all_questions) + " --> ")
    elif msg.startswith('.answer'):
        submit_answer(uid, " ".join(msg.split()[1:]), exam_info)
        info = get_student_info(uid, exam_info)
        for i in range(len(info[3])):
            await message.a     uthor.send(info[2][i] + " --> " + info[3][i])
        question = get_question(uid, exam_info, all_questions)
        if question != "end":
            question += " -->"
        await message.author.send(question)
        
def sign_in(uid, sid, exam_info):
    for info in exam_info:
        if info[0]==uid or info[1]==sid: return
    exam_info.append([uid, sid, [], [], 0])
    return     

def get_welcome_and_rules_msg():
    text_out = "ยินดีต้อนรับสู่การสอบกลางภาค  \n วิชา 2110101 Computer Programming ครับ"
    return text_out  

def get_student_info(uid, exam_info):
    for info in exam_info:
        if info[0]==uid: return info
    return     

def get_question(uid, exam_info, all_questions):
    info = get_student_info(uid,exam_info)
    temp = []
    if len(info[2])<=info[4] and len(info[2])!=len(all_questions):
        for e in all_questions:
            if e not in info[2]: temp.append(e)
        q_rand = random.choice(temp)
        info[2].append(q_rand)
        return q_rand
    return "end"

def submit_answer(uid, answer, exam_info):
    info = get_student_info(uid,exam_info)
    info[3].append(answer)
    info[4]+=1
    return     

client.run(TOKEN)

