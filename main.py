import pygame

pygame.init()
windowwidth = 720 
pixelwidth = windowwidth //3 
screen = pygame.display.set_mode((windowwidth,windowwidth))  
clock = pygame.time.Clock()  
running = True        

def load_icons(path, resolution):     
    icon = pygame.image.load(path)      
    return pygame.transform.scale(icon,resolution)   

board = [           
    [None,None,None],          
    [None,None,None],          
    [None,None,None],                    
]      

icon_x = load_icons('icons/x.png',[pixelwidth , pixelwidth]) 
icon_o = load_icons('icons/o.png',[pixelwidth ,pixelwidth]) 
grid = load_icons('icons/grid.png',[windowwidth, windowwidth])   

player = 0     

def play_run(current_player):     
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Calculate column and row based on mouse position
    col = mouse_x // pixelwidth
    row = mouse_y // pixelwidth
    
    if pygame.mouse.get_pressed()[0]:         
        # Ensure the click is within the board
        if 0 <= row < 3 and 0 <= col < 3:
            # Only place if cell is empty
            if board[row][col] is None:
                board[row][col] = 0 if current_player == 0 else 1          
                global player          
                player = 1 - player                     

def draw_icons():     
    for i, row in enumerate(board):         
        for j, col in enumerate(row):             
            if board[i][j] == 0:                 
                screen.blit(icon_o,(j * pixelwidth ,i * pixelwidth))
            if board[i][j] == 1:                     
                screen.blit(icon_x,(j * pixelwidth,i * pixelwidth))

def check_winner():
    # Check rows
    for row in board:
        if row[0] is not None and row.count(row[0]) == 3:
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None

while running:     
    for event in pygame.event.get():         
        if event.type == pygame.QUIT:             
            running = False
        
        # Reset game on space key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            board[:] = [[None,None,None], [None,None,None], [None,None,None]]
            player = 0

    pygame.display.flip()      
    screen.blit(grid,(0, 0))     
    play_run(player)     
    draw_icons()

    # Check for winner
    winner = check_winner()
    if winner is not None:
        font = pygame.font.Font(None, 74)
        text = font.render(f"Player {winner + 1} Wins!", True, (255, 0, 0))
        screen.blit(text, (windowwidth // 4, windowwidth // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait 2 seconds before resetting
        board[:] = [[None,None,None], [None,None,None], [None,None,None]]
        player = 0

    clock.tick(50)   

pygame.quit()