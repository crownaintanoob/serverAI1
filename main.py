import simple_websocket
import json
import pygame
 
# initialising pygame
pygame.init()
ip = "142.170.107.132"
port = "2943"
screen = pygame.display.set_mode((800, 800))
def main():
    networkID = input("Pick the Network ID between 1-2: ")
    ws = simple_websocket.Client('ws://' + ip + ":" + port + "/" + str(networkID))
    dataToSend = {"KeyboardInputNetwork": {"W": False, "A": False, "S": False, "D": False}, "networkId": networkID}
    try:
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              exit()
           
            if event.type == pygame.KEYDOWN:
              print("key pressed")
              if event.key == pygame.K_w:
                dataToSend["KeyboardInputNetwork"]["W"] = True
              if event.key == pygame.K_a:
                dataToSend["KeyboardInputNetwork"]["A"] = True
              if event.key == pygame.K_s:
                dataToSend["KeyboardInputNetwork"]["S"] = True
              if event.key == pygame.K_d:
                dataToSend["KeyboardInputNetwork"]["D"] = True
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_w:
                dataToSend["KeyboardInputNetwork"]["W"] = False
              if event.key == pygame.K_a:
                dataToSend["KeyboardInputNetwork"]["A"] = False
              if event.key == pygame.K_s:
                dataToSend["KeyboardInputNetwork"]["S"] = False
              if event.key == pygame.K_d:
                dataToSend["KeyboardInputNetwork"]["D"] = False
            print(dataToSend["KeyboardInputNetwork"])
            ws.send(json.dumps(dataToSend))
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()

if __name__ == '__main__':
    main()
