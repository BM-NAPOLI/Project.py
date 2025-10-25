import random
import curses

def main(stdscr):
    # إعداد نافذة الكورسيز
    curses.curs_set(0)         # إخفاء المؤشر
    stdscr.nodelay(1)          # إدخال غير محجوز
    stdscr.timeout(200)        # زيادة سرعة اللعبة (كل 100 مللي ثانية)

    while True:  # حلقة إعادة تشغيل اللعبة
        # أبعاد الشاشة
        sh, sw = stdscr.getmaxyx()

        # موضع بدء الثعبان
        snk_x = sw // 4
        snk_y = sh // 2
        snake = [
            [snk_y, snk_x],
            [snk_y, snk_x - 1],
            [snk_y, snk_x - 2]
        ]

        # موضع بدء الطعام (أمام الثعبان)
        food = [snk_y, snk_x + 5]

        # الاتجاه الأولي
        key = curses.KEY_RIGHT

        # حلقة اللعبة
        while True:
            stdscr.clear()
            stdscr.border()

            # قراءة إدخال المفتاح
            next_key = stdscr.getch()
            key = key if next_key == -1 else next_key

            # فحص إذا اصطدم الثعبان بنفسه فقط
            if snake[0] in snake[1:]:
                msg1 = "GAME OVER!"
                msg2 = "Press any key to play again"
                # تأكد من أن الرسائل تناسب الشاشة
                if len(msg1) < sw and len(msg2) < sw and sh > 4:
                    y1 = max(1, min(sh // 2 - 1, sh - 3))
                    y2 = max(2, min(sh // 2 + 1, sh - 2))
                    x1 = max(1, min(sw // 2 - len(msg1) // 2, sw - len(msg1) - 1))
                    x2 = max(1, min(sw // 2 - len(msg2) // 2, sw - len(msg2) - 1))
                    try:
                        stdscr.addstr(y1, x1, msg1)
                        stdscr.addstr(y2, x2, msg2)
                    except curses.error:
                        stdscr.addstr(1, 1, "GAME OVER! Press key")
                stdscr.refresh()
                stdscr.nodelay(0)  # تفعيل انتظار المفتاح
                stdscr.getch()     # انتظار ضغط أي مفتاح
                stdscr.nodelay(1)  # إعادة تفعيل الإدخال غير المحجوز
                break

            # حساب موضع الرأس الجديد
            new_head = [snake[0][0], snake[0][1]]

            if key == curses.KEY_DOWN:
                new_head[0] += 1
            elif key == curses.KEY_UP:
                new_head[0] -= 1
            elif key == curses.KEY_LEFT:
                new_head[1] -= 1
            elif key == curses.KEY_RIGHT:
                new_head[1] += 1

            # جعل الثعبان يمر عبر الجدران
            if new_head[0] <= 0:
                new_head[0] = sh - 2
            elif new_head[0] >= sh - 1:
                new_head[0] = 1
            elif new_head[1] <= 0:
                new_head[1] = sw - 2
            elif new_head[1] >= sw - 1:
                new_head[1] = 1

            snake.insert(0, new_head)

            # فحص إذا أكل الثعبان الطعام
            if snake[0] == food:
                while True:
                    nf = [
                        random.randint(1, sh - 2),
                        random.randint(1, sw - 2)
                    ]
                    if nf not in snake:
                        food = nf
                        break
            else:
                snake.pop()

            # رسم الثعبان
            for y, x in snake:
                if 1 <= y < sh-1 and 1 <= x < sw-1:
                    try:
                        stdscr.addch(y, x, '#')
                    except curses.error:
                        pass

            # رسم الطعام
            if 1 <= food[0] < sh-1 and 1 <= food[1] < sw-1:
                try:
                    stdscr.addch(food[0], food[1], '*')
                except curses.error:
                    pass

            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)