# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=ICF8b1aL5lM)

<details> <summary> 👀 Answer </summary>

```python
import os, time, random

def add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  else:
    show()
```

</details>


- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)