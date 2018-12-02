import random

class Main():
    _your_name = "";
    _word_list = ["お腹空いた", "ピザ頼んで", "それ何？"];

    def __init__(self):
        global _your_name;

        print("girlfriend: あなたの名前、教えて？");
        _your_name = input("your_name: ");
        print("おはよ、" + _your_name);
        print("帰るときは『バイバイ』って言って。");

    def Response(self):
        while True:
            your_phrase = input("> ");
            if your_phrase == "バイバイ":
                print(_your_name + "、またね。");
                break;
            else:
                print(random.choice(self._word_list));

main = Main();
main.Response();
