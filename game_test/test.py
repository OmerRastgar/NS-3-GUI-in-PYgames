import pygame
from pygame.locals import *
import subprocess
import os
import webbrowser
import signal

RED = (255, 0, 0)
GRAY = (150, 150, 150)
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
BLUE = pygame.Color('lightblue')

pygame.init()
pygame.display.set_caption('LTE Vulnerability Test Environment')
icon = pygame.image.load("lteicon.png")
pygame.display.set_icon(icon)
w, h = 750, 800
clock = pygame.time.Clock()

def pkt_flow(src,dst,msg,msg_img ,screen):
        step = 5
        x=(dst.x+40-src.x)//step
        y=(dst.y+40-src.y)//step
        c1= src.x
        c2= src.y
        
        q1=0
        q2=0
        for i in range(step):
            
            q1+=x
            q2+=y
            clock.tick_busy_loop(10)
            
            msg.center = (c1+q1,c2+q2)
            screen.blit(msg_img,msg )
            pygame.draw.rect(screen, GRAY, msg,1)
            pygame.display.update()
    
class EPC():
    def __init__(self):
        self.rectline= pygame.Rect(497, 257, 205, 205)
        self.rect= pygame.Rect(500, 260, 200, 200)
        self.SWG_img = pygame.image.load("router.png")
        self.SWG_img = pygame.transform.scale(self.SWG_img,(60,60))
        self.SWG_img.convert()
        self.PWG_img = pygame.image.load("router.png")
        self.PWG_img = pygame.transform.scale(self.PWG_img,(60,60))
        self.PWG_img.convert()
        self.Internet_img = pygame.image.load("internet.png")
        self.Internet_img = pygame.transform.scale(self.Internet_img,(60,60))
        self.Internet_img.convert()
        self.MME_img = pygame.image.load("server.png")
        self.MME_img = pygame.transform.scale(self.MME_img,(60,60))
        self.MME_img.convert()
        self.radio_img = pygame.image.load("radio-station.png")
        self.radio_img = pygame.transform.scale(self.radio_img,(90,90))
        self.radio_img.convert()
        self.enode_img = pygame.image.load("UE.png")
        self.enode_img = pygame.transform.scale(self.enode_img,(500,500))
        self.enode_img.convert()
        self.Phone_img = pygame.image.load("user.png")
        self.Phone_img = pygame.transform.scale(self.Phone_img,(200,400))
        self.enode_img.convert()
        self.server_img = pygame.image.load("server_arch.png")
        self.server_img = pygame.transform.scale(self.server_img,(200,400))
        self.server_img.convert()


        self.icon_SWG = self.SWG_img.get_rect()
        self.icon_SWG.center = 550,400
        self.icon_PWG = self.PWG_img.get_rect()
        self.icon_PWG.center = 640,400
        self.icon_Internet = self.Internet_img.get_rect()
        self.icon_Internet.center = 650,500
        self.icon_MME = self.MME_img.get_rect()
        self.icon_MME.center = 550,310
        self.icon_radio = self.radio_img.get_rect()
        self.icon_radio.center = 640,400
        self.icon_enode = self.enode_img.get_rect()
        self.icon_enode.center = 0,0
        self.icon_Phone = self.Phone_img.get_rect()
        self.icon_Phone.center = 0,0
        self.icon_server = self.server_img.get_rect()
        self.icon_server.center = 0,0




        self.base_font = pygame.font.Font(None,32)
        self.EPC= self.base_font.render("EPC",True,(0,0,0))
        self.SWG= self.base_font.render("SWG",True,(0,0,0))
    
        self.PWG= self.base_font.render("PWG",True,(0,0,0))
    
        self.MME= self.base_font.render("MME",True,(0,0,0))
        self.Internet= self.base_font.render("Internet",True,(0,0,0))
        self.arch = False
        self.phone=False
        self.Tower = False
        self.server=False
    
    def display(self,screen):
        if (self.arch):
            pygame.draw.rect(screen, BLACK, self.rectline,3)
            pygame.draw.rect(screen, BLUE,self.rect )
            screen.blit(self.SWG_img, self.icon_SWG)
            screen.blit(self.PWG_img, self.icon_PWG)
            screen.blit(self.MME_img, self.icon_MME)
            screen.blit(self.SWG,(self.icon_SWG.x,self.icon_SWG.y+70))
            screen.blit(self.PWG,(self.icon_PWG.x,self.icon_PWG.y+70))
            screen.blit(self.MME,(self.icon_MME.x,self.icon_MME.y+70))
            screen.blit(self.EPC,(self.icon_MME.x+80,self.icon_MME.y-20))
            pygame.draw.line(screen, BLACK, (self.icon_SWG.x+30,self.icon_SWG.y+30),(self.icon_PWG.x+30,self.icon_PWG.y+30), 3)
            pygame.draw.line(screen, BLACK, (self.icon_SWG.x+30,self.icon_SWG.y+30),(self.icon_MME.x+30,self.icon_MME.y+30), 3)
        else:
             screen.blit(self.radio_img, self.icon_radio)
        screen.blit(self.Internet_img, self.icon_Internet)
        screen.blit(self.Internet,(self.icon_Internet.x,self.icon_Internet.y+70))
        if (self.phone):
            screen.blit(self.Phone_img, self.icon_Phone)
        if (self.Tower):
            screen.blit(self.enode_img, self.icon_enode)
        if (self.server):
            screen.blit(self.server_img, self.icon_server)



        pygame.draw.line(screen, BLACK, (self.icon_Internet.x+30,self.icon_Internet.y+30),(self.icon_PWG.x+30,self.icon_PWG.y+30), 3)
    
        
      

        
        
        


class Menu():
    def __init__(self):
        
        self.select_img = pygame.image.load("click.png")
        self.select_img = pygame.transform.scale(self.select_img,(40,40))
        self.select_img.convert()
        self.wire_img = pygame.image.load("wire.png")
        self.wire_img = pygame.transform.scale(self.wire_img,(40,40))
        self.wire_img.convert()
        self.disconnect_img = pygame.image.load("disconnect.png")
        self.disconnect_img = pygame.transform.scale(self.disconnect_img,(40,40))
        self.disconnect_img.convert()
        self.ping_img = pygame.image.load("chrome.png")
        self.ping_img = pygame.transform.scale(self.ping_img,(40,40))
        self.ping_img.convert()
        self.inspection_img = pygame.image.load("inspection.png")
        self.inspection_img = pygame.transform.scale(self.inspection_img,(40,40))
        self.inspection_img.convert()
        self.arch_img = pygame.image.load("project.png")
        self.arch_img = pygame.transform.scale(self.arch_img,(40,40))
        self.arch_img.convert()
        self.bar = pygame.Rect(0,h-(h*0.02),w,h*0.02)
        

        
        self.icon_select = self.select_img.get_rect()
        self.icon_select.center = 230,30
        self.icon_wire = self.wire_img.get_rect()
        self.icon_wire.center = 290,30
        self.icon_disconnect = self.disconnect_img.get_rect()
        self.icon_disconnect.center = 350,30
        self.icon_ping = self.ping_img.get_rect()
        self.icon_ping.center = 400,30
        self.icon_inspection = self.inspection_img.get_rect()
        self.icon_inspection.center = 450,30
        self.icon_arch = self.inspection_img.get_rect()
        self.icon_arch.center = 500,30

        
        self.mode= 0
        self.connections=[]
        self.cursor=self.select_img.get_rect()
        self.count=0
    
    
    def display(self,screen):
        self.cursor.center = pygame.mouse.get_pos()
        screen.blit(self.select_img, self.icon_select)
        screen.blit(self.wire_img, self.icon_wire)
        screen.blit(self.disconnect_img, self.icon_disconnect)
        screen.blit(self.ping_img, self.icon_ping)
        screen.blit(self.inspection_img, self.icon_inspection)
        screen.blit(self.arch_img, self.icon_arch)
        pygame.draw.rect(screen, WHITE ,self.bar )
        for i in range(len(self.connections)):
                pygame.draw.line(screen, BLACK, (self.connections[i][0][2].x+40,self.connections[i][0][2].y+40),(self.connections[i][1][2].x+40,self.connections[i][1][2].y+40), 3)
        if(not(self.mode)):    
             pygame.mouse.set_visible(True)
        elif (self.mode == 1):
            self.cursor.center = pygame.mouse.get_pos()
            screen.blit(self.wire_img, self.cursor)
            pygame.mouse.set_visible(False)      
        elif (self.mode == 2):
            self.cursor.center = pygame.mouse.get_pos()
            screen.blit(self.disconnect_img, self.cursor)
            pygame.mouse.set_visible(False)
        elif (self.mode == 3):
            self.cursor.center = pygame.mouse.get_pos()
            screen.blit(self.ping_img, self.cursor)
            pygame.mouse.set_visible(False)
        elif (self.mode == 4):
            self.cursor.center = pygame.mouse.get_pos()
            screen.blit(self.inspection_img, self.cursor)
            pygame.mouse.set_visible(False)
        elif (self.mode == 5):
            self.cursor.center = pygame.mouse.get_pos()
            screen.blit(self.arch_img, self.cursor)
            pygame.mouse.set_visible(False)

          
    def check_input(self, event):
        if (event.type == MOUSEBUTTONDOWN):
            if (self.icon_select.collidepoint(event.pos)):
                self.mode= 0
            elif(self.icon_wire.collidepoint(event.pos)):
                self.mode= 1
            elif(self.icon_disconnect.collidepoint(event.pos)):
                self.mode= 2
            elif(self.icon_ping.collidepoint(event.pos)):
                self.mode= 3
            elif(self.icon_inspection.collidepoint(event.pos)):
                self.mode= 4
            elif(self.icon_arch.collidepoint(event.pos)):
                self.mode= 5

        if event.type == pygame.KEYDOWN :
               
            if event.key == pygame.K_ESCAPE:
                self.mode = 0
                pygame.mouse.set_visible(True)
        
    
    def add_connections(self,device1,device2):
        self.connections.append((device1,device2))
        self.count +=1

class element():
  
    

    def __init__(self, IP,Filename,x,y,Name ):
        self.name=Name
        self.xx=0
        self.yy=0
        self.count= 0
        self.click = False
        self.keyboard_enable=False
        self.icon = ""
        self.IP= []
        self.text_surface=[]
        self.rect = []
        self.IP.append(IP)
        self._img = pygame.image.load(Filename)
        self._img = pygame.transform.scale(self._img,(80,80))
        self._img.convert()
        self.base_font = pygame.font.Font(None,32)
        self.text_surface.append(self.base_font.render(IP[self.count],True,(0,0,0)))
        self.icon = self._img.get_rect()
        self.icon.center = x,y


    def display(self, screen):
        screen.blit(self._img, self.icon)
        if (len(self.rect)):
            pygame.draw.rect(screen, RED, self.rect[self.count],2,0,)
        for i in range(len(self.rect)):
            self.text_surface[i]= self.base_font.render(self.IP[i],True,(0,0,0))
            screen.blit(self.text_surface[i],(self.rect[i].x,self.rect[i].y+100))
            screen.blit(self._img, self.rect[i])
        return screen
        

    def add_device(self,IP):
        self.IP.append(IP)
        self.base_font = pygame.font.Font(None,32)
        self.text_surface.append(self.base_font.render(IP[len(self.rect)-1],True,(0,0,0)))
        self.rect.append(self._img.get_rect())
        self.count+=1
        self.keyboard_enable=True
        self.rect[len(self.rect)-1].move_ip(self.icon.x,self.icon.y)
        self.click=True

    def check_input(self,event):
        if (event.type == MOUSEBUTTONDOWN):
            if (len(self.rect)):
                if self.rect[self.count].collidepoint(event.pos):
                    if (event.button == 1):  
                        self.click = True
                    if (event.button == 3):
                        self.keyboard_enable= True
                        self.xx, self.yy = event.pos
                    
            if self.icon.collidepoint(event.pos):
                self.add_device("10.0.0.0")
            
            for i in range(len(self.rect)):
                if self.rect[i].collidepoint(event.pos):
                    self.count = i
                    
        elif(event.type == MOUSEBUTTONUP):
            self.click = False
        if event.type == MOUSEMOTION :
            if (self.click):
                self.rect[self.count].move_ip(event.rel)

        if event.type == pygame.KEYDOWN :

            if self.keyboard_enable == True and self.rect[self.count].collidepoint(self.xx,self.yy)  :
                if event.key == pygame.K_BACKSPACE:
                    self.IP[self.count]= self.IP[self.count][:-1]
                elif event.key == pygame.K_RETURN:
                    self.keyboard_enable= False
                elif (event.unicode.isdigit()):
                    self.IP[self.count] += event.unicode
                elif (event.unicode == '.'):
                        self.IP[self.count] += event.unicode


    def Dump(self):
        return [self.IP,len(self.rect)]






def main():
    os.chdir('app') # This will change the present working directory
    x= subprocess.Popen("dx.py", stdout=subprocess.PIPE, 
                       shell=True)

    os.chdir('..')
    screen = pygame.display.set_mode((w, h))
    
    running = True
    imp = pygame.image.load("map.jpg").convert()
    imp = pygame.transform.scale(imp,(w,h))
    
    
    play__img = pygame.image.load('play-button.png')
    play__img = pygame.transform.scale(play__img,(80,80))
    play__img.convert()
    stop__img = pygame.image.load('stop-button.png')
    stop__img = pygame.transform.scale(stop__img,(80,80))
    stop__img.convert()
    
    msg_img = pygame.image.load('email.png')
    msg_img = pygame.transform.scale(msg_img,(40,40))
    msg_img.convert()
    

    Tower=element("192.168.10.1","cell-tower.png",40,60,"tower")
    Phone=element("192.168.10.2","smartphone.png",40,160,"phone")
    Hacker=element("192.168.10.3","hacker .png",40,260,"hacker")
    message=element("10.8.0.4","server.png",40,360, "message")
    menu  = Menu()

    base_font = pygame.font.SysFont('arial', 15)
    text_surface = base_font.render("0,0",True,(0,0,0))



    msg = msg_img.get_rect()
    msg.center = 0,0
    play = play__img.get_rect(topleft=(450, 700))
    stop = stop__img.get_rect(topleft=(550, 700))
    panel = pygame.rect.Rect(0,0,w//8,h)
    TOPpanel = pygame.rect.Rect(200,5,w//2,h//16)
    selected = 0 
    sent = 0
    enum = 0 

    cellsite=  EPC()
    while running:

        for event in pygame.event.get():
            

            if(menu.mode == 0):
                Tower.check_input(event)
                Phone.check_input(event)
                Hacker.check_input(event)
                message.check_input(event)
            menu.check_input(event)
            
            if event.type == QUIT:
                subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=x.pid))
                running = False
            

            
            
            elif event.type == MOUSEBUTTONDOWN:
                if play.collidepoint(event.pos):
                    sent = 1
                    msg.move_ip(Phone.rect[0].x,Phone.rect[0].y )
                
                cellsite.arch= False
                cellsite.phone=False
                cellsite.Tower=False
                cellsite.server=False
                if(menu.mode == 3):
                    if(Phone.rect[0].collidepoint(event.pos)):
                        url = "http://localhost:5000/"
                        webbrowser.open(url,0,0)
                if(menu.mode == 4):
                    if(cellsite.rect.collidepoint(event.pos)):
                        os.startfile("LTE.pcap")
                    if(Tower.rect[0].collidepoint(event.pos)):
                        os.startfile("tower.pcap")
                    if(Phone.rect[0].collidepoint(event.pos)):
                        os.startfile("UE.pcap")
                    if(message.rect[0].collidepoint(event.pos)):
                        os.startfile("server.pcap")
                if(menu.mode == 5):
                    if(cellsite.icon_radio.collidepoint(event.pos)):
                                 cellsite.arch=True       
                    if(Tower.rect[0].collidepoint(event.pos)):
                                 cellsite.Tower=True   
                                 cellsite.icon_enode.center= (event.pos[0]+100,event.pos[1]+100)    
                    if(Phone.rect[0].collidepoint(event.pos)):
                                 cellsite.phone=True   
                                 cellsite.icon_Phone.center= event.pos     
                    if(message.rect[0].collidepoint(event.pos)):
                                 cellsite.server=True   
                                 cellsite.icon_server.center= event.pos    
                if (menu.mode == 1):
                    if(not(selected)):
                        for i in range(len(Tower.rect)):
                            if Tower.rect[i].collidepoint(event.pos):
                                selected= [Tower.name,Tower.count-1,Tower.rect[i]]
                        for i in range(len(Phone.rect)):
                            if Phone.rect[i].collidepoint(event.pos):
                                selected= [Phone.name,Phone.count-1,Phone.rect[i]]
                    else:
                        
                        for i in range(len(Tower.rect)):
                            if Tower.rect[i].collidepoint(event.pos):
                                menu.add_connections(selected,[Tower.name,i,Tower.rect[i]])
                                selected = 0
                        for i in range(len(Phone.rect)):
                            if Phone.rect[i].collidepoint(event.pos):
                                menu.add_connections(selected,[Phone.name,i,Phone.rect[i]])
                                selected = 0
                else:
                    selected=False
            
                        
        for i in range(len(menu.connections)):
            
            
            
            if (menu.connections[i][0][0] == "tower"):
                
                menu.connections[i][0][2]=Tower.rect[menu.connections[i][0][1]]
            
            if (menu.connections[i][0][0] == "phone"):
                
                menu.connections[i][0][2]=Phone.rect[menu.connections[i][0][1]]
            
            if (menu.connections[i][1][0] == "tower"):
                menu.connections[i][1][2]=Tower.rect[menu.connections[i][1][1]]
            
            if (menu.connections[i][1][0] == "phone"):
                menu.connections[i][1][2]=Phone.rect[menu.connections[i][1][1]]
    

        screen.fill(GRAY)
        #panel
        screen.blit(imp, (0, 0))
        pygame.draw.rect(screen, GRAY, panel)
        pygame.draw.rect(screen, GRAY, TOPpanel)
        #icon
        
        screen.blit(play__img, play)
        pygame.draw.rect(screen, GRAY, play,1)
        screen.blit(stop__img, stop)
        pygame.draw.rect(screen, GRAY, stop,1)

        for i in range(len(Tower.rect)):
            pygame.draw.line(screen,BLACK,(Tower.rect[i].x+40,Tower.rect[i].y+40),(cellsite.icon_PWG.x+30,cellsite.icon_PWG.y+30),3)
        
        
        
        Tower.display(screen)
        Phone.display(screen)
        Hacker.display(screen)
        
        message.display(screen)
        if( not(sent) ):
            menu.display(screen)
        elif(sent):
            if(len(Hacker.rect)):
                g=0
            else:
                menu.display(screen)
        
       
        for i in range(len(message.rect)):
                pygame.draw.line(screen,BLACK,(message.rect[i].x+40,message.rect[i].y+40),(cellsite.icon_Internet.x+30,cellsite.icon_Internet.y+30),3)
        cellsite.display(screen)
        if (sent):
            if(len(Phone.rect)):
                if(len(Hacker.rect)):
                    pygame.draw.line(screen,BLACK,(Phone.rect[0].x+40,Phone.rect[0].y+40),(Hacker.rect[0].x+30,Hacker.rect[0].y+30),3)
                    pygame.draw.line(screen,BLACK,(Tower.rect[0].x+40,Tower.rect[0].y+40),(Hacker.rect[0].x+30,Hacker.rect[0].y+30),3)
                    if (sent == 1):
                        pkt_flow(Phone.rect[0],Hacker.rect[0],msg,msg_img,screen)
                        pkt_flow(Hacker.rect[0],Tower.rect[0],msg,msg_img,screen)
                        pkt_flow(Tower.rect[0],cellsite.icon_SWG,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_PWG,cellsite.icon_Internet,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_Internet,message.rect[0],msg,msg_img,screen)
                        sent =2
                    if (sent == 3 ):
                        pkt_flow(message.rect[0],cellsite.icon_Internet,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_Internet,cellsite.icon_PWG,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_SWG,Tower.rect[0],msg,msg_img,screen)
                        pkt_flow(Tower.rect[0],Hacker.rect[0],msg,msg_img,screen)
                        pkt_flow(Hacker.rect[0],Phone.rect[0],msg,msg_img,screen)
                        sent =-1
                    sent +=1
                    
                else:
                    if (sent == 1):
                        pkt_flow(Phone.rect[0],Tower.rect[0],msg,msg_img,screen)
                        pkt_flow(Tower.rect[0],cellsite.icon_SWG,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_PWG,cellsite.icon_Internet,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_Internet,message.rect[0],msg,msg_img,screen)
                        sent =2
                    if (sent == 3 ):
                        pkt_flow(message.rect[0],cellsite.icon_Internet,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_Internet,cellsite.icon_PWG,msg,msg_img,screen)
                        pkt_flow(cellsite.icon_SWG,Tower.rect[0],msg,msg_img,screen)
                        pkt_flow(Tower.rect[0],Phone.rect[0],msg,msg_img,screen)
                        sent =-1
                    sent +=1
                        
            
            screen.blit(msg_img, msg)
        clock.tick(24)
        text_surface= base_font.render(str(pygame.mouse.get_pos()),True,(0,0,0))
        screen.blit(text_surface,(w-80,h-18))
        

        
        pygame.display.update()
        
            

    pygame.quit()



main()

    
    