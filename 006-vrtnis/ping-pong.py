import marimo

__generated_with = "0.8.13"
app = marimo.App()


@app.cell
def __():
    def install(package_name: str):
        import micropip
        import asyncio

        asyncio.get_running_loop().run_until_complete(micropip.install(package_name))

    install('random')
    return install,


@app.cell
def __():
    import time
    import marimo as mo

    # Game board dimensions and initial setup
    canvas_width, canvas_height = 40, 20
    user = {'x': 1, 'y': canvas_height // 2 - 2, 'width': 2, 'height': 4, 'score': 0}
    com = {'x': canvas_width - 3, 'y': canvas_height // 2 - 2, 'width': 2, 'height': 4, 'score': 0}
    ball = {'x': canvas_width // 2, 'y': canvas_height // 2, 'velocityX': 1, 'velocityY': 1}
    move_direction = 1  # Direction for user paddle movement: 1 for down, -1 for up

    # Function to create and return the current game board as an HTML string
    def create_board():
        board_html = '<div style="font-family: monospace; white-space: pre;">'
        for y in range(canvas_height):
            for x in range(canvas_width):
                if x == ball['x'] and y == ball['y']:
                    # Represent ball with a green circle
                    board_html += '<span style="color: green;">ⵔ</span>'
                elif (user['x'] <= x < user['x'] + user['width'] and user['y'] <= y < user['y'] + user['height']) or \
                     (com['x'] <= x < com['x'] + com['width'] and com['y'] <= y < com['y'] + com['height']):
                    # Represent paddles
                    board_html += '▮'
                else:
                    board_html += ' '
            board_html += '\n'
        board_html += f"Score: {user['score']} - {com['score']}</div>"
        return board_html

    def update_game():
        global move_direction
        # Update ball position
        import random
        ball['x'] += ball['velocityX']
        ball['y'] += ball['velocityY']

        # Ball collision with top or bottom
        if ball['y'] <= 0 or ball['y'] >= canvas_height - 1:
            ball['velocityY'] = -ball['velocityY']

        # Check for collision with user paddle
        if ball['x'] == user['x'] + 1 and user['y'] <= ball['y'] <= user['y'] + user['height']:
            ball['velocityX'] = -ball['velocityX']

        # Check for collision with com paddle
        if ball['x'] == com['x'] - 1 and com['y'] <= ball['y'] <= com['y'] + com['height']:
            ball['velocityX'] = -ball['velocityX']

        # Ball reset if it goes past a paddle (simple scoring)
        if ball['x'] < 0:
            com['score'] += 1
            reset_ball()
        elif ball['x'] > canvas_width - 1:
            user['score'] += 1
            reset_ball()

        # Randomly decide if the user paddle will miss
        if random.random() < 0.1:  # 10% chance to miss
            pass  # User paddle does nothing, simulating a miss
        else:
            # Move user paddle in a simple pattern
            user['y'] += move_direction
            if user['y'] <= 0 or user['y'] + user['height'] >= canvas_height:
                move_direction = -move_direction  # Change direction at bounds

        # Randomly decide if the com paddle will miss
        if random.random() < 0.1:  # 10% chance to miss
            pass  # Com paddle does nothing, simulating a miss
        else:
            # AI for com paddle (simplified)
            if com['y'] + com['height'] // 2 < ball['y']:
                com['y'] = min(com['y'] + 1, canvas_height - com['height'])
            elif com['y'] + com['height'] // 2 > ball['y']:
                com['y'] = max(com['y'] - 1, 0)

    def reset_ball():
        ball['x'], ball['y'] = canvas_width // 2, canvas_height // 2
        ball['velocityX'], ball['velocityY'] = 1, 1  # Reset velocity

    # Function to animate the game for a given number of steps
    def animate_game(steps, delay=0.1):
        for _ in range(steps):
            update_game()
            board_html = create_board()
            mo.output.replace(mo.Html(board_html))
            time.sleep(delay)  # Note: This is conceptual; actual behavior may vary in Marimo.

    # Start the animation
    animate_game(2000)  # Adjust steps or delay as necessary for desired play duration
    return (
        animate_game,
        ball,
        canvas_height,
        canvas_width,
        com,
        create_board,
        mo,
        move_direction,
        reset_ball,
        time,
        update_game,
        user,
    )


if __name__ == "__main__":
    app.run()