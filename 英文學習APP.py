from flask import Flask, jsonify, send_from_directory
import random

app = Flask(__name__, static_folder=".", static_url_path="")

# ===== 題庫資料（原本在 HTML 裡的 database）=====
database = [
    {"q": "我對這份工作感興趣。", "a": ["I", "am", "interested", "in", "this", "job"]},
    {"q": "天氣今天很好。", "a": ["The", "weather", "is", "nice", "today"]},
    {"q": "我喜歡學習新事物。", "a": ["I", "like", "learning", "new", "things"]},
    {"q": "他在這家公司工作。", "a": ["He", "works", "at", "this", "company"]},
    {"q": "這本書非常有趣。", "a": ["This", "book", "is", "very", "interesting"]},
    {"q": "我們明天去公園吧。", "a": ["Let's", "go", "to", "the", "park", "tomorrow"]},
    {"q": "妳想要喝咖啡嗎？", "a": ["Do", "you", "want", "to", "drink", "coffee"]},
    {"q": "我迷路了。", "a": ["I", "am", "lost"]},
    {"q": "請幫我一下。", "a": ["Please", "help", "me"]},
    {"q": "我很高興見到你。", "a": ["I", "am", "glad", "to", "see", "you"]},
    {"q": "他跑得很快。", "a": ["He", "runs", "very", "fast"]},
    {"q": "現在幾點了？", "a": ["What", "time", "is", "it", "now"]},
    {"q": "這份沙拉很好吃。", "a": ["This", "salad", "tastes", "good"]},
    {"q": "你家在哪裡？", "a": ["Where", "is", "your", "house"]},
    {"q": "我忘記帶鑰匙了。", "a": ["I", "forgot", "to", "bring", "keys"]},
    {"q": "這是一支新手機。", "a": ["This", "is", "a", "new", "phone"]},
    {"q": "天快黑了。", "a": ["It", "is", "getting", "dark"]},
    {"q": "這是我第一次來這裡。", "a": ["This", "is", "my", "first", "time", "here"]},
    {"q": "音樂很大聲。", "a": ["The", "music", "is", "very", "loud"]},
    {"q": "我需要多點時間。", "a": ["I", "need", "more", "time"]},
    {"q": "這是一個秘密。", "a": ["This", "is", "a", "secret"]},
    {"q": "你準備好了嗎？", "a": ["Are", "you", "ready"]},
    {"q": "這條路通往哪裡？", "a": ["Where", "does", "this", "road", "lead"]},
    {"q": "門是鎖著的。", "a": ["The", "door", "is", "locked"]},
    {"q": "他在睡覺。", "a": ["He", "is", "sleeping"]},
    {"q": "我有一隻貓。", "a": ["I", "have", "a", "cat"]},
    {"q": "電影快開始了。", "a": ["The", "movie", "is", "starting", "soon"]},
    {"q": "蘋果是紅色的。", "a": ["Apples", "are", "red"]},
    {"q": "你在做什麼？", "a": ["What", "are", "you", "doing"]},
    {"q": "謝謝你的幫忙。", "a": ["Thank", "you", "for", "your", "help"]},
    {"q": "這件衣服很適合你。", "a": ["This", "outfit", "suits", "you", "well"]},
    {"q": "明天會下雨。", "a": ["It", "will", "rain", "tomorrow"]},
    {"q": "我正在吃午飯。", "a": ["I", "am", "having", "lunch"]},
    {"q": "那隻狗在叫。", "a": ["That", "dog", "is", "barking"]},
    {"q": "我很累。", "a": ["I", "am", "very", "tired"]},
    {"q": "太陽升起來了。", "a": ["The", "sun", "is", "rising"]},
    {"q": "這雙鞋太小了。", "a": ["These", "shoes", "are", "too", "small"]},
    {"q": "請關掉燈。", "a": ["Please", "turn", "off", "the", "light"]},
    {"q": "她在彈鋼琴。", "a": ["She", "is", "playing", "the", "piano"]},
    {"q": "我不明白。", "a": ["I", "do", "not", "understand"]},
    {"q": "這是一個好主意。", "a": ["That", "is", "a", "good", "idea"]},
    {"q": "別擔心。", "a": ["Do", "not", "worry"]},
    {"q": "水很涼快。", "a": ["The", "water", "is", "cool"]},
    {"q": "他在學校。", "a": ["He", "is", "at", "school"]},
    {"q": "你想去哪裡？", "a": ["Where", "do", "you", "want", "to", "go"]},
    {"q": "這花很香。", "a": ["This", "flower", "smells", "sweet"]},
    {"q": "我感冒了。", "a": ["I", "have", "a", "cold"]},
    {"q": "火車站很遠。", "a": ["The", "train", "station", "is", "far"]},
    {"q": "那是我的朋友。", "a": ["That", "is", "my", "friend"]},
    {"q": "今天是星期一。", "a": ["Today", "is", "Monday"]}
]

# ===== API =====
@app.route("/api/questions")
def get_questions():
    return jsonify(database)

# ===== 開啟 HTML =====
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
  
