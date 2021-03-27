https://xss-game.appspot.com/level1
Mission Description
This level demonstrates a common cause of cross-site scripting where user input is directly included in the page without proper escaping.

Interact with the vulnerable application window below and find a way to make it execute JavaScript of your choosing. You can take actions inside the vulnerable window or directly edit its URL bar.
Mission Objective
Inject a script to pop up a JavaScript alert() in the frame below.

Once you show the alert you will be able to advance to the next level.

Solution: https://xss-game.appspot.com/level1/frame?query=<script>alert('wtf')</script>
