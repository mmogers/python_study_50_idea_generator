# 👉 Day 50 Challenge

Day 50! Boy, you are smashing this 100 days! 🎊 To celebrate, here's a project for you.

Your idea storage system should:

1. Prompt the user to add an idea, or load a random one.
2. Choosing 'Add an idea' results in:
   1. A prompt for the user to input their idea.
   2. Add the idea to a text file called 'my.ideas'.
   3. Add the idea in append mode, with every new idea on a brand new line.
3. Choosing 'Load random' results in:
    1. Load the list of ideas.
    2. Choose one at random.
    3. Display it on screen for a few seconds.
    4. Return to the menu.


Example:

```
🌟Idea Storage🌟

Add an idea or see a random idea? a/r. > r

Monkey tennis.

Add an idea or see a ranmdom idea? a/r. > a

Input your idea. > Youth hostelling with Chris Eubank

Nice! Your idea has been stored.
```

<details> <summary> 💡 Hints </summary>
  
- To pick an idea at random, you could use `split()` to get an array of values. Or you could use `random.choice` to generate a random number and keep loading lines until you get to the random number line.
- Try implementing your menu as a subroutine, so you can call it whenever you need to return to it.
</details>