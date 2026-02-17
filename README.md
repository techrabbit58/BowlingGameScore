# Scoring a Bowling Game
## Task
Complete the [Bowling Game Kata](https://codingdojo.org/kata/Bowling/)
in contemporary python of the year 2026.

## Requirements
- There are ten pins in a bowling game. Players throw bowling balls
to the pins to knock as much of them as possible.
- Take "write a program..." as "write a bowling score function..."
- The bowling score function, that must be called with a finished
bowling line of a player, then calculates the total line score of
that player.
- The bowling line must be a string of characters containing all ten
**frames**, plus possibly up to two extra frames, separated by whitespace.
- Each frame must be composed of one or two symbols, one for each ball.
- If a ball has not knocked down any pins, this is represented by a **dash (-)**.
- The number of pins knocked down by the ball is represented as a singel digit, otherwise.
- If the second ball of a frame knocks down all remaining pins, this is represented
by a **slash (/)**. A frame with a slash for the second ball is called a **strike**.
- If the first ball of a frame alsredy nocked down all ten pins at once,
this is represented by a single "X", and then the frame is finished. Such a
single ball frame is called a **strike**.
- A **normal frame** with less than ten pins knocked counts as the number of
knocked-down pins from both balls together.
- A **spare** is scored as 10 points, plus the result of the _next_ ball.
- A **strike** is scored as 10 points, plus the results of the _next two_ balls.
- If the **last frame of a line** results in a **spare**, _one extra ball_ must be thrown
and then gets added to the last frame's score.
- If the **last frame of a line** results in a **strike**, _two extra balls_
must be thrown and then get added to the last frame's score.
- A **spare** always counts the number of pins knocked down after the first ball, 
and 10 after the second ball.
- A **strike** always counts 10 per ball.

## Non-Requirements
- Do not check for valid rolls.
- Do not check for correct number of rolls and frames.
- Do not provide scores for intermediate frames.
- It is assumed that all checking shall be done by the caller.
- The bowling score is not defined for malformed inputs.

## Line Examples
- "-- -- -- -- -- -- -- -- -- --", a line of gutters, score 0
- "X X X X X X X X X X X X", a perfect game of all strikes, score 300
- "5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5", all spares, score 150
- "9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", normal line with misses, score 90
- "12 12 12 12 12 12 12 12 12 12", normal line, no misses, score 30

## Scoring Examples
- A frame where both balls are misses: "--", score 0 (also called a "gutter game")
- A spare followed by another spare: "5/ 2/", first frame scores 12
- A spare followed by a strike: "7/ X", first frame scores 20
- A strike followed by a spare: "X 5/", first frame scores 20
- A normal frame: "71", score 8
- A strike followed by a normal frame: "X 52", first frame scores 17
- A strike followed by two strikes: "X X X", first frame scores 30
- A line with alternating strikes and spares only, score 200 (sometimes called a "Dutch 200")
- A line with all strikes (meaning ten strikes, and both extra balls are strikes as well),
score 300

---