import tkinter as tk, random

class MyFirstApp:
    def __init__(self):
        root = tk.Tk()
        root.title("Dice Roller")
        root.geometry("500x500")
        self.root=root
        self.root.config(bg='yellow')
        self.canvas= tk. Canvas(root, width=200, height=200, bg="purple")
        self.canvas.pack()
        self.button = tk.Button(root, text="Click me ", command=self.roll_dice)
        self.button.pack()

        self.root.mainloop()

    def roll_dice(self):
        guess = random.randint(1,6)
        self.draw_dice(guess=guess)

    def draw_dice(self, guess):
        self.canvas.delete('all')

        positions = {
            1: [(100,100)],
            2: [(50,50),(150,150)],
            3: [(50,50),(100,100),(150,150)],
            4: [(50,50),(50,150),(150,50),(150,150)],
            5: [(50,50), (50,150),(150,50), (150,150), (100,100)],
            6: [(50,50), (50,100), (50,150), (150,50), (150,100), (150,150)]
        }

        for x,y in positions[guess]:
            self.canvas.create_rectangle((x-10,y-10),(x+10,y+10), fill='green')

        
def main():
    app=MyFirstApp()

if (__name__=="__main__"):
    main()






