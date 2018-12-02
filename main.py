import random

class Main():
    PHRASE_PASS = 'phrase.txt';
    _your_name = "";
    _girlfriend_name = "girlfriend";
    _word_list = [];

    def __init__(self):
        global _word_list;
        with open(self.PHRASE_PASS) as f:
            _word_list = [s.strip() for s in f.readlines()];
        
    def SetName(self):
        global _your_name;
        print(self._girlfriend_name + ": あなたの名前、教えて？");
        _your_name = input("your_name: ");
        print(self._girlfriend_name + ": おはよ、" + _your_name);
        print(self._girlfriend_name + ": 帰るときは『バイバイ』って言って。");

    def Response(self):
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
                print(self._girlfriend_name + ": " + random.choice(_word_list));

    def LearnPhrase(self, your_phrase, your_phrase_sub):
        global _word_list;
        _word_list.append(your_phrase);
        f = open(self.PHRASE_PASS, "a");
        f.writelines(your_phrase);
        f.close();

main = Main();
main.SetName();
main.Response();
