import sys, pygame

pygame.init()

setup = {
	"resolution": (1920, 1080),
	"fullscreen": True,
	"backgroundColor": "#ff0000",
	"backgroundImg": [],
	"buttonColor": "#ffffff",
	"countdownColor1": "#00ff00",
	"countdownColor2": "ffff00",
	"countdownColor3": "ff0000",
	"countdownStart": "5",
	"cameraIndicator": "up",
	"cameraIndicatorColor": "#ffffff",
	"message": "SAY CHEESE!",
	"messagePosition": "bottom"
}

def hex2color(hex):
	r = hex[1:3]
	g = hex[3:5]
	b = hex[5:7]
	
	return (int(r, 16), int(g, 16), int(b, 16))
	
def drawText(text, font, size, color):
	return pygame_font.Font(font, size).render(text, True, color)

screen = pygame.display.set_mode(setup["resolution"], pygame.FULLSCREEN if setup["resolution"] else 0)
# draw background color
screen.fill(hex2color(setup["backgroundColor"]))

#draw background image

#draw camera indicator

#draw message

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
	
	#draw start button/countdown
	
    pygame.display.flip()