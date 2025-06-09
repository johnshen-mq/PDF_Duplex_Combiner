import os
import tkinter as tk
from tkinter import filedialog, messagebox

from main import merge_pdfs


class Tooltip:
    """Simple tooltip implementation for Tkinter widgets."""

    def __init__(self, widget: tk.Widget, text: str) -> None:
        self.widget = widget
        self.text = text
        self.tip_window: tk.Toplevel | None = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, _event=None) -> None:
        if self.tip_window:
            return
        x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5
        y = self.widget.winfo_rooty() + 5
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            font=("Helvetica", 9),
        )
        label.pack(ipadx=1)

    def hide(self, _event=None) -> None:
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


class PDFCombinerGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("PDF Duplex Combiner")

        self.odd_file: str | None = None
        self.even_file: str | None = None

        # Help information
        info_frame = tk.Frame(root)
        info_frame.pack(pady=5)
        tk.Label(info_frame, text="How to use (使用说明)").pack(side=tk.LEFT)
        info_icon = tk.Label(
            info_frame,
            text="?",
            fg="blue",
            font=("Helvetica", 14, "bold"),
            cursor="question_arrow",
        )
        info_icon.pack(side=tk.LEFT)
        Tooltip(
            info_icon,
            (
                "1. Place pages face up and scan to odd.pdf.\n"
                "2. Flip the stack (backs up) and scan again to even.pdf.\n"
                "3. Load both PDFs here to merge.\n\n"
                "1. 将文件正面朝上单面扫描保存为 odd.pdf。\n"
                "2. 把整叠纸翻面再次扫描保存为 even.pdf。\n"
                "3. 在此工具合并两份 PDF。"
            ),
        )

        # Odd file selection
        frame_odd = tk.Frame(root)
        frame_odd.pack(pady=10)
        odd_top = tk.Frame(frame_odd)
        odd_top.pack()
        self.odd_btn = tk.Button(odd_top, text="Select Odd Pages PDF", command=self.select_odd)
        self.odd_btn.pack(side=tk.LEFT)
        odd_canvas = tk.Canvas(odd_top, width=80, height=70, highlightthickness=0)
        odd_canvas.pack(side=tk.LEFT, padx=5)
        self.draw_icon(odd_canvas, [1, 3, 5])
        self.odd_label = tk.Label(frame_odd, text="")
        self.odd_label.pack()

        # Even file selection
        frame_even = tk.Frame(root)
        frame_even.pack(pady=10)
        even_top = tk.Frame(frame_even)
        even_top.pack()
        self.even_btn = tk.Button(even_top, text="Select Even Pages PDF", command=self.select_even)
        self.even_btn.pack(side=tk.LEFT)
        even_canvas = tk.Canvas(even_top, width=80, height=70, highlightthickness=0)
        even_canvas.pack(side=tk.LEFT, padx=5)
        self.draw_icon(even_canvas, [6, 4, 2])
        self.even_label = tk.Label(frame_even, text="")
        self.even_label.pack()

        # Combine button
        self.combine_btn = tk.Button(root, text="Combine Now", fg="white", command=self.combine)
        self.combine_btn.pack(pady=20)
        self.rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        self.rainbow_index = 0
        self.cycle_rainbow()

    def cycle_rainbow(self) -> None:
        """Cycle background color of the combine button."""
        color = self.rainbow_colors[self.rainbow_index]
        self.combine_btn.configure(bg=color)
        self.rainbow_index = (self.rainbow_index + 1) % len(self.rainbow_colors)
        self.root.after(500, self.cycle_rainbow)

    def draw_icon(self, canvas: tk.Canvas, numbers: list[int]) -> None:
        """Draw overlapping page icon with given numbers."""
        width, height = 50, 60
        offset = 8
        for idx, num in enumerate(numbers[::-1]):  # draw bottom first
            x = offset * idx
            y = offset * (len(numbers) - idx - 1)
            canvas.create_rectangle(x, y, x + width, y + height, fill="white", outline="black")
            canvas.create_text(
                x + width - 5,
                y + height - 5,
                text=str(num),
                font=("Helvetica", 12, "bold"),
                anchor="se",
            )

    def select_odd(self) -> None:
        self.odd_file = filedialog.askopenfilename(title="Select Odd Pages PDF", filetypes=[("PDF files", "*.pdf")])
        if self.odd_file:
            self.odd_btn.configure(bg="light green")
            self.odd_label.configure(text=os.path.basename(self.odd_file))

    def select_even(self) -> None:
        self.even_file = filedialog.askopenfilename(title="Select Even Pages PDF", filetypes=[("PDF files", "*.pdf")])
        if self.even_file:
            self.even_btn.configure(bg="light green")
            self.even_label.configure(text=os.path.basename(self.even_file))

    def combine(self) -> None:
        if not self.odd_file or not self.even_file:
            messagebox.showerror("Error", "Please select both PDF files.")
            return
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf", initialfile="Duplex.pdf", filetypes=[("PDF files", "*.pdf")]
        )
        if not output_file:
            return
        try:
            merge_pdfs(self.odd_file, self.even_file, output_file)
            messagebox.showinfo("Success", f"PDFs combined into {output_file}")
        except Exception as exc:
            messagebox.showerror("Error", f"Failed to merge PDFs: {exc}")


def main() -> None:
    root = tk.Tk()
    PDFCombinerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
