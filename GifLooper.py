import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageSequence
from threading import Thread

class SimpleGifEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Reddit GIF Looper")
        self.root.minsize(500, 300)
        
        self.input_gif_path = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Load GIF button
        self.load_button = tk.Button(self.root, text="Load GIF", command=self.load_gif)
        self.load_button.pack(pady=10)
        
        # Display loaded GIF path
        self.loaded_gif_label = tk.Label(self.root, text="No GIF loaded")
        self.loaded_gif_label.pack(pady=5)
        
        # Frame rate label and entry
        self.frame_rate_label = tk.Label(self.root, text="Frame Rate (fps) (1-120):")
        self.frame_rate_label.pack(pady=5)
        
        self.frame_rate_entry = tk.Entry(self.root)
        self.frame_rate_entry.pack(pady=5)
        self.frame_rate_entry.insert(0, "10")
        
        # Upscaling options
        self.upscale_label = tk.Label(self.root, text="Upscaling:")
        self.upscale_label.pack(pady=5)
        
        self.upscale_var = tk.StringVar(value="None")
        upscale_frame = tk.Frame(self.root)
        upscale_frame.pack(pady=5)
        upscale_options = ["None", "x2", "x4", "x8"]
        for option in upscale_options:
            tk.Radiobutton(upscale_frame, text=option, variable=self.upscale_var, value=option, command=self.update_output_size).pack(side=tk.LEFT)
        
        # Original size label
        self.original_size_label = tk.Label(self.root, text="Original Size: N/A")
        self.original_size_label.pack(pady=5)
        
        # Output size label
        self.output_size_label = tk.Label(self.root, text="Output Size: N/A")
        self.output_size_label.pack(pady=5)
        
        # Save GIF button
        self.save_button = tk.Button(self.root, text="Save GIF", command=self.save_gif, state=tk.DISABLED)
        self.save_button.pack(pady=10)
        
        # Attribution
        attribution_label = tk.Label(self.root, text="Simple GIF Looper by i_like_lips", fg="blue", cursor="hand2")
        attribution_label.pack(pady=5)
        attribution_label.bind("<Button-1>", lambda e: self.open_link("https://www.reddit.com/user/I_like_lips/"))
            
    def load_gif(self):
        self.input_gif_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
        if self.input_gif_path:
            self.loaded_gif_label.config(text=f"Loaded GIF: {self.input_gif_path}")
            self.save_button.config(state=tk.NORMAL)
            original_gif = Image.open(self.input_gif_path)
            self.original_size_label.config(text=f"Original Size: {original_gif.size[0]} x {original_gif.size[1]}")
            self.update_output_size()
            messagebox.showinfo("GIF Loaded", "GIF successfully loaded.")
    
    def save_gif(self):
        if self.input_gif_path:
            output_gif_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
            if output_gif_path:
                frame_rate = int(self.frame_rate_entry.get())
                upscale_factor = self.upscale_var.get()
                
                thread = Thread(target=self.process_gif, args=(self.input_gif_path, output_gif_path, frame_rate, upscale_factor))
                thread.start()
    
    def process_gif(self, input_path, output_path, frame_rate, upscale_factor):
        # Open the original gif
        original_gif = Image.open(input_path)
        
        # Extract frames from the original gif
        frames = [frame.copy() for frame in ImageSequence.Iterator(original_gif)]
        
        # Duplicate and reverse the frames
        reversed_frames = frames[::-1]
        all_frames = frames + reversed_frames
        
        # Calculate frame duration in milliseconds for smooth playback
        frame_duration = int(1000 / frame_rate)
        
        # Upscaling if needed
        if upscale_factor != "None":
            scale = int(upscale_factor[1])  # Get the scale factor from the string (e.g., "x2" -> 2)
            all_frames = self.resize_frames(all_frames, scale)
        
        # Save the new gif with the adjusted frame duration
        all_frames[0].save(output_path, save_all=True, append_images=all_frames[1:], loop=0, duration=frame_duration)

        # Display output size immediately after resizing
        output_gif = Image.open(output_path)
        self.output_size_label.config(text=f"Output Size: {output_gif.size[0]} x {output_gif.size[1]}")

        messagebox.showinfo("GIF Saved", "Modified GIF successfully saved.")

    def resize_frames(self, frames, scale):
        resized_frames = []
        for frame in frames:
            resized_frame = frame.resize((frame.width * scale, frame.height * scale), Image.NEAREST)
            resized_frames.append(resized_frame)
        return resized_frames

    def update_output_size(self):
        if self.input_gif_path:
            original_gif = Image.open(self.input_gif_path)
            upscale_factor = self.upscale_var.get()
            if upscale_factor != "None":
                scale = int(upscale_factor[1])
                output_size = (original_gif.size[0] * scale, original_gif.size[1] * scale)
            else:
                output_size = original_gif.size
            self.output_size_label.config(text=f"Output Size: {output_size[0]} x {output_size[1]}")

    def open_link(self, url):
        import webbrowser
        webbrowser.open_new(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGifEditor(root)
    root.mainloop()
