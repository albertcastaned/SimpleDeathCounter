from ast import parse
from typing import Union
import tkinter as tk
import sys

class Main():
    def parse_file(self) -> Union[int, None]:
        try:
            file = open(self.file_path, "r")
            text = file.read()
            clean = text.replace(" ", "")
            split = clean.split(":")
            result = split[1]
            file.close()
            return result
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def save_file(self) -> bool:
        try:
            file = open(self.file_path, "w")
            file.write(f"Deaths: {self.deaths}")
            file.close()
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def deaths_label(self, deaths: int) -> str:
        return f"Deaths: {deaths}"

    def substract(self) -> None:
        self.deaths -= 1
        self.save_file()
        self.label.configure(
            text=self.deaths_label(self.deaths)
        )

    def add(self) -> None:
        self.deaths += 1
        self.save_file()
        self.label.configure(
            text=self.deaths_label(self.deaths)
        )


    def __init__(self, root, file) -> None:
        self.file_path = file
        parsed = self.parse_file()
        if parsed:
            self.deaths : int = int(parsed)
        else:
            self.deaths : int = 0

        root.geometry("400x200")
        left_btn = tk.Button(
            root,
            text = '-',
            command=self.substract,
        )

        self.label = tk.Label(
            root,
            text=self.deaths_label(self.deaths),
        )
        self.label.config(
            fg="white",
        )

        right_btn = tk.Button(
            root,
            text = '+',
            command=self.add,
        )

        left_btn.grid(column=0, row=0)
        self.label.grid(column=1, row=0)
        right_btn.grid(column=2, row=0)

if __name__ == "__main__":
    root =  tk.Tk()
    if not len(sys.argv) == 2:
        print("Usage: app.py [filedir]")
    else:
        file_dir = sys.argv[1]
        print(f"Using file: {file_dir}")
        root.title(f"Death counter [{file_dir}]")

        Main(root, file_dir)
        root.mainloop()