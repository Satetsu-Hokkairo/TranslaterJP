import tkinter as tk
from tkinter import scrolledtext
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("翻訳アプリ")

        self.text_area = scrolledtext.ScrolledText(master, width=40, height=10, font=("Arial", 12))
        self.text_area.grid(column=0, row=0, padx=10, pady=10)

        self.find_text_label = tk.Label(master, text="翻訳する文字列:")
        self.find_text_label.grid(column=0, row=1, padx=10, pady=5)

        self.find_text_entry = tk.Entry(master)
        self.find_text_entry.grid(column=1, row=1, padx=10, pady=5)

        self.translate_button = tk.Button(master, text="翻訳", command=self.translate_text)
        self.translate_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        original_text = self.text_area.get("1.0", tk.END)
        find_txt = self.find_text_entry.get()

        # 検出した文字列の位置を取得
        find_index = original_text.find(find_txt)

        if find_index != -1:  # 文字列が見つかった場合
            text_to_translate = original_text[find_index + len(find_txt):].strip()

            if text_to_translate:  # 空でないテキストを翻訳
                translator = Translator()
                translated_text = translator.translate(text_to_translate, dest='ja').text

                # 翻訳したテキストを元のテキストに置き換える
                translated_full_text = original_text[:find_index + len(find_txt)] + translated_text
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, translated_full_text)
            else:
                print("翻訳するテキストがありません")
        else:
            print("指定された文字が見つかりませんでした")

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
