import random
import json

class Main():
    PHRASE_PASS = 'phrase.json';
    _girlfriend_name = "girlfriend";
    _emotional_mode = "GOOD";
    _love_score = 0;
    _your_name = "";
    _word_list = [];

    def __init__(self):
        global _word_list;
        try:
            # ローカルJSONファイルの読み込み
            with open(self.PHRASE_PASS, 'r') as f:
                _word_list = json.load(f);
        except json.JSONDecodeError as e:
            print('JSONDecodeError: ', e);
        
    def SetName(self):
        global _your_name;
        print(self._girlfriend_name + ": あなたの名前、教えて？");
        _your_name = input("your_name: ");
        print(self._girlfriend_name + ": おはよ、" + _your_name);
        print(self._girlfriend_name + ": 帰るときは『バイバイ』って言って。");

    def Response(self):
        global _emotional_mode;
        while True:
            your_phrase = input("> ");
            is_what_mean = random.choice([True, False, False]);
            if your_phrase == "バイバイ":
                print(self._girlfriend_name + ": " + _your_name + "、またね。");
                break;
            elif is_what_mean:
                print(self._girlfriend_name + ": " + your_phrase + "ってなに？");
                your_phrase_sub = input("> ");
                self.LearnPhrase(your_phrase, your_phrase_sub);
                print(self._girlfriend_name + ": " + your_phrase_sub + "ってことなの？ふーん。");
            else:
                print(self._girlfriend_name + ": " + random.choice(_word_list[self._emotional_mode]));
            self.EmotionMoved(your_phrase);

    def LearnPhrase(self, your_phrase, your_phrase_sub):
        global _emotional_mode;
        global _word_list;
        _word_list[self._emotional_mode].append(your_phrase);
        with open(self.PHRASE_PASS, 'w') as outfile:
            json.dump(_word_list, outfile);

    def EmotionMoved(self, your_phrase):
        global _love_score;
        global _emotional_mode;
        if your_phrase in _word_list["GOOD"]:
            self._love_score += 1.0;
        elif your_phrase in _word_list["BAD"]:
            self._love_score -= 1.0;
        else:
            self._love_score += 0.5;
        print("現在の高感度: " + str(self._love_score));
        if self._love_score > 0:
            self._emotional_mode = "GOOD";
        else:
            self._emotional_mode = "BAD";


main = Main();
main.SetName();
main.Response();
