import tkinter as tk
from tkinter import filedialog, messagebox

from main import merge_pdfs


class PDFCombinerGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("PDF Duplex Combiner")

        self.odd_file: str | None = None
        self.even_file: str | None = None

        # Odd file selection
        frame_odd = tk.Frame(root)
        frame_odd.pack(pady=10)
        self.odd_btn = tk.Button(frame_odd, text="Select Odd Pages PDF", command=self.select_odd)
        self.odd_btn.pack(side=tk.LEFT)
        odd_canvas = tk.Canvas(frame_odd, width=60, height=60, highlightthickness=0)
        odd_canvas.pack(side=tk.LEFT, padx=5)
        self.draw_icon(odd_canvas, [1, 3, 5])

        # Even file selection
        frame_even = tk.Frame(root)
        frame_even.pack(pady=10)
        self.even_btn = tk.Button(frame_even, text="Select Even Pages PDF", command=self.select_even)
        self.even_btn.pack(side=tk.LEFT)
        even_canvas = tk.Canvas(frame_even, width=60, height=60, highlightthickness=0)
        even_canvas.pack(side=tk.LEFT, padx=5)
        self.draw_icon(even_canvas, [6, 4, 2])

        # Combine button
        self.combine_btn = tk.Button(root, text="Combine Now", bg="green", fg="white", command=self.combine)
        self.combine_btn.pack(pady=20)

    def draw_icon(self, canvas: tk.Canvas, numbers: list[int]) -> None:
        """Draw overlapping page icon with given numbers."""
        width, height = 40, 50
        offset = 6
        for idx, num in enumerate(numbers[::-1]):  # draw bottom first
            x = offset * idx
            y = offset * (len(numbers) - idx - 1)
            canvas.create_rectangle(x, y, x + width, y + height, fill="white", outline="black")
            canvas.create_text(x + width / 2, y + height / 2, text=str(num), font=("Helvetica", 12, "bold"))

    def select_odd(self) -> None:
        self.odd_file = filedialog.askopenfilename(title="Select Odd Pages PDF", filetypes=[("PDF files", "*.pdf")])

    def select_even(self) -> None:
        self.even_file = filedialog.askopenfilename(title="Select Even Pages PDF", filetypes=[("PDF files", "*.pdf")])

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
