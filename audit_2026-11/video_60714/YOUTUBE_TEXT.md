# Video description and comment (as posted)

## Video title (Arbolinea channel)

6174 has a five-digit cousin: 60714

## Video description

In 1949 the mathematician and schoolteacher D. R. Kaprekar found that his routine (sort the digits, subtract the reverse, repeat) sends every four-digit number to 6174, now called Kaprekar's constant. The four-digit result is his; this video is about what happens at five digits. At five digits the same routine never settles; it falls into loops.

Keep the same idea but change the order of the subtraction. Sort the five digits from biggest to smallest and call them A, B, C, D, E. Compute ADCBE minus DEACB, take the positive difference, keep five digits (leading zeros count), and repeat.

Every five-digit start ends at 60714, except the ten starts made of one repeated digit (00000, 11111, ...), which go to 0. The longest trip is 30 steps.

What kind of result this is: a complete computer check. Counting leading zeros there are 100,000 five-digit strings (00000 to 99999); leaving out the ten repeats, all 99,990 others end at 60714. Counting only true five-digit numbers (10000 to 99999), that is 89,991 of 90,000. It is not Kaprekar's routine, and at five digits we do not have a pen-and-paper proof. The rule was found by a computer search.

Why sort first? We also tried skipping the sort and just shuffling the digits as written. Of all 7,140 such rules at five digits, none sends every start to one number; for a typical one, about 98% of starts end in a loop. The closest gets 99,840 of 100,000 starts to a single number.

How it was made: we asked the questions and set the direction; AI models (Anthropic's Claude and OpenAI's ChatGPT) did the heavy lifting on the computation and checking.

Paper and details: https://arbolinea.com/60714/

## Comment for the Numberphile 6174 video

Five digits does have an answer if you change the order of the subtraction. Sort the digits biggest to smallest as A, B, C, D, E, then compute ADCBE − DEACB (take the positive difference, keep leading zeros) and repeat. Every five-digit number that is not a single repeated digit ends at 60714, the digits of 6174 plus a zero. Example: 58196 → 43713 → 41607 → 60714. This is a different rule from Kaprekar's, and it is a complete computer check of all 99,990 such starts (longest trip 30 steps), not a hand proof. Short video on the Arbolinea channel: "6174 has a five-digit cousin: 60714".

Note: YouTube often hides comments that contain links, so the comment names the video instead of linking it.

## Published

Uploaded to the Arbolinea channel on 2026-11-25, public: https://youtu.be/8B35aQmRqBg
